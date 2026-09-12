"""Modo ARENA: salas encadenadas y mejoras al estilo Archero.

Una *run* es una secuencia de salas cerradas. En cada sala apareces con el
tanque que llevas, la limpias de enemigos y eliges **una de tres mejoras**
antes de pasar a la siguiente. No hay aguila que defender: lo que se pierde
al morir es la run entera.

La chatarra sigue siendo el recurso central y aqui tiene tres destinos:
levantar muro, pagar rerolls de la oferta de mejoras, y lo que sobre al
acabar la run se funde en puntos.
"""
import random

BOSS_EVERY = 5           # cada 5 salas, una de jefe
REROLL_COST = 3
SCRAP_TO_SCORE = 10      # cada chatarra sin gastar valen 10 puntos al final
ROOM_CLEAR_SCORE = 300
BOSS_CLEAR_SCORE = 1200


# --- Generacion de salas ---------------------------------------------------

def is_boss_room(index):
    return (index + 1) % BOSS_EVERY == 0


def generate_room(index, rng=None):
    """Devuelve una sala como 13 filas de 13 caracteres (mismo formato que
    levels.py). El centro y los bordes quedan despejados para poder moverse."""
    rng = rng or random
    grid = [["."] * 13 for _ in range(13)]
    archetype = rng.choice(("pilares", "cruz", "trincheras", "patio", "molino"))

    def put(cx, cy, ch):
        if 0 <= cx < 13 and 0 <= cy < 13:
            grid[cy][cx] = ch

    if archetype == "pilares":
        for cy in range(2, 11, 3):
            for cx in range(2, 11, 3):
                put(cx, cy, "@" if (cx + cy) % 2 == 0 else "#")
                put(cx + 1, cy, "#")
    elif archetype == "cruz":
        for i in range(2, 11):
            put(i, 6, "#")
            put(6, i, "#")
        for d in (-1, 1):
            put(6 + d, 6, ".")
            put(6, 6 + d, ".")
        put(6, 6, "@")
        for (cx, cy) in ((3, 3), (9, 3), (3, 9), (9, 9)):
            put(cx, cy, "@")
    elif archetype == "trincheras":
        for cy in (3, 6, 9):
            for cx in range(1, 12):
                put(cx, cy, "#")
            gap = rng.randrange(2, 10)
            put(gap, cy, ".")
            put(gap + 1, cy, ".")
        put(6, 6, "~")
    elif archetype == "patio":
        for cx in range(3, 10):
            put(cx, 3, "#")
            put(cx, 9, "#")
        for cy in range(3, 10):
            put(3, cy, "#")
            put(9, cy, "#")
        for (cx, cy) in ((6, 3), (6, 9), (3, 6), (9, 6)):
            put(cx, cy, ".")
        put(6, 6, "x")
        put(5, 6, "x")
        put(7, 6, "x")
    else:  # molino
        for i in range(2, 7):
            put(i, 3, "#")
            put(12 - i, 9, "#")
            put(3, 12 - i, "#")
            put(9, i, "#")
        for (cx, cy) in ((2, 2), (10, 10)):
            put(cx, cy, "@")
        put(6, 6, "-")

    # El hielo y el agua se van sumando a medida que avanza la run.
    hazards = min(6, index // 2)
    for _ in range(hazards):
        cx, cy = rng.randrange(1, 12), rng.randrange(1, 12)
        if grid[cy][cx] == ".":
            grid[cy][cx] = rng.choice(("~", "-", "x"))

    # Deja libres el centro-bajo (donde apareces) y las tres bocas de arriba.
    for (cx, cy) in ((6, 11), (6, 12), (5, 12), (7, 12),
                     (0, 0), (6, 0), (12, 0)):
        grid[cy][cx] = "."
    return ["".join(row) for row in grid]


def room_roster(index, rng=None):
    """Enemigos de la sala. Las de jefe traen blindados de escolta."""
    rng = rng or random
    n = index + 1
    if is_boss_room(index):
        # Un jefe y su escolta. La escolta crece, el jefe engorda de vida.
        roster = ["power"] * 2 + ["fast"] * 2 + ["armor"] * (n // BOSS_EVERY)
        rng.shuffle(roster)
        return roster + ["boss"]         # el jefe sale primero (se saca del final)
    else:
        roster = ["basic"] * max(2, 5 - n // 3)
        roster += ["fast"] * min(5, 1 + n // 2)
        roster += ["power"] * min(4, n // 2)
        roster += ["armor"] * min(3, max(0, (n - 2) // 3))
    rng.shuffle(roster)
    return roster


def boss_hp(index, base=None, per_room=None):
    """Vida del jefe segun lo avanzada que este la run."""
    from .constants import BOSS_HP_BASE, BOSS_HP_PER_ROOM
    base = BOSS_HP_BASE if base is None else base
    per_room = BOSS_HP_PER_ROOM if per_room is None else per_room
    return base + per_room * (index // BOSS_EVERY)


# --- Mejoras ---------------------------------------------------------------
# Cada mejora es: id, nombre corto, dos lineas de texto, cuantas veces se
# puede coger, y que le hace al tanque.

def _up_cannon(g):
    g.player.max_bullets += 1


def _up_rate(g):
    g.player.fire_interval = max(0.12, g.player.fire_interval * 0.78)


def _up_speed_bullet(g):
    g.player.bullet_speed += 0.6


def _up_armor(g):
    g.player.max_hp += 1
    g.player.hp = min(g.player.max_hp, g.player.hp + 1)


def _up_tracks(g):
    g.player.speed += 0.12


def _up_pierce(g):
    g.player.pierce_brick = True


def _up_bounce(g):
    g.player.bounces += 1


def _up_salvage(g):
    g.player.scrap_bonus += 1


def _up_magnet(g):
    g.player.magnet += 20


def _up_repair(g):
    g.player.hp = g.player.max_hp


def _up_supply(g):
    g.player.supply += 6


UPGRADES = [
    ("canon", "DOBLE CANON", ("UNA BALA MAS", "EN VUELO"), 3, _up_cannon),
    ("cadencia", "CADENCIA", ("DISPARAS UN", "22% MAS RAPIDO"), 4, _up_rate),
    ("veloz", "BALA VELOZ", ("LA BALA VUELA", "MAS RAPIDO"), 3, _up_speed_bullet),
    ("blindaje", "BLINDAJE", ("+1 DE VIDA", "MAXIMA Y CURA 1"), 4, _up_armor),
    ("orugas", "ORUGAS", ("TE MUEVES", "MAS RAPIDO"), 3, _up_tracks),
    ("perfora", "PERFORANTE", ("TU BALA ATRAVIESA", "EL LADRILLO"), 1, _up_pierce),
    ("rebote", "REBOTE", ("LA BALA REBOTA", "EN EL ACERO"), 2, _up_bounce),
    ("desguace", "DESGUACE", ("CADA LADRILLO", "DA +1 CHATARRA"), 3, _up_salvage),
    ("iman", "IMAN", ("RECOGES CHATARRA", "A DISTANCIA"), 2, _up_magnet),
    ("taller", "TALLER", ("CURA TODA", "LA VIDA"), 99, _up_repair),
    ("suministro", "SUMINISTRO", ("+6 DE CHATARRA", "AL ENTRAR"), 99, _up_supply),
]

BY_ID = {u[0]: u for u in UPGRADES}


def offer(taken, rng=None, count=3):
    """Saca `count` mejoras elegibles, sin repetir dentro de la misma oferta."""
    rng = rng or random
    pool = [u for u in UPGRADES if taken.get(u[0], 0) < u[3]]
    rng.shuffle(pool)
    return pool[:count]
