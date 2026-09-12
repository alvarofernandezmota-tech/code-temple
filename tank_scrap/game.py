"""Bucle principal de TANK SCRAP 1990.

La vuelta de tuerca: cada ladrillo que se rompe en el campo deja CHATARRA.
La recoges pisandola y la gastas construyendo muro donde te convenga, asi que
el escenario deja de ser decorado y pasa a ser tu arsenal defensivo.
"""
import random

import pygame

from . import field as fld
from . import levels, pixfont, sprites
from .constants import (
    BLACK, DIR_VECTORS, BUILD_COOLDOWN, BUILD_RANGE_TILES, COST_BRICK, COST_STEEL, DOWN,
    ENEMIES_ON_FIELD, ENEMY_SPAWN_DELAY, FIELD_PX, FIELD_TILES, FPS, GHOST_NO,
    GHOST_OK, GREY_FRAME, HUD_DIM, LEFT, MARGIN_PX, PLAYER_LIVES,
    PLAYER_SPAWN_SHIELD, RIGHT, SCALE, SCORE_BY_KIND, SCORE_STAGE_CLEAR,
    SCRAP_START, SCREEN_H, SCREEN_W, TANK_PX, TILE, UP, WHITE,
)
from .entities import Bullet, EnemyTank, Explosion, PlayerTank, Scrap

ORIGIN = (MARGIN_PX, MARGIN_PX)

TITLE, PLAY, CLEARED, GAME_OVER = "title", "play", "cleared", "over"

SPAWN_TILES = ((0, 0), (12, 0), (24, 0))
PLAYER_SPAWN_TILE = (8, 24)

MOVE_KEYS = {
    pygame.K_UP: UP, pygame.K_w: UP,
    pygame.K_RIGHT: RIGHT, pygame.K_d: RIGHT,
    pygame.K_DOWN: DOWN, pygame.K_s: DOWN,
    pygame.K_LEFT: LEFT, pygame.K_a: LEFT,
}


def stage_roster(stage_index):
    """Lista de enemigos de la fase: mas duros a medida que avanzas."""
    n = stage_index + 1
    roster = ["basic"] * max(4, 8 - n)
    roster += ["fast"] * min(6, 1 + n)
    roster += ["power"] * min(5, n)
    roster += ["armor"] * max(0, n - 1)
    random.shuffle(roster)
    return roster


