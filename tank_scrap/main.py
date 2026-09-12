"""Punto de entrada: python3 -m tank_scrap [--selftest N] [--seed N]"""
import argparse

from .game import run


def main(argv=None):
    parser = argparse.ArgumentParser(description="TANK SCRAP 1990")
    parser.add_argument("--seed", type=int, default=None,
                        help="semilla aleatoria (partidas reproducibles)")
    parser.add_argument("--selftest", type=int, metavar="FRAMES", default=None,
                        help="corre N fotogramas sin ventana y sale (CI)")
    parser.add_argument("--arena", action="store_true",
                        help="empieza directamente en modo ARENA")
    args = parser.parse_args(argv)
    game = run(seed=args.seed, frames=args.selftest, headless=bool(args.selftest),
               mode="arena" if args.arena else None)
    if args.selftest:
        print("selftest ok (%s): %d fotogramas, nivel %d, puntos %d, chatarra %d"
              % (game.mode, args.selftest, game.stage_index + 1, game.score,
                 game.scrap))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
