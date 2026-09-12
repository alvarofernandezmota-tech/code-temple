"""Pruebas de humo: se ejecutan sin ventana (SDL dummy)."""
import os

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

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
