"""Pruebas de humo: se ejecutan sin ventana (SDL dummy)."""
import os
import tempfile

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
# el record no debe tocar el HOME real durante los tests
os.environ["XDG_DATA_HOME"] = tempfile.mkdtemp(prefix="tank-scrap-test-")

import pygame  # noqa: E402

from tank_scrap import field as fld  # noqa: E402
from tank_scrap import levels  # noqa: E402
from tank_scrap.constants import COST_BRICK, COST_STEEL, FPS, TILE  # noqa: E402
from tank_scrap.entities import Bullet, Scrap  # noqa: E402
from tank_scrap.game import PLAY, Game, _KeyProxy  # noqa: E402

pygame.init()
pygame.display.set_mode((64, 64))


def free_tile(g, skip=()):
    """Primer subtile donde se puede construir (evitando los ya usados)."""
    for y in range(25, 0, -1):
        for x in range(26):
            if (x, y) not in skip and g.field.can_build(x, y):
                return x, y
    raise AssertionError("no hay hueco donde construir")


def new_game():
    g = Game(seed=1)
    g.state = PLAY
    return g


def test_record_va_y_vuelve(tmp_path, monkeypatch):
    from tank_scrap import storage
    monkeypatch.setattr(storage, "APP_DIR", str(tmp_path))
    monkeypatch.setattr(storage, "HISCORE_FILE", str(tmp_path / "hiscore.json"))
    assert storage.load_hiscore() == 0
    assert storage.save_hiscore(4200)
    assert storage.load_hiscore() == 4200


def test_fin_de_fase_pasa_por_el_recuento():
    g = new_game()
    g.queue = []
    g.enemies = []
    for _ in range(int(2.0 * FPS)):
        g.update(1.0 / FPS)
        if g.state == "tally":
            break
    assert g.state == "tally"
    g.state_timer = 99.0
    g.update(1.0 / FPS)
    assert g.state == "intro"
    assert g.stage_index == 1


def test_stages_bien_formados():
    for i in range(levels.stage_count()):
        rows = levels.stage(i)
        assert len(rows) == 13
        assert all(len(r) == 13 for r in rows)
        assert sum(r.count("A") for r in rows) == 1


def test_romper_ladrillo_da_chatarra():
    g = new_game()
    tx, ty = next((x, y) for y in range(26) for x in range(26)
                  if g.field.at(x, y) == fld.BRICK)
    blocked, scrap, base = g.field.hit(tx, ty)
    assert blocked and scrap == 1 and not base
    assert g.field.at(tx, ty) == fld.EMPTY


def test_construir_gasta_chatarra_y_recuperar_devuelve():
    g = new_game()
    g.scrap = 10
    g.build_mode = True
    tx, ty = free_tile(g)
    g.build_cursor = [tx, ty]
    g._build(fld.BUILT_BRICK, COST_BRICK)
    assert g.field.at(tx, ty) == fld.BUILT_BRICK
    assert g.scrap == 10 - COST_BRICK
    g.build_cd = 0.0
    g._demolish()
    assert g.field.at(tx, ty) == fld.EMPTY
    assert g.scrap == 10


def test_no_se_construye_sin_chatarra():
    g = new_game()
    g.scrap = 0
    tx, ty = free_tile(g)
    g.build_cursor = [tx, ty]
    g._build(fld.BUILT_BRICK, COST_BRICK)
    assert g.field.at(tx, ty) == fld.EMPTY


def test_acero_propio_aguanta_bala_normal():
    g = new_game()
    g.scrap = COST_STEEL
    tx, ty = free_tile(g)
    g.build_cursor = [tx, ty]
    g._build(fld.BUILT_STEEL, COST_STEEL)
    assert g.field.at(tx, ty) == fld.BUILT_STEEL
    blocked, scrap, _ = g.field.hit(tx, ty, piercing=False)
    assert blocked and scrap == 0
    assert g.field.at(tx, ty) == fld.BUILT_STEEL
    blocked, _, _ = g.field.hit(tx, ty, piercing=True)
    assert blocked and g.field.at(tx, ty) == fld.EMPTY


