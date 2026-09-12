"""Tanques, balas, chatarra y explosiones."""
import random

import pygame

from . import sprites
from .constants import (
    BOSS_PX, BULLET_PX, MULTI_BARREL_PENALTY, PLAYER_FIRE_INTERVAL, DIR_VECTORS, DOWN, ENEMY_COLORS, ENEMY_FIRE_MAX, ENEMY_FIRE_MIN,
    ENEMY_HUNT_CHANCE, ENEMY_TURN_CHANCE, FIELD_PX, LEFT, PLAYER_A, PLAYER_B,
    PLAYER_BULLET_SPEED, PLAYER_C, PLAYER_MAX_BULLETS, PLAYER_SPEED, RIGHT,
    SCRAP_LIFETIME, TANK_PX, TILE, UP,
)

ENEMY_STATS = {
    # tipo:   (velocidad, vel. bala, vida, perfora acero)
    "basic": (0.55, 1.9, 1, False),
    "fast":  (1.05, 2.0, 1, False),
    "power": (0.62, 3.0, 1, True),
    "armor": (0.58, 2.0, 4, False),
}


class Tank:
    def __init__(self, x, y, direction=UP):
        self.size = TANK_PX
        self.x = float(x)
        self.y = float(y)
        self.direction = direction
        self.speed = PLAYER_SPEED
        self.bullet_speed = PLAYER_BULLET_SPEED
        self.hp = 1
        self.piercing = False
        self.treads = 0
        self.chassis = "basic"
        self._tread_acc = 0.0
        self.dead = False
        self.slide = 0.0

    @property
    def rect(self):
        return pygame.Rect(int(self.x), int(self.y), self.size, self.size)

    def muzzle(self):
        r = self.rect
        dx, dy = DIR_VECTORS[self.direction]
        return (r.centerx + dx * (self.size // 2), r.centery + dy * (self.size // 2))

    def _free(self, rect, field, others):
        if rect.left < 0 or rect.top < 0 or rect.right > FIELD_PX or rect.bottom > FIELD_PX:
            return False
        if field.blocks_tank_rect(rect):
            return False
        for other in others:
            if other is not self and not other.dead and other.rect.colliderect(rect):
                return False
        return True

    def face(self, direction):
        if direction == self.direction:
            return
        self.direction = direction
        # Ajuste al medio subtile, como el original: facilita colarse por huecos.
        if direction in (UP, DOWN):
            self.x = round(self.x / 4.0) * 4
        else:
            self.y = round(self.y / 4.0) * 4

    def step(self, direction, field, others, dt, factor=1.0):
        self.face(direction)
        dx, dy = DIR_VECTORS[direction]
        dist = self.speed * factor * dt * 60.0
        moved = False
        for _ in range(2):                      # dos medios pasos: menos tuneles
            half = dist / 2.0
            nxt = pygame.Rect(int(self.x + dx * half), int(self.y + dy * half),
                              self.size, self.size)
            if self._free(nxt, field, others):
                self.x += dx * half
                self.y += dy * half
                moved = True
        if moved:
            self._tread_acc += dist
            if self._tread_acc >= 3.0:
                self._tread_acc = 0.0
                self.treads += 1
        return moved

    def draw(self, surf, origin, colors):
        spr = sprites.tank_sprite(self.chassis, colors, self.direction, self.treads)
        surf.blit(spr, (origin[0] + int(self.x), origin[1] + int(self.y)))


class PlayerTank(Tank):
    """El tanque del jugador. Los atributos que las mejoras de ARENA tocan
    viven aqui, con los valores base del modo campana."""

    def __init__(self, x, y):
        super().__init__(x, y, UP)
        self.chassis = "player"
        self.speed = PLAYER_SPEED
        self.shield = 0.0
        self.max_bullets = PLAYER_MAX_BULLETS
        self.max_hp = 1
        self.hp = 1
        self.fire_interval = PLAYER_FIRE_INTERVAL
        self.fire_cd = 0.0
        self.pierce_brick = False
        self.pierce_steel = False
        self.bounces = 0
        self.magnet = 0
        self.scrap_bonus = 0
        self.supply = 0
        self.hurt_flash = 0.0

    def reload_time(self):
        """Recarga real: la base mas un 15% por cada canon extra."""
        return self.fire_interval * (1 + MULTI_BARREL_PENALTY * (self.max_bullets - 1))

    def carry_over(self, other):
        """Copia el estado que sobrevive de una sala a la siguiente."""
        for attr in ("speed", "max_bullets", "max_hp", "hp", "fire_interval",
                     "bullet_speed", "pierce_brick", "pierce_steel", "bounces",
                     "magnet", "scrap_bonus", "supply", "chassis"):
            setattr(self, attr, getattr(other, attr))

    def draw(self, surf, origin, frame=0):
        super().draw(surf, origin, (PLAYER_A, PLAYER_B, PLAYER_C))
        if self.shield > 0:
            surf.blit(sprites.shield_sprite(frame // 3),
                      (origin[0] + int(self.x), origin[1] + int(self.y)))


class EnemyTank(Tank):
    def __init__(self, x, y, kind):
        super().__init__(x, y, DOWN)
        speed, bullet_speed, hp, piercing = ENEMY_STATS[kind]
        self.kind = kind
        self.chassis = kind
        self.speed = speed
        self.bullet_speed = bullet_speed
        self.hp = hp
        self.max_hp = hp
        self.piercing = piercing
        self.fire_timer = random.uniform(ENEMY_FIRE_MIN, ENEMY_FIRE_MAX)
        self.blocked_for = 0.0

    def think(self, dt, field, others, target_pos):
        """IA sencilla: rumbo aleatorio con sesgo hacia el objetivo."""
        if random.random() < ENEMY_TURN_CHANCE or self.blocked_for > 0.25:
            self.direction = self._pick_direction(target_pos)
            self.blocked_for = 0.0
        if not self.step(self.direction, field, others, dt):
            self.blocked_for += dt
        self.fire_timer -= dt

    def _pick_direction(self, target_pos):
        if random.random() < ENEMY_HUNT_CHANCE and target_pos:
            r = self.rect
            dx = target_pos[0] - r.centerx
            dy = target_pos[1] - r.centery
            if abs(dx) > abs(dy):
                return RIGHT if dx > 0 else LEFT
            return DOWN if dy > 0 else UP
        return random.choice((UP, RIGHT, DOWN, LEFT))

    def wants_to_fire(self):
        if self.fire_timer > 0:
            return False
        self.fire_timer = random.uniform(ENEMY_FIRE_MIN, ENEMY_FIRE_MAX)
        return True

    def draw(self, surf, origin, frame=0):
        dark, light, shadow = ENEMY_COLORS[self.kind]
        if self.kind == "armor" and self.hp < self.max_hp:
            # el blindado va cambiando de tono segun el dano recibido
            t = (self.max_hp - self.hp) / float(self.max_hp)
            dark = tuple(int(c + (232 - c) * t * 0.6) for c in dark)
        super().draw(surf, origin, (dark, light, shadow))


class BossTank(EnemyTank):
    """El jefe de las salas de jefe: 32x32, lento, con dos canones.

    Hereda la IA del blindado pero dispara en pareja y no se deja empujar por
    la cadencia: lo que le sobra es vida.
    """

    def __init__(self, x, y, hp):
        super().__init__(x, y, "armor")
        self.kind = "boss"
        self.chassis = "boss"
        self.size = BOSS_PX
        self.hp = hp
        self.max_hp = hp
        self.speed = 0.42
        self.bullet_speed = 2.2
        self.piercing = True              # sus balas se comen el acero
        self.fire_timer = 1.2

    def muzzles(self):
        """Las dos bocas del jefe, separadas del centro."""
        r = self.rect
        dx, dy = DIR_VECTORS[self.direction]
        half = self.size // 2
        # perpendicular a la direccion, para separar los dos canones
        px, py = (1, 0) if dx == 0 else (0, 1)
        out = []
        for off in (-6, 6):
            out.append((r.centerx + dx * half + px * off,
                        r.centery + dy * half + py * off))
        return out

    def draw(self, surf, origin, frame=0):
        spr = sprites.boss_sprite(self.direction, self.treads)
        if self.hurt_blink(frame):
            spr = spr.copy()
            spr.fill((255, 255, 255, 90), special_flags=pygame.BLEND_RGBA_ADD)
        surf.blit(spr, (origin[0] + int(self.x), origin[1] + int(self.y)))

    def hurt_blink(self, frame):
        """Parpadea cuando esta por debajo de un tercio de vida."""
        return self.hp <= self.max_hp // 3 and (frame // 4) % 2 == 0


class Bullet:
    def __init__(self, x, y, direction, speed, owner, piercing=False,
                 pierce_brick=False, bounces=0):
        self.x = float(x) - BULLET_PX / 2
        self.y = float(y) - BULLET_PX / 2
        self.direction = direction
        self.speed = speed
        self.owner = owner               # "player" o "enemy"
        self.piercing = piercing        # atraviesa acero (tanque rojo)
        self.pierce_brick = pierce_brick  # atraviesa ladrillo (mejora)
        self.bounces = bounces            # rebotes que le quedan (mejora)
        self.dead = False

    @property
    def rect(self):
        return pygame.Rect(int(self.x), int(self.y), BULLET_PX, BULLET_PX)

    def bounce(self):
        """Rebota 180 grados y gasta un rebote."""
        self.direction = (self.direction + 2) % 4
        self.bounces -= 1

    def advance(self, dt):
        dx, dy = DIR_VECTORS[self.direction]
        step = self.speed * dt * 60.0
        self.x += dx * step
        self.y += dy * step

    def draw(self, surf, origin):
        r = self.rect
        pygame.draw.rect(surf, (248, 248, 216),
                         (origin[0] + r.x, origin[1] + r.y, r.w, r.h))


class Scrap:
    """Chatarra en el suelo. Se recoge pisandola; se oxida con el tiempo."""

    def __init__(self, tx, ty, amount=1):
        self.tx = tx
        self.ty = ty
        self.amount = amount
        self.life = SCRAP_LIFETIME
        self.dead = False

    @property
    def rect(self):
        return pygame.Rect(self.tx * TILE, self.ty * TILE, TILE, TILE)

    def update(self, dt):
        self.life -= dt
        if self.life <= 0:
            self.dead = True

    def draw(self, surf, origin, sprite, frame):
        if self.life < 3.0 and (frame // 4) % 2 == 0:
            return                        # parpadea antes de desaparecer
        surf.blit(sprite, (origin[0] + self.tx * TILE, origin[1] + self.ty * TILE))


class Explosion:
    """Explosion de 2 o 4 pasos. El sonido lo lanza quien la crea."""

    def __init__(self, cx, cy, big=False):
        self.cx = cx
        self.cy = cy
        self.steps = 4 if big else 2
        self.step = 0
        self.timer = 0.0
        self.dead = False

    def update(self, dt):
        self.timer += dt
        if self.timer >= 0.06:
            self.timer = 0.0
            self.step += 1
            if self.step >= self.steps:
                self.dead = True

    def draw(self, surf, origin):
        spr = sprites.explosion_sprite(min(self.step, 3))
        surf.blit(spr, (origin[0] + self.cx - spr.get_width() // 2,
                        origin[1] + self.cy - spr.get_height() // 2))
