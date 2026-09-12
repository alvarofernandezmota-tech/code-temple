#!/usr/bin/env bash
# Arranca TANK SCRAP 1990 en un solo paso: prepara el entorno si hace falta
# y lanza el juego. No toca el Python del sistema: todo va en .venv/
set -euo pipefail
cd "$(dirname "$0")"

PY=""
for c in python3 python; do
  if command -v "$c" >/dev/null 2>&1; then PY="$c"; break; fi
done
if [ -z "$PY" ]; then
  echo "No encuentro Python. Instalalo desde https://www.python.org/downloads/"
  exit 1
fi

if [ ! -d .venv ]; then
  echo "Preparando el entorno (solo la primera vez)..."
  "$PY" -m venv .venv
fi

VENV_PY=".venv/bin/python"
[ -x "$VENV_PY" ] || VENV_PY=".venv/Scripts/python.exe"

if ! "$VENV_PY" -c "import pygame" >/dev/null 2>&1; then
  echo "Instalando pygame..."
  "$VENV_PY" -m pip install --quiet --upgrade pip
  "$VENV_PY" -m pip install --quiet -r requirements.txt
fi

# Sin sesion grafica no hay ventana posible: pasa al entrar por SSH a un
# servidor. Mejor decirlo aqui que dejar que SDL falle a medio arrancar.
if [ -z "${DISPLAY:-}" ] && [ -z "${WAYLAND_DISPLAY:-}" ] && [ -z "${SDL_VIDEODRIVER:-}" ]; then
  case " $* " in
    *--selftest*) ;;   # el autotest corre sin ventana a proposito
    *)
      echo "Esta maquina no tiene pantalla (sesion: ${XDG_SESSION_TYPE:-desconocida})."
      echo
      echo "El juego necesita escritorio para abrir ventana. Dos salidas:"
      echo "  1. Jugarlo en un ordenador con escritorio."
      echo "  2. Servirlo en el navegador desde aqui y abrirlo desde otro aparato:"
      echo "       scripts/servir_web.sh"
      exit 2
      ;;
  esac
fi

echo "Arrancando TANK SCRAP 1990 — flechas para moverte, B para construir."
exec "$VENV_PY" -m tank_scrap "$@"
