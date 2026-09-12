"""Mapas de las fases, escritos en celdas de 16 px (13x13).

Cada caracter es una celda clasica y se expande a 2x2 subtiles de 8 px, que es
la resolucion real a la que se destruyen y se construyen los muros.

  '.' vacio   '#' ladrillo   '@' acero   '~' agua   'x' arboles
  '-' hielo   'A' aguila (base)
"""

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
        "@...#...#...@",
        ".#.#.#.#.#.#.",
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
]


def stage_count():
    return len(STAGES)


def stage(index):
    """Devuelve la fase index (0-based), ciclando si se pasa de la ultima."""
    return STAGES[index % len(STAGES)]
