"""Mapas de las fases, escritos en celdas de 16 px (13x13).

Cada caracter es una celda clasica y se expande a 2x2 subtiles de 8 px, que es
la resolucion real a la que se destruyen y se construyen los muros.

  '.' vacio   '#' ladrillo   '@' acero   '~' agua   'x' arboles
  '-' hielo   'A' aguila (base)
"""

# Progresion pensada, no acumulacion de mapas: 1-2 ensenan la mecanica, 3-4
# meten acero y agua, 5-6 aprietan los caminos hacia el aguila, 7-8 mezclan
# hielo con pasillos estrechos. Todas tienen que dejar libres la casilla de
# aparicion del jugador (4,12) y las tres bocas de arriba (0,0) (6,0) (12,0),
# y llevar exactamente un aguila.
STAGES = [
    # 1 - El patio: mucho ladrillo, o sea, mucha chatarra que robar.
    [
        ".....#.#.....",
        "..#..#.#..#..",
        "..#..#.#..#..",
        "..#.......#..",
        ".###.###.###.",
        ".............",
        "@@..#####..@@",
        ".............",
        ".###.xxx.###.",
        "..#...~...#..",
        "..#..#.#..#..",
        ".....###.....",
        ".....#A#.....",
    ],
    # 2 - Pasillos: poco ladrillo suelto, hay que administrar la chatarra.
    [
        "....#...#....",
        "@#.#.#.#.#.#@",
        ".#.#.....#.#.",
        ".#..@###@..#.",
        "....#...#....",
        "##.#..~..#.##",
        "...#.....#...",
        "xx.#.###.#.xx",
        "...#..#..#...",
        ".@.....#...@.",
        "..###.#.###..",
        "....#####....",
        ".....#A#.....",
    ],
    # 3 - La fortaleza rota: acero por todas partes, el hielo te traiciona.
    [
        "..@.......@..",
        ".---.###.---.",
        "..#..#.#..#..",
        "@.#..#.#..#.@",
        "..#.......#..",
        ".....###.....",
        "~~#.#...#.#~~",
        ".....###.....",
        "..#.......#..",
        "@.#..###..#.@",
        ".---.#.#.---.",
        "..####.####..",
        ".....#A#.....",
    ],
    # 4 - Vados: el agua parte el campo y el acero marca los pasos.
    [
        "....@...@....",
        ".##.......##.",
        ".##...#...##.",
        "......#......",
        "@@.##...##.@@",
        "......#......",
        "~~~...#...~~~",
        "......#......",
        "@@.##...##.@@",
        "......#......",
        ".##...#...##.",
        ".##..###..##.",
        ".....#A#.....",
    ],
    # 5 - Espina: dos pasillos centrales que van directos al aguila.
    [
        "..#.......#..",
        "..#.@...@.#..",
        "..#.......#..",
        ".###.###.###.",
        ".....#.#.....",
        "@@##.#.#.##@@",
        ".....#.#.....",
        ".###.#.#.###.",
        "..#..#.#..#..",
        "..#.......#..",
        "..######.....",
        ".....#.#.....",
        ".....#A#.....",
    ],
    # 6 - Embudo: todo el mapa empuja hacia el centro, y el centro es tuyo.
    [
        ".@.........@.",
        ".###.....###.",
        "...#.###.#...",
        ".#.#.#.#.#.#.",
        ".#...#...#.#.",
        ".#.###.###.#.",
        ".#...~.~...#.",
        ".#.###.###.#.",
        ".#.......#.#.",
        ".#.#####.#.#.",
        "...#...#.....",
        ".###.#.###...",
        ".....#A#.....",
    ],
    # 7 - Patinadero: pasillos largos con hielo en las esquinas.
    [
        "..-.......-..",
        ".###.###.###.",
        ".....#.#.....",
        "@##..#.#..##@",
        ".....#.#.....",
        ".--#.....#--.",
        "...#.###.#...",
        ".--#.###.#--.",
        ".....#.#.....",
        "@##..#.#..##@",
        "..-..#.#..-..",
        ".###.###.###.",
        ".....#A#.....",
    ],
    # 8 - Ultima: acero, agua y hielo a la vez, y el aguila al fondo de todo.
    [
        "..@.......@..",
        ".#.#.###.#.#.",
        ".#.#.....#.#.",
        ".#.##@.@##.#.",
        ".#.........#.",
        ".#.##~.~##..#",
        "...#.....#...",
        ".##..###..##.",
        ".....#.#.....",
        ".-##.#.#.##-.",
        ".....#.#.....",
        "..####.####..",
        ".....#A#.....",
    ],
]


def stage_count():
    return len(STAGES)


def stage(index):
    """Devuelve la fase index (0-based), ciclando si se pasa de la ultima."""
    return STAGES[index % len(STAGES)]
