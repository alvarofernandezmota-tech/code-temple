"""Punto de entrada para la version web (pygbag) y tambien nativo.

pygbag exige un bucle asincrono: el navegador necesita devolver el control
entre fotogramas, asi que hay un `await asyncio.sleep(0)` por vuelta. El mismo
archivo funciona en el escritorio con `python3 main.py`.

Para jugar en el escritorio es mas comodo `./jugar.sh` (que usa el modulo);
este archivo existe sobre todo para compilar a web:

    pygbag --build main.py        # deja la web en build/web/
    scripts/servir_web.sh         # la construye y la sirve en la red local

La variable de entorno TANK_SCRAP_FRAMES sale sola tras N fotogramas, para
poder probar este bucle sin ventana.
"""
import asyncio
import os

import pygame

from tank_scrap import audio
from tank_scrap.constants import FPS, SCALE, SCREEN_H, SCREEN_W
from tank_scrap.game import Game


async def main():
    pygame.init()
    pygame.display.set_caption("TANK SCRAP 1990 - el mapa es municion")
    screen = pygame.display.set_mode((SCREEN_W * SCALE, SCREEN_H * SCALE))
    clock = pygame.time.Clock()

    # En el navegador el sonido puede no estar disponible hasta que el usuario
    # toca la pagina; Sfx se queda mudo solo si falla, sin romper el juego.
    game = Game(sfx=audio.Sfx())

    limit = int(os.environ.get("TANK_SCRAP_FRAMES", "0"))
    frames = 0
    while not game.quit:
        dt = min(clock.tick(FPS) / 1000.0, 1.0 / 20.0)
        for event in pygame.event.get():
            game.handle_event(event)
        game.update(dt)
        pygame.transform.scale(game.draw(), screen.get_size(), screen)
        pygame.display.flip()
        frames += 1
        if limit and frames >= limit:
            break
        await asyncio.sleep(0)       # el navegador respira aqui
    pygame.quit()


asyncio.run(main())