class Game:
    def __init__(self, seed=None):
        if seed is not None:
            random.seed(seed)
        self.surface = pygame.Surface((SCREEN_W, SCREEN_H))
        self.state = TITLE
        self.frame = 0
        self.score = 0
        self.lives = PLAYER_LIVES
        self.stage_index = 0
        self.scrap = SCRAP_START
        self.build_mode = False
        self.build_cursor = [0, 0]
        self.build_cd = 0.0
        self.message = ""
        self.message_timer = 0.0
        self.state_timer = 0.0
        self.paused = False
        self.quit = False
        self._load_stage(0, reset_run=True)

    # --- ciclo de vida de la fase -----------------------------------------
    def _load_stage(self, index, reset_run=False):
        self.stage_index = index
        self.field = fld.Field(levels.stage(index))
        self.bullets = []
        self.enemies = []
        self.scraps = []
        self.explosions = []
        self.queue = stage_roster(index)
        self.spawn_timer = 0.6
        self.spawn_slot = 0
        if reset_run:
            self.score = 0
            self.lives = PLAYER_LIVES
            self.scrap = SCRAP_START
        self._spawn_player()
        self.build_mode = False

    def _spawn_player(self):
        tx, ty = PLAYER_SPAWN_TILE
        self.player = PlayerTank(tx * TILE, ty * TILE)
        self.player.shield = PLAYER_SPAWN_SHIELD
        self.build_cursor = [tx, ty - 2]

    def _spawn_enemy(self):
        if not self.queue or len(self.enemies) >= ENEMIES_ON_FIELD:
            return
        tx, ty = SPAWN_TILES[self.spawn_slot % len(SPAWN_TILES)]
        self.spawn_slot += 1
        spot = pygame.Rect(tx * TILE, ty * TILE, TANK_PX, TANK_PX)
        if self.field.blocks_tank_rect(spot):
            return
        for t in self.enemies + [self.player]:
            if t and not t.dead and t.rect.colliderect(spot):
                return
        kind = self.queue.pop()
        self.enemies.append(EnemyTank(spot.x, spot.y, kind))
        self.explosions.append(Explosion(spot.centerx, spot.centery))

    # --- entrada ----------------------------------------------------------
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
            return
        if event.type != pygame.KEYDOWN:
            return
        key = event.key
        if key == pygame.K_ESCAPE:
            self.quit = True
        elif self.state == TITLE:
            if key in (pygame.K_RETURN, pygame.K_SPACE):
                self._load_stage(0, reset_run=True)
                self.state = PLAY
        elif self.state == GAME_OVER:
            if key in (pygame.K_RETURN, pygame.K_SPACE, pygame.K_r):
                self.state = TITLE
        elif self.state == PLAY:
            self._handle_play_key(key)

    def _handle_play_key(self, key):
        if key == pygame.K_p:
            self.paused = not self.paused
            return
        if self.paused:
            return
        if key == pygame.K_b:
            self.build_mode = not self.build_mode
            if self.build_mode:
                self._reset_cursor()
            return
        if self.build_mode:
            if key in MOVE_KEYS:
                self._move_cursor(MOVE_KEYS[key])
            elif key == pygame.K_SPACE:
                self._build(fld.BUILT_BRICK, COST_BRICK)
            elif key in (pygame.K_LSHIFT, pygame.K_RSHIFT, pygame.K_e):
                self._build(fld.BUILT_STEEL, COST_STEEL)
            elif key in (pygame.K_x, pygame.K_BACKSPACE):
                self._demolish()
            return
        if key == pygame.K_SPACE:
            self._player_fire()

    def _reset_cursor(self):
        r = self.player.rect
        dx, dy = DIR_VECTORS[self.player.direction]
        self.build_cursor = [
            max(0, min(FIELD_TILES - 1, r.centerx // TILE + dx * 2)),
            max(0, min(FIELD_TILES - 1, r.centery // TILE + dy * 2)),
        ]

    def _move_cursor(self, direction):
        dx, dy = DIR_VECTORS[direction]
        nx = max(0, min(FIELD_TILES - 1, self.build_cursor[0] + dx))
        ny = max(0, min(FIELD_TILES - 1, self.build_cursor[1] + dy))
        r = self.player.rect
        if (abs(nx - r.centerx // TILE) <= BUILD_RANGE_TILES
                and abs(ny - r.centery // TILE) <= BUILD_RANGE_TILES):
            self.build_cursor = [nx, ny]

    def _cursor_blocked_by_tank(self, tx, ty):
        cell = pygame.Rect(tx * TILE, ty * TILE, TILE, TILE)
        tanks = [self.player] + self.enemies
        return any(t and not t.dead and t.rect.colliderect(cell) for t in tanks)

    def _build(self, kind, cost):
        tx, ty = self.build_cursor
        if self.build_cd > 0:
            return
        if self.scrap < cost:
            self._say("no scrap")
            return
        if self._cursor_blocked_by_tank(tx, ty) or not self.field.can_build(tx, ty):
            self._say("no cabe")
            return
        self.field.build(tx, ty, kind)
        self.scrap -= cost
        self.build_cd = BUILD_COOLDOWN

    def _demolish(self):
        tx, ty = self.build_cursor
        refund = self.field.demolish(tx, ty)
        if refund:
            self.scrap += refund
            self.build_cd = BUILD_COOLDOWN
        else:
            self._say("no es tuyo")

    def _player_fire(self):
        mine = [b for b in self.bullets if b.owner == "player" and not b.dead]
        if len(mine) >= self.player.max_bullets:
            return
        mx, my = self.player.muzzle()
        self.bullets.append(Bullet(mx, my, self.player.direction,
                                   self.player.bullet_speed, "player"))

    def _say(self, text, seconds=1.1):
        self.message = text
        self.message_timer = seconds

    # --- actualizacion ----------------------------------------------------
    def update(self, dt, keys=None):
        self.frame += 1
        self.state_timer += dt
        if self.message_timer > 0:
            self.message_timer -= dt
        if self.state == CLEARED:
            if self.state_timer > 2.2:
                self.score += SCORE_STAGE_CLEAR
                self._load_stage(self.stage_index + 1)
                self.state = PLAY
                self.state_timer = 0.0
            return
        if self.state != PLAY or self.paused:
            return

        self.field.update(dt)
        self.build_cd = max(0.0, self.build_cd - dt)
        keys = keys if keys is not None else pygame.key.get_pressed()

        self._update_player(dt, keys)
        self._update_enemies(dt)
        self._update_bullets(dt)
        for s in self.scraps:
            s.update(dt)
        for e in self.explosions:
            e.update(dt)
        self.scraps = [s for s in self.scraps if not s.dead]
        self.explosions = [e for e in self.explosions if not e.dead]

        self.spawn_timer -= dt
        if self.spawn_timer <= 0:
            self.spawn_timer = ENEMY_SPAWN_DELAY
            self._spawn_enemy()

        if not self.field.base_alive:
            self._game_over("base perdida")
        elif not self.queue and not self.enemies:
            self.state = CLEARED
            self.state_timer = 0.0

    def _update_player(self, dt, keys):
        p = self.player
        if p.dead:
            return
        p.shield = max(0.0, p.shield - dt)
        if not self.build_mode:
            direction = None
            for key, d in MOVE_KEYS.items():
                if keys[key]:
                    direction = d
                    break
            if direction is not None:
                on_ice = self.field.is_ice(p.rect)
                p.step(direction, self.field, self.enemies, dt,
                       factor=1.25 if on_ice else 1.0)
                p.slide = 0.18 if on_ice else 0.0
            elif p.slide > 0:
                p.slide -= dt
                p.step(p.direction, self.field, self.enemies, dt, factor=0.7)
        # recoger chatarra
        for s in self.scraps:
            if not s.dead and p.rect.colliderect(s.rect):
                s.dead = True
                self.scrap += s.amount

    def _update_enemies(self, dt):
        others = self.enemies + [self.player]
        target = None
        if self.field.base_tiles:
            bx = (min(t[0] for t in self.field.base_tiles) + 1) * TILE
            by = (min(t[1] for t in self.field.base_tiles) + 1) * TILE
            target = (bx, by)
        if not self.player.dead and random.random() < 0.5:
            target = self.player.rect.center
        for e in self.enemies:
            e.think(dt, self.field, others, target)
            if e.wants_to_fire():
                mx, my = e.muzzle()
                self.bullets.append(
                    Bullet(mx, my, e.direction, e.bullet_speed, "enemy", e.piercing))

    def _update_bullets(self, dt):
        for b in self.bullets:
            if b.dead:
                continue
            b.advance(dt)
            r = b.rect
            if r.right < 0 or r.left > FIELD_PX or r.bottom < 0 or r.top > FIELD_PX:
                b.dead = True
                self.explosions.append(Explosion(
                    max(1, min(FIELD_PX - 1, r.centerx)),
                    max(1, min(FIELD_PX - 1, r.centery))))
                continue
            if self._bullet_vs_terrain(b):
                continue
            if self._bullet_vs_bullets(b):
                continue
            self._bullet_vs_tanks(b)
        self.bullets = [b for b in self.bullets if not b.dead]

    def _bullet_vs_terrain(self, b):
        hit_any = False
        scrap_total = 0
        base_down = False
        for tx, ty in self.field.tiles_in(b.rect):
            blocked, scrap, base = self.field.hit(tx, ty, b.piercing)
            if blocked:
                hit_any = True
                scrap_total += scrap
                base_down = base_down or base
                if scrap:
                    self.scraps.append(Scrap(tx, ty, scrap))
        if hit_any:
            b.dead = True
            r = b.rect
            self.explosions.append(Explosion(r.centerx, r.centery, big=base_down))
            if base_down:
                self.explosions.append(Explosion(r.centerx, r.centery, big=True))
        return hit_any

    def _bullet_vs_bullets(self, b):
        for other in self.bullets:
            if other is b or other.dead or other.owner == b.owner:
                continue
            if b.rect.colliderect(other.rect):
                b.dead = other.dead = True
                self.explosions.append(Explosion(b.rect.centerx, b.rect.centery))
                return True
        return False

    def _bullet_vs_tanks(self, b):
        if b.owner == "player":
            for e in self.enemies:
                if e.dead or not b.rect.colliderect(e.rect):
                    continue
                b.dead = True
                e.hp -= 1
                if e.hp <= 0:
                    e.dead = True
                    self.score += SCORE_BY_KIND[e.kind]
                    self.explosions.append(
                        Explosion(e.rect.centerx, e.rect.centery, big=True))
                else:
                    self.explosions.append(Explosion(b.rect.centerx, b.rect.centery))
                break
            self.enemies = [e for e in self.enemies if not e.dead]
        else:
            p = self.player
            if not p.dead and b.rect.colliderect(p.rect):
                b.dead = True
                if p.shield > 0:
                    self.explosions.append(Explosion(b.rect.centerx, b.rect.centery))
                else:
                    self.explosions.append(
                        Explosion(p.rect.centerx, p.rect.centery, big=True))
                    self._player_died()

    def _player_died(self):
        self.lives -= 1
        # Al morir sueltas la mitad de la chatarra que llevabas encima.
        dropped = self.scrap // 2
        self.scrap -= dropped
        r = self.player.rect
        self._scatter_scrap(r.centerx // TILE, r.centery // TILE, dropped)
        if self.lives < 0:
            self._game_over("sin tanques")
        else:
            self._spawn_player()
            self._say("-%d chatarra" % dropped if dropped else "cuidado")

    def _scatter_scrap(self, tx, ty, amount):
        spots = [(tx + dx, ty + dy) for dx in range(-2, 3) for dy in range(-2, 3)]
        random.shuffle(spots)
        for (sx, sy) in spots:
            if amount <= 0:
                break
            if self.field.can_build(sx, sy):
                self.scraps.append(Scrap(sx, sy, 1))
                amount -= 1

    def _game_over(self, reason):
        self.state = GAME_OVER
        self.state_timer = 0.0
        self._say(reason, 4.0)
        self.build_mode = False

    # --- dibujado ---------------------------------------------------------
    def draw(self):
        s = self.surface
        s.fill(GREY_FRAME)
        pygame.draw.rect(s, BLACK, (*ORIGIN, FIELD_PX, FIELD_PX))
        if self.state == TITLE:
            self._draw_title()
        else:
            self._draw_battlefield()
        self._draw_panel()
        return s

    def _draw_title(self):
        cx = ORIGIN[0] + FIELD_PX // 2
        y = ORIGIN[1] + 26
        pixfont.draw_centered(self.surface, "TANK SCRAP", cx, y, (248, 216, 120))
        pixfont.draw_centered(self.surface, "1990", cx, y + 10, (248, 216, 120))
        self.surface.blit(sprites.base_sprite(), (cx - 8, y + 22))
        lines = [
            "EL MAPA ES MUNICION",
            "",
            "CADA LADRILLO ROTO",
            "DEJA CHATARRA.",
            "RECOGELA Y CONSTRUYE",
            "TU PROPIA FORTALEZA.",
            "",
            "FLECHAS MOVER",
            "ESPACIO DISPARAR",
            "B MODO OBRA",
            "  ESPACIO LADRILLO 1",
            "  SHIFT ACERO 6",
            "  X RECUPERAR",
            "",
            "ENTER PARA EMPEZAR",
        ]
        yy = y + 44
        for line in lines:
            color = (248, 216, 120) if line.endswith("MUNICION") else HUD_DIM
            if line.startswith("ENTER"):
                color = WHITE if (self.frame // 20) % 2 == 0 else HUD_DIM
            pixfont.draw_centered(self.surface, line, cx, yy, color)
            yy += 7

    def _draw_battlefield(self):
        s = self.surface
        self.field.draw_ground(s, ORIGIN)
        scrap_spr = self.field.terrain["scrap"]
        for sc in self.scraps:
            sc.draw(s, ORIGIN, scrap_spr, self.frame)
        for e in self.enemies:
            e.draw(s, ORIGIN, self.frame)
        if not self.player.dead and self.lives >= 0:
            self.player.draw(s, ORIGIN, self.frame)
        for b in self.bullets:
            b.draw(s, ORIGIN)
        self.field.draw_trees(s, ORIGIN)
        for ex in self.explosions:
            ex.draw(s, ORIGIN)
        if self.build_mode:
            self._draw_build_cursor()
        if self.state == CLEARED:
            pixfont.draw_centered(s, "FASE SUPERADA", ORIGIN[0] + FIELD_PX // 2,
                                  ORIGIN[1] + FIELD_PX // 2 - 3, WHITE)
        if self.state == GAME_OVER:
            cx = ORIGIN[0] + FIELD_PX // 2
            pixfont.draw_centered(s, "GAME OVER", cx, ORIGIN[1] + FIELD_PX // 2 - 8,
                                  (248, 96, 96))
            pixfont.draw_centered(s, self.message, cx, ORIGIN[1] + FIELD_PX // 2 + 2,
                                  HUD_DIM)
            pixfont.draw_centered(s, "ENTER", cx, ORIGIN[1] + FIELD_PX // 2 + 12,
                                  HUD_DIM)
        if self.paused:
            pixfont.draw_centered(s, "PAUSA", ORIGIN[0] + FIELD_PX // 2,
                                  ORIGIN[1] + FIELD_PX // 2 - 3, WHITE)

    def _draw_build_cursor(self):
        tx, ty = self.build_cursor
        ok = (self.field.can_build(tx, ty) and self.scrap >= COST_BRICK
              and not self._cursor_blocked_by_tank(tx, ty))
        color = GHOST_OK if ok else GHOST_NO
        rect = (ORIGIN[0] + tx * TILE, ORIGIN[1] + ty * TILE, TILE, TILE)
        pygame.draw.rect(self.surface, color, rect, 1)
        if (self.frame // 5) % 2:
            pygame.draw.rect(self.surface, color, (rect[0] + 3, rect[1] + 3, 2, 2))

    def _draw_panel(self):
        s = self.surface
        px = MARGIN_PX + FIELD_PX + 4
        y = MARGIN_PX + 2
        # enemigos pendientes, como iconitos
        pending = len(self.queue) + len(self.enemies)
        pixfont.draw(s, "ENEM", (px, y), HUD_DIM)
        y += 7
        for i in range(min(pending, 20)):
            col = px + (i % 4) * 5
            row = y + (i // 4) * 5
            pygame.draw.rect(s, WHITE, (col, row, 3, 3))
        y += 5 * (min(pending, 20) // 4 + 1) + 4

        pixfont.draw(s, "FASE", (px, y), HUD_DIM)
        pixfont.draw(s, "%d" % (self.stage_index + 1), (px, y + 7), WHITE)
        y += 18
        pixfont.draw(s, "TANQ", (px, y), HUD_DIM)
        pixfont.draw(s, "%d" % max(0, self.lives), (px, y + 7), WHITE)
        y += 18
        pixfont.draw(s, "CHAT", (px, y), (248, 216, 120))
        pixfont.draw(s, "%d" % self.scrap, (px, y + 7), (248, 216, 120))
        y += 18
        pixfont.draw(s, "PUNT", (px, y), HUD_DIM)
        pixfont.draw(s, "%d" % self.score, (px, y + 7), WHITE)
        y += 18
        if self.build_mode:
            blink = (self.frame // 10) % 2 == 0
            pixfont.draw(s, "OBRA", (px, y), GHOST_OK if blink else HUD_DIM)
        if self.message_timer > 0:
            pixfont.draw(s, self.message[:6], (px, MARGIN_PX + FIELD_PX - 8), WHITE)


def run(seed=None, frames=None, headless=False):
    """Arranca el juego. Con frames=N corre N fotogramas sin ventana (autotest)."""
    import os
    if headless:
        os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
        os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
    pygame.init()
    pygame.display.set_caption("TANK SCRAP 1990 - el mapa es municion")
    screen = pygame.display.set_mode((SCREEN_W * SCALE, SCREEN_H * SCALE))
    clock = pygame.time.Clock()
    game = Game(seed=seed)

    if frames:
        game.state = PLAY
        fake_keys = {k: False for k in MOVE_KEYS}
        ticks = 0
        while ticks < frames:
            ticks += 1
            keys = dict(fake_keys)
            keys[pygame.K_RIGHT if ticks % 120 < 60 else pygame.K_UP] = True
            game.update(1.0 / FPS, keys=_KeyProxy(keys))
            if ticks % 37 == 0:
                game._player_fire()
            if ticks % 211 == 0:
                game.build_mode = not game.build_mode
            if game.build_mode and ticks % 23 == 0:
                game._build(fld.BUILT_BRICK, COST_BRICK)
            game.draw()
            if game.state == GAME_OVER:
                game.state = PLAY
                game.lives = 1
                game.field.base_alive = True
        pygame.quit()
        return game

    while not game.quit:
        dt = min(clock.tick(FPS) / 1000.0, 1.0 / 20.0)
        for event in pygame.event.get():
            game.handle_event(event)
        game.update(dt)
        frame = game.draw()
        pygame.transform.scale(frame, screen.get_size(), screen)
        pygame.display.flip()
    pygame.quit()
    return game


class _KeyProxy:
    """Imita pygame.key.get_pressed() para el autotest."""

    def __init__(self, mapping):
        self.mapping = mapping

    def __getitem__(self, key):
        return self.mapping.get(key, False)
