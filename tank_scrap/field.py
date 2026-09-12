"""El campo de batalla: rejilla de subtiles, destruccion y construccion."""
import pygame

from .constants import FIELD_TILES, SCRAP_PER_BRICK, TILE
from . import sprites

EMPTY = "."
BRICK = "B"
STEEL = "S"
WATER = "W"
TREE = "T"
ICE = "I"
BUILT_BRICK = "b"        # ladrillo puesto por el jugador con chatarra
BUILT_STEEL = "s"        # acero puesto por el jugador con chatarra
BASE = "A"

CELL_TO_TILE = {
    ".": EMPTY, "#": BRICK, "@": STEEL, "~": WATER, "x": TREE, "-": ICE,
    "A": BASE,
}

BLOCKS_TANK = frozenset((BRICK, STEEL, WATER, BUILT_BRICK, BUILT_STEEL, BASE))
BLOCKS_BULLET = frozenset((BRICK, STEEL, BUILT_BRICK, BUILT_STEEL, BASE))
BREAKABLE = frozenset((BRICK, BUILT_BRICK))
BUILDABLE_OVER = frozenset((EMPTY, ICE))


class Field:
    def __init__(self, cell_rows):
        self.grid = [[EMPTY] * FIELD_TILES for _ in range(FIELD_TILES)]
        self.base_tiles = []
        for cy, row in enumerate(cell_rows):
            for cx, ch in enumerate(row):
                kind = CELL_TO_TILE.get(ch, EMPTY)
                for dy in range(2):
                    for dx in range(2):
                        tx, ty = cx * 2 + dx, cy * 2 + dy
                        self.grid[ty][tx] = kind
                        if kind == BASE:
                            self.base_tiles.append((tx, ty))
        self.base_alive = True
        self.terrain = sprites.terrain_surfaces()
        self._water_frame = 0
        self._water_timer = 0.0

    # --- consultas ---------------------------------------------------------
    def inside(self, tx, ty):
        return 0 <= tx < FIELD_TILES and 0 <= ty < FIELD_TILES

    def at(self, tx, ty):
        if not self.inside(tx, ty):
            return STEEL                      # el borde del campo es solido
        return self.grid[ty][tx]

    def blocks_tank_rect(self, rect):
        for tx, ty in self.tiles_in(rect):
            if self.at(tx, ty) in BLOCKS_TANK:
                return True
        return False

    def tiles_in(self, rect):
        x0, y0 = rect.left // TILE, rect.top // TILE
        x1, y1 = (rect.right - 1) // TILE, (rect.bottom - 1) // TILE
        for ty in range(y0, y1 + 1):
            for tx in range(x0, x1 + 1):
                yield tx, ty

    def is_ice(self, rect):
        cx, cy = rect.centerx // TILE, rect.centery // TILE
        return self.at(cx, cy) == ICE

    # --- destruccion -------------------------------------------------------
    def hit(self, tx, ty, piercing=False):
        """Impacto de bala en un subtile.

        Devuelve (bloqueada, chatarra_generada, base_destruida).
        """
        if not self.inside(tx, ty):
            return True, 0, False         # el borde para la bala
        kind = self.at(tx, ty)
        if kind in BREAKABLE:
            self.grid[ty][tx] = EMPTY
            return True, SCRAP_PER_BRICK, False
        if kind == STEEL or kind == BUILT_STEEL:
            if piercing:
                self.grid[ty][tx] = EMPTY
                return True, 0, False
            return True, 0, False
        if kind == BASE:
            if self.base_alive:
                self.base_alive = False
            return True, 0, True
        return False, 0, False

    def clear_around_base(self, kind=EMPTY):
        """Deja limpio el anillo que rodea al aguila (para reconstruirlo)."""
        tiles = set(self.base_tiles)
        ring = set()
        for tx, ty in tiles:
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    p = (tx + dx, ty + dy)
                    if p not in tiles and self.inside(*p):
                        ring.add(p)
        for tx, ty in ring:
            if self.at(tx, ty) in BREAKABLE or self.at(tx, ty) in BUILDABLE_OVER:
                self.grid[ty][tx] = kind
        return ring

    def clear_rect(self, rect):
        """Vacia el ladrillo de un rectangulo (lo usa el jefe al entrar)."""
        cleared = 0
        for tx, ty in self.tiles_in(rect):
            if self.at(tx, ty) in BREAKABLE:
                self.grid[ty][tx] = EMPTY
                cleared += 1
        return cleared

    # --- construccion (la vuelta de tuerca) --------------------------------
    def can_build(self, tx, ty):
        return self.inside(tx, ty) and self.at(tx, ty) in BUILDABLE_OVER

    def build(self, tx, ty, kind):
        if not self.can_build(tx, ty):
            return False
        self.grid[ty][tx] = kind
        return True

    def demolish(self, tx, ty):
        """Retira un muro propio y devuelve la chatarra que costo, o 0."""
        kind = self.at(tx, ty)
        if kind == BUILT_BRICK:
            self.grid[ty][tx] = EMPTY
            return 1
        if kind == BUILT_STEEL:
            self.grid[ty][tx] = EMPTY
            return 6
        return 0

    # --- dibujado ----------------------------------------------------------
    def update(self, dt):
        self._water_timer += dt
        if self._water_timer >= 0.35:
            self._water_timer = 0.0
            self._water_frame ^= 1

    def draw_ground(self, surf, origin):
        """Terreno bajo los tanques (todo menos los arboles)."""
        ox, oy = origin
        water = self.terrain["water0" if self._water_frame == 0 else "water1"]
        for ty in range(FIELD_TILES):
            row = self.grid[ty]
            for tx in range(FIELD_TILES):
                kind = row[tx]
                if kind == EMPTY or kind == TREE:
                    continue
                pos = (ox + tx * TILE, oy + ty * TILE)
                if kind == BRICK:
                    surf.blit(self.terrain["brick"], pos)
                elif kind == BUILT_BRICK:
                    surf.blit(self.terrain["brick"], pos)
                    pygame.draw.rect(surf, (248, 232, 160), (*pos, TILE, TILE), 1)
                elif kind == STEEL:
                    surf.blit(self.terrain["steel"], pos)
                elif kind == BUILT_STEEL:
                    surf.blit(self.terrain["steel"], pos)
                    pygame.draw.rect(surf, (248, 232, 160), (*pos, TILE, TILE), 1)
                elif kind == WATER:
                    surf.blit(water, pos)
                elif kind == ICE:
                    surf.blit(self.terrain["ice"], pos)
        if self.base_tiles:
            bx = min(t[0] for t in self.base_tiles) * TILE + ox
            by = min(t[1] for t in self.base_tiles) * TILE + oy
            surf.blit(sprites.base_sprite(not self.base_alive), (bx, by))

    def draw_trees(self, surf, origin):
        """Los arboles tapan a los tanques: se pintan encima."""
        ox, oy = origin
        tree = self.terrain["tree"]
        for ty in range(FIELD_TILES):
            for tx in range(FIELD_TILES):
                if self.grid[ty][tx] == TREE:
                    surf.blit(tree, (ox + tx * TILE, oy + ty * TILE))
