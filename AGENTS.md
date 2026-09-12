# AGENTS.md — reglas de este repo

Repo de un juego: **TANK SCRAP 1990**, tank shooter de pixeles en pygame cuya
vuelta de tuerca es la economia de chatarra (ver README).

## Estructura
- `tank_scrap/constants.py` — toda la afinacion del juego (velocidades, costes,
  paleta). Los numeros magicos van aqui, no repartidos por el codigo.
- `tank_scrap/sprites.py` — pixel art generado en codigo. Sin assets externos:
  si hace falta un grafico nuevo, se dibuja con rects o con mascara ASCII.
- `tank_scrap/field.py` — rejilla de subtiles de 8 px, destruccion y obra.
- `tank_scrap/entities.py` — tanques, balas, chatarra, explosiones.
- `tank_scrap/game.py` — bucle, estados, HUD.
- `tank_scrap/levels.py` — mapas de campaña en celdas de 16 px (13x13).
- `tank_scrap/arena.py` — modo roguelite: salas generadas, oleadas y mejoras.
- `tank_scrap/storage.py` — lo unico que se persiste es el record.

## Antes de commitear
    python3 -m pyflakes tank_scrap/*.py
    python3 -m pytest tests -q
    SDL_VIDEODRIVER=dummy python3 -m tank_scrap --selftest 1800
    SDL_VIDEODRIVER=dummy python3 -m tank_scrap --selftest 1800 --arena

Las tres cosas tienen que pasar. Los tests corren sin ventana (SDL dummy), asi
que valen en CI.

## Convenciones
- Commits: `tipo: descripcion breve en presente`.
- Un mapa nuevo se anade a `levels.STAGES`, siempre 13 filas de 13 caracteres
  y exactamente una `A` (el aguila).
- Una mejora nueva de arena se anade a `arena.UPGRADES` con su funcion
  `_up_*`; los atributos que toca tienen que existir en `PlayerTank` y estar
  listados en `PlayerTank.carry_over`, o se perderan al cambiar de sala.
- Las salas de arena no llevan aguila: nunca metas una `A` en `generate_room`.
- Nada de dependencias nuevas sin una razon buena: pygame y nada mas.
