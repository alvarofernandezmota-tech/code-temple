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

def _tracks(s, dark, light, shadow, treads, width=4, top=2, bottom=16):
    """Orugas laterales; treads desplaza los eslabones para animarlas."""
    for tx in (0, 16 - width):
        pygame.draw.rect(s, shadow, (tx, top, width, bottom - top))
        for y in range(top + treads % 3, bottom, 3):
            pygame.draw.rect(s, light, (tx + 1, y, width - 2, 1))


def _chassis_player(s, dark, light, shadow, treads):
    """Tanque del jugador: casco compacto y una estrella en la torreta."""
    _tracks(s, dark, light, shadow, treads)
    pygame.draw.rect(s, dark, (4, 4, 8, 11))
    pygame.draw.rect(s, shadow, (4, 4, 8, 11), 1)
    pygame.draw.rect(s, light, (5, 6, 6, 7))
    pygame.draw.rect(s, shadow, (7, 8, 2, 2))       # escotilla
    pygame.draw.rect(s, light, (6, 10, 1, 1))
    pygame.draw.rect(s, light, (9, 10, 1, 1))
    pygame.draw.rect(s, light, (7, 0, 2, 7))        # canon
    pygame.draw.rect(s, shadow, (7, 0, 1, 7))


def _chassis_basic(s, dark, light, shadow, treads):
    """Gris: el tanque de infanteria, silueta corta y cuadrada."""
    _tracks(s, dark, light, shadow, treads, top=3)
    pygame.draw.rect(s, dark, (4, 5, 8, 10))
    pygame.draw.rect(s, shadow, (4, 5, 8, 10), 1)
    pygame.draw.rect(s, light, (5, 7, 6, 6))
    pygame.draw.rect(s, shadow, (6, 9, 4, 2))
    pygame.draw.rect(s, light, (7, 1, 2, 6))
    pygame.draw.rect(s, shadow, (7, 1, 1, 6))


def _chassis_fast(s, dark, light, shadow, treads):
    """Azul: orugas finas, morro en punta y canon largo. Se lee veloz."""
    _tracks(s, dark, light, shadow, treads, width=3, top=4)
    pygame.draw.rect(s, dark, (4, 6, 8, 9))
    pygame.draw.rect(s, shadow, (4, 6, 8, 9), 1)
    for i in range(3):                               # morro escalonado
        pygame.draw.rect(s, dark, (5 + i, 5 - i, 6 - i * 2, 1))
    pygame.draw.rect(s, light, (6, 9, 4, 5))
    pygame.draw.rect(s, shadow, (6, 9, 4, 5), 1)
    pygame.draw.rect(s, light, (7, 0, 2, 9))         # canon largo
    pygame.draw.rect(s, shadow, (7, 0, 1, 9))
    pygame.draw.rect(s, light, (5, 14, 6, 1))        # aleta trasera


def _chassis_power(s, dark, light, shadow, treads):
    """Rojo: torreta redonda y canon grueso con freno de boca."""
    _tracks(s, dark, light, shadow, treads)
    pygame.draw.rect(s, dark, (4, 4, 8, 11))
    pygame.draw.rect(s, shadow, (4, 4, 8, 11), 1)
    pygame.draw.circle(s, light, (8, 10), 4)
    pygame.draw.circle(s, shadow, (8, 10), 4, 1)
    pygame.draw.rect(s, light, (6, 1, 4, 8))         # canon grueso
    pygame.draw.rect(s, shadow, (6, 1, 1, 8))
    pygame.draw.rect(s, shadow, (6, 2, 4, 1))        # freno de boca


def _chassis_armor(s, dark, light, shadow, treads):
    """Morado: faldones blindados que sobresalen y remaches. Se lee pesado."""
    _tracks(s, dark, light, shadow, treads, top=3)
    pygame.draw.rect(s, dark, (2, 5, 12, 10))        # faldones
    pygame.draw.rect(s, shadow, (2, 5, 12, 10), 1)
    pygame.draw.rect(s, shadow, (2, 9, 12, 1))       # linea de blindaje
    pygame.draw.rect(s, light, (5, 7, 6, 5))
    pygame.draw.rect(s, shadow, (5, 7, 6, 5), 1)
    for (rx, ry) in ((3, 6), (12, 6), (3, 13), (12, 13)):
        pygame.draw.rect(s, light, (rx, ry, 1, 1))   # remaches
    pygame.draw.rect(s, light, (7, 2, 2, 5))
    pygame.draw.rect(s, shadow, (7, 2, 1, 5))


