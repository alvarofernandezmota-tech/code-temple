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

echo "Arrancando TANK SCRAP 1990 — flechas para moverte, B para construir."
exec "$VENV_PY" -m tank_scrap "$@"
