#!/usr/bin/env python3
"""Mide el balance del juego con el propio codigo, sin abrir ventana.

No opina: cuenta chatarra disponible, dano por segundo, vida de las oleadas,
cuanto tarda en caer un jefe y que recoge de verdad un bot que no busca
chatarra. Cualquier cambio de numeros en constants.py se comprueba aqui.

    SDL_VIDEODRIVER=dummy python3 scripts/medir_balance.py
"""
import os
import random
import sys

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pygame  # noqa: E402

pygame.init()
pygame.display.set_mode((16, 16))

from tank_scrap import arena, levels  # noqa: E402
from tank_scrap import field as fld  # noqa: E402
from tank_scrap.constants import (  # noqa: E402
    COST_BRICK, COST_STEEL, FPS, MULTI_BARREL_PENALTY, PLAYER_FIRE_INTERVAL,
    SCRAP_CAP, SCRAP_START,
)
from tank_scrap.entities import ENEMY_STATS  # noqa: E402
from tank_scrap.game import ARENA, OFFER, PLAY, Game, _KeyProxy  # noqa: E402

BAR = "=" * 68


def bricks_in(field):
    return sum(row.count(fld.BRICK) for row in field.grid)


def dps(bullets, rate_stacks):
    """Impactos por segundo con N canones y N escalones de cadencia."""
    interval = PLAYER_FIRE_INTERVAL * (0.78 ** rate_stacks)
    interval *= 1 + MULTI_BARREL_PENALTY * (bullets - 1)
    interval = max(0.12, interval)
    return bullets / interval, interval


def chatarra_disponible():
    print(BAR)
    print("CHATARRA DISPONIBLE EN EL MAPA (1 por subtile de ladrillo)")
    for i in range(3):
        n = bricks_in(fld.Field(levels.stage(i)))
        print("  campana fase %d: %3d" % (i + 1, n))
    rng = random.Random(1)
    salas = [bricks_in(fld.Field(arena.generate_room(i, rng))) for i in range(10)]
    print("  arena salas 1-10: %s" % " ".join("%3d" % n for n in salas))
    print("  media arena: %.0f por sala" % (sum(salas) / len(salas)))
    print("  costes: ladrillo %d, acero %d, reroll %d, techo en mano %d, inicio %d"
          % (COST_BRICK, COST_STEEL, arena.REROLL_COST, SCRAP_CAP, SCRAP_START))
    anillo = len(fld.Field(levels.stage(0)).clear_around_base())
    print("  anillo del aguila: %d subtiles = %d en ladrillo / %d en acero"
          % (anillo, anillo * COST_BRICK, anillo * COST_STEEL))


def dano():
    print(BAR)
    print("DANO DEL JUGADOR (impactos/s) — filas: canones, columnas: cadencia")
    print("          cadencia x0   x1      x2      x3")
    for b in (1, 2, 3, 4):
        fila = ["%6.2f" % dps(b, r)[0] for r in range(4)]
        print("  %d canon  %s" % (b, "  ".join(fila)))
    top = dps(4, 3)
    print("  tope alcanzable: %.2f impactos/s (intervalo %.3f s)" % (top[0], top[1]))
    return top[0]


def oleadas(tope):
    print(BAR)
    print("VIDA DE LA OLEADA vs TIEMPO DE FUEGO PURO")
    base = dps(1, 0)[0]
    medio = dps(2, 2)[0]
    print("  sala  enemigos  vida   base %.1f/s   medio %.1f/s   tope %.1f/s"
          % (base, medio, tope))
    rng = random.Random(7)
    for i in (0, 1, 4, 9, 14, 19, 24):
        roster = arena.room_roster(i, rng)
        bonus = arena.enemy_hp_bonus(i)
        vida = 0
        for k in roster:
            vida += arena.boss_hp(i) if k == "boss" else ENEMY_STATS[k][2] + bonus
        print("   %2d      %2d      %3d     %5.1f s      %5.1f s      %5.1f s"
              % (i + 1, len(roster), vida, vida / base, vida / medio, vida / tope))


def jefes(tope):
    print(BAR)
    print("EL JEFE")
    base, medio = dps(1, 0)[0], dps(2, 2)[0]
    for i in (4, 9, 14, 19, 24):
        hp = arena.boss_hp(i)
        print("  sala %2d: vida %3d -> %5.1f s a dano base, %4.1f s medio, %4.1f s a tope"
              % (i + 1, hp, hp / base, hp / medio, hp / tope))


def runs_de_bot(seeds=(3, 11, 29), segundos=90):
    print(BAR)
    print("BOT (persigue al enemigo y dispara; no va a por la chatarra)")
    for seed in seeds:
        g = Game(seed=seed)
        g.mode = ARENA
        g._load_stage(0, reset_run=True)
        g.state = PLAY
        salas = 0
        for t in range(FPS * segundos):
            if g.state == OFFER:
                g._choose_upgrade(0)
                salas += 1
                continue
            if g.state == "over":
                break
            keys = {}
            if g.enemies and t % 60 < 35:
                e = g.enemies[0]
                r = g.player.rect
                dx = e.rect.centerx - r.centerx
                dy = e.rect.centery - r.centery
                if abs(dx) > abs(dy):
                    keys[pygame.K_RIGHT if dx > 0 else pygame.K_LEFT] = True
                else:
                    keys[pygame.K_DOWN if dy > 0 else pygame.K_UP] = True
            keys[pygame.K_SPACE] = True
            g.update(1.0 / FPS, keys=_KeyProxy(keys))
        print("  seed %2d: salas %d, recogida %2d, perdida por el techo %2d, "
              "en mano %2d, puntos %5d"
              % (seed, salas, g.run_collected, g.run_wasted, g.scrap, g.score))


def main():
    chatarra_disponible()
    tope = dano()
    oleadas(tope)
    jefes(tope)
    runs_de_bot()
    print(BAR)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