def _chassis_boss(s, dark, light, shadow, treads):
    """Jefe 32x32: orugas dobles, faldones remachados y dos canones."""
    for tx in (0, 25):
        pygame.draw.rect(s, shadow, (tx, 4, 7, 28))
        for y in range(4 + treads % 3, 32, 4):
            pygame.draw.rect(s, light, (tx + 1, y, 5, 2))
    pygame.draw.rect(s, dark, (5, 8, 22, 22))
    pygame.draw.rect(s, shadow, (5, 8, 22, 22), 1)
    pygame.draw.rect(s, shadow, (5, 18, 22, 1))
    pygame.draw.rect(s, light, (10, 12, 12, 14))
    pygame.draw.rect(s, shadow, (10, 12, 12, 14), 1)
    for (rx, ry) in ((7, 10), (24, 10), (7, 27), (24, 27), (7, 19), (24, 19)):
        pygame.draw.rect(s, light, (rx, ry, 2, 2))
    for bx in (10, 19):                       # dos canones
        pygame.draw.rect(s, light, (bx, 0, 3, 13))
        pygame.draw.rect(s, shadow, (bx, 0, 1, 13))
    pygame.draw.rect(s, shadow, (14, 18, 4, 4))


def boss_sprite(direction, treads=0):
    from .constants import BOSS_PX, ENEMY_COLORS
    dark, light, shadow = ENEMY_COLORS["boss"]
    key = ("boss", direction, treads % 3)
    if key not in _cache:
        s = _surf(BOSS_PX, BOSS_PX)
        _chassis_boss(s, dark, light, shadow, treads)
        angle = {UP: 0, LEFT: 90, DOWN: 180, RIGHT: 270}[direction]
        _cache[key] = pygame.transform.rotate(s, angle)
    return _cache[key]


CHASSIS = {
    "player": _chassis_player,
    "basic": _chassis_basic,
    "fast": _chassis_fast,
    "power": _chassis_power,
    "armor": _chassis_armor,
}


def tank_sprite(chassis, colors, direction, treads=0):
    """Sprite 16x16 del chasis pedido, girado a la direccion dada."""
    dark, light, shadow = colors
    key = ("tank", chassis, dark, light, shadow, direction, treads % 3)
    if key not in _cache:
        s = _surf(16, 16)
        CHASSIS.get(chassis, _chassis_basic)(s, dark, light, shadow, treads)
        angle = {UP: 0, LEFT: 90, DOWN: 180, RIGHT: 270}[direction]
        _cache[key] = pygame.transform.rotate(s, angle)
    return _cache[key]


def mini_tank(color, light=None):
    """Iconito de tanque 6x7 para el marcador (vidas y oleada pendiente)."""
    key = ("mini", color, light)
    if key not in _cache:
        s = _surf(6, 7)
        light = light or color
        pygame.draw.rect(s, color, (0, 1, 2, 6))
        pygame.draw.rect(s, color, (4, 1, 2, 6))
        pygame.draw.rect(s, light, (2, 2, 2, 4))
        pygame.draw.rect(s, light, (2, 0, 2, 2))
        _cache[key] = s
    return _cache[key]


def shield_sprite(frame):
    """Escudo de aparicion: chispas girando alrededor del tanque."""
    s = _surf(16, 16)
    color = (152, 216, 248) if frame % 2 == 0 else (248, 248, 248)
    ring = ((4, 0), (8, 0), (12, 1), (15, 4), (15, 8), (14, 12), (11, 15),
            (7, 15), (3, 14), (0, 11), (0, 7), (1, 3))
    phase = frame % 3
    for i, (x, y) in enumerate(ring):
        if i % 3 == phase:
            continue
        pygame.draw.rect(s, color, (x, y, 1, 1))
    for (x, y) in ((0, 0), (15, 0), (0, 15), (15, 15)):
        pygame.draw.rect(s, color, (x, y, 1, 1))
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