def test_recoger_chatarra_al_pisarla():
    g = new_game()
    g.scrap = 0
    r = g.player.rect
    g.scraps.append(Scrap(r.centerx // TILE, r.centery // TILE, 3))
    g._update_player(1.0 / FPS, _KeyProxy({}))
    assert g.scrap == 3
    assert all(s.dead for s in g.scraps)


def test_base_destruida_termina_la_partida():
    g = new_game()
    tx, ty = g.field.base_tiles[0]
    g.bullets.append(Bullet(tx * TILE + 4, ty * TILE + 4, 2, 1.0, "enemy"))
    for _ in range(5):
        g.update(1.0 / FPS)
    assert not g.field.base_alive
    assert g.state == "over"


def test_partida_larga_no_revienta():
    g = new_game()
    for t in range(1200):
        keys = _KeyProxy({pygame.K_RIGHT: t % 80 < 40, pygame.K_UP: t % 80 >= 40})
        g.update(1.0 / FPS, keys=keys)
        if t % 30 == 0:
            g._player_fire()
        g.draw()
        if g.state == "over":
            break
    assert g.frame >= 1


# --- Modo ARENA -------------------------------------------------------------

def arena_game():
    g = Game(seed=2)
    g.mode = "arena"
    g._load_stage(0, reset_run=True)
    g.state = PLAY
    return g


def test_salas_bien_formadas_y_sin_aguila():
    from tank_scrap import arena
    rng = __import__("random").Random(7)
    for i in range(12):
        rows = arena.generate_room(i, rng)
        assert len(rows) == 13 and all(len(r) == 13 for r in rows)
        assert all("A" not in r for r in rows)      # en arena no hay aguila
        assert rows[11][6] == "." and rows[12][6] == "."   # sitio donde apareces
        for (cx, cy) in ((0, 0), (6, 0), (12, 0)):
            assert rows[cy][cx] == "."              # bocas de aparicion libres


def test_arena_tiene_vida_y_no_vidas():
    g = arena_game()
    assert g.player.max_hp == 4 and g.player.hp == 4
    assert g.lives == 0


def test_impacto_quita_vida_no_mata():
    g = arena_game()
    g.player.shield = 0.0
    r = g.player.rect
    g.bullets.append(Bullet(r.centerx, r.centery, 0, 0.1, "enemy"))
    g.update(1.0 / FPS)
    assert g.player.hp == 3
    assert g.state == PLAY


def test_disparo_automatico_solo_al_estar_quieto():
    g = arena_game()
    g.player.fire_cd = 0.0
    g._update_player(1.0 / FPS, _KeyProxy({pygame.K_RIGHT: True}))
    assert not [b for b in g.bullets if b.owner == "player"]
    g.player.fire_cd = 0.0
    g._update_player(1.0 / FPS, _KeyProxy({}))
    assert len([b for b in g.bullets if b.owner == "player"]) == 1


def test_el_keydown_de_espacio_no_dispara_en_arena():
    """En arena el disparo se lee cada fotograma, no en el evento de tecla."""
    g = arena_game()
    g._handle_play_key(pygame.K_SPACE)
    assert not g.bullets


def test_espacio_dispara_en_marcha_pero_recarga_mas_lenta():
    from tank_scrap.constants import ARENA_MOVING_FIRE_PENALTY
    g = arena_game()
    g.player.fire_cd = 0.0
    g._update_player(1.0 / FPS, _KeyProxy({pygame.K_RIGHT: True,
                                           pygame.K_SPACE: True}))
    disparos = [b for b in g.bullets if b.owner == "player"]
    assert len(disparos) == 1
    esperado = g.player.fire_interval * ARENA_MOVING_FIRE_PENALTY
    assert abs(g.player.fire_cd - esperado) < 1e-6

    # parado, la misma tecla recarga a cadencia normal
    g2 = arena_game()
    g2.player.fire_cd = 0.0
    g2._update_player(1.0 / FPS, _KeyProxy({pygame.K_SPACE: True}))
    assert abs(g2.player.fire_cd - g2.player.fire_interval) < 1e-6


def test_en_modo_obra_el_espacio_construye_y_no_dispara():
    g = arena_game()
    g.build_mode = True
    g.player.fire_cd = 0.0
    g._update_player(1.0 / FPS, _KeyProxy({pygame.K_SPACE: True}))
    assert not [b for b in g.bullets if b.owner == "player"]


def test_mejora_se_aplica_y_se_apunta():
    from tank_scrap import arena
    g = arena_game()
    g.offer = [arena.BY_ID["canon"]]
    antes = g.player.max_bullets
    g._choose_upgrade(0)
    assert g.player.max_bullets == antes + 1
    assert g.taken["canon"] == 1
    assert g.stage_index == 1          # elegir mejora pasa a la sala siguiente


def test_las_mejoras_sobreviven_a_la_sala_siguiente():
    from tank_scrap import arena
    g = arena_game()
    g.offer = [arena.BY_ID["orugas"]]
    g._choose_upgrade(0)
    veloz = g.player.speed
    g.offer = [arena.BY_ID["orugas"]]
    g._choose_upgrade(0)
    assert g.player.speed > veloz


def test_reroll_cuesta_chatarra_y_no_va_sin_ella():
    from tank_scrap import arena
    g = arena_game()
    g.scrap = arena.REROLL_COST
    g.offer = arena.offer(g.taken, g.rng)
    g._reroll_offer()
    assert g.scrap == 0 and len(g.offer) == 3
    antes = list(g.offer)
    g._reroll_offer()                  # ya no hay chatarra: la oferta no cambia
    assert g.offer == antes


def test_la_chatarra_sobrante_se_funde_en_puntos():
    from tank_scrap import arena
    g = arena_game()
    g.scrap = 7
    g.score = 100
    g.player.hp = 1
    g.player.shield = 0.0
    g._player_died()
    assert g.state == "over"
    assert g.melted == 7 * arena.SCRAP_TO_SCORE
    assert g.score == 100 + g.melted and g.scrap == 0


def test_bala_perforante_atraviesa_el_ladrillo():
    g = arena_game()
    g.player.pierce_brick = True
    tx, ty = next((x, y) for y in range(26) for x in range(26)
                  if g.field.at(x, y) == fld.BRICK)
    b = Bullet(tx * TILE + 4, ty * TILE + 4, 2, 0.1, "player", pierce_brick=True)
    g.bullets.append(b)
    g._bullet_vs_terrain(b)
    assert g.field.at(tx, ty) == fld.EMPTY
    assert not b.dead                  # sigue su camino


def test_bala_con_rebote_cambia_de_sentido():
    b = Bullet(40, 40, 2, 0.1, "player", bounces=1)
    b.bounce()
    assert b.direction == 0 and b.bounces == 0
