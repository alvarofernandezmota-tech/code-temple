"""Pixel art generado en codigo: cero assets externos.

Todo se dibuja sobre superficies de 8x8 (terreno) o 16x16 (tanques, base) en
pixeles logicos; el escalado final lo hace la ventana.
"""
import pygame

from .constants import (
    BASE_A, BASE_B, BRICK_A, BRICK_B, BRICK_MORTAR, DOWN, ICE_A, ICE_B, LEFT,
    RIGHT, SCRAP_A, SCRAP_B, STEEL_A, STEEL_B, TILE, TREE_A, TREE_B, UP,
    WATER_A, WATER_B,
)

_cache = {}


def _surf(w, h):
    return pygame.Surface((w, h), pygame.SRCALPHA)


# --- Terreno ---------------------------------------------------------------

def brick_tile():
    s = _surf(TILE, TILE)
    s.fill(BRICK_MORTAR)
    for row in range(2):
        y = row * 4
        offset = 0 if row == 0 else 2
        for x in range(-4, TILE, 4):
            pygame.draw.rect(s, BRICK_A, (x + offset, y, 3, 3))
            pygame.draw.rect(s, BRICK_B, (x + offset, y, 3, 1))
    return s


def steel_tile():
    s = _surf(TILE, TILE)
    s.fill(STEEL_A)
    pygame.draw.rect(s, STEEL_B, (0, 0, TILE, 1))
    pygame.draw.rect(s, STEEL_B, (0, 0, 1, TILE))
    pygame.draw.rect(s, STEEL_B, (2, 2, 4, 4), 1)
    return s


def water_tile(frame):
    s = _surf(TILE, TILE)
    s.fill(WATER_A)
    shift = 0 if frame == 0 else 4
    for y in (1, 5):
        pygame.draw.rect(s, WATER_B, ((shift + y) % TILE, y, 3, 1))
        pygame.draw.rect(s, WATER_B, ((shift + y + 4) % TILE, y + 2, 2, 1))
    return s


def tree_tile():
    s = _surf(TILE, TILE)
    s.fill(TREE_A)
    for (x, y) in ((1, 1), (5, 2), (3, 5), (6, 6)):
        pygame.draw.rect(s, TREE_B, (x, y, 2, 2))
    return s


def ice_tile():
    s = _surf(TILE, TILE)
    s.fill(ICE_A)
    pygame.draw.rect(s, ICE_B, (0, 0, 4, 4))
    pygame.draw.rect(s, ICE_B, (4, 4, 4, 4))
    return s


def scrap_tile():
    """Chatarra en el suelo: el recurso que deja cada ladrillo roto."""
    s = _surf(TILE, TILE)
    pygame.draw.rect(s, SCRAP_A, (1, 3, 6, 3))
    pygame.draw.rect(s, SCRAP_B, (2, 2, 4, 2))
    pygame.draw.rect(s, SCRAP_B, (3, 1, 1, 1))
    return s


BASE_MASK = (
    "................",
    ".......22.......",
    "......2112......",
    "......2112......",
    ".11...2112...11.",
    ".1211.2112.1121.",
    ".12211211211221.",
    ".12221111112221.",
    "..122211112221..",
    "...1221111221...",
    "....11122111....",
    ".....211112.....",
    "....21111112....",
    "...1111111111...",
    "..111111111111..",
    "................",
)


def base_sprite(destroyed=False):
    """El aguila, 16x16 (2x2 celdas), dibujada desde una mascara de pixeles."""
    s = _surf(16, 16)
    if destroyed:
        colors = {"1": (72, 72, 72), "2": (120, 120, 120)}
    else:
        colors = {"1": BASE_A, "2": BASE_B}
    for y, row in enumerate(BASE_MASK):
        for x, ch in enumerate(row):
            col = colors.get(ch)
            if col:
                s.set_at((x, y), col)
    if destroyed:
        pygame.draw.line(s, (24, 24, 24), (1, 2), (14, 14), 1)
        pygame.draw.line(s, (24, 24, 24), (14, 2), (1, 14), 1)
    return s


# --- Tanques ---------------------------------------------------------------

def _tank_up(dark, light, shadow, treads):
    """Tanque mirando arriba, 16x16. treads desplaza las orugas (animacion)."""
    s = _surf(16, 16)
    # orugas
    for tx in (0, 12):
        pygame.draw.rect(s, shadow, (tx, 2, 4, 14))
        for y in range(2 + treads % 2, 16, 3):
            pygame.draw.rect(s, light, (tx + 1, y, 2, 1))
    # casco
    pygame.draw.rect(s, dark, (4, 4, 8, 11))
    pygame.draw.rect(s, shadow, (4, 4, 8, 11), 1)
    # torreta
    pygame.draw.rect(s, light, (5, 6, 6, 7))
    pygame.draw.rect(s, shadow, (7, 9, 2, 2))
    # canon
    pygame.draw.rect(s, light, (7, 0, 2, 7))
    pygame.draw.rect(s, shadow, (7, 0, 1, 7))
    return s


def tank_sprite(dark, light, shadow, direction, treads=0):
    key = ("tank", dark, light, shadow, direction, treads % 2)
    if key not in _cache:
        base = _tank_up(dark, light, shadow, treads)
        angle = {UP: 0, LEFT: 90, DOWN: 180, RIGHT: 270}[direction]
        _cache[key] = pygame.transform.rotate(base, angle)
    return _cache[key]


def shield_sprite(frame):
    s = _surf(16, 16)
    color = (152, 216, 248) if frame % 2 == 0 else (248, 248, 248)
    pygame.draw.rect(s, color, (0, 0, 16, 16), 1)
    for (x, y) in ((0, 7), (15, 7), (7, 0), (7, 15)):
        pygame.draw.rect(s, color, (x, y, 1, 2))
    return s


def explosion_sprite(step):
    """4 pasos de explosion, del destello al humo."""
    size = (8, 14, 20, 24)[step]
    s = _surf(size, size)
    c = size // 2
    palette = ((248, 248, 216), (248, 184, 72), (216, 96, 32), (96, 96, 96))
    for i, col in enumerate(palette[: step + 1]):
        r = max(1, c - i * 2)
        pygame.draw.circle(s, col, (c, c), r)
    return s


# --- Cache de terreno ------------------------------------------------------

def terrain_surfaces():
    return {
        "brick": brick_tile(),
        "steel": steel_tile(),
        "water0": water_tile(0),
        "water1": water_tile(1),
        "tree": tree_tile(),
        "ice": ice_tile(),
        "scrap": scrap_tile(),
    }
