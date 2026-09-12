#!/usr/bin/env bash
# Construye la version web del juego y la sirve en la red local, para jugarlo
# desde el navegador de cualquier aparato de casa (movil incluido).
#
#   scripts/servir_web.sh            # puerto 8000
#   scripts/servir_web.sh 9000       # otro puerto
#
# Solo se expone a tu red local, no a internet.
set -euo pipefail
cd "$(dirname "$0")/.."

PORT="${1:-8000}"

PY=""
for c in python3 python; do
  if command -v "$c" >/dev/null 2>&1; then PY="$c"; break; fi
done
[ -n "$PY" ] || { echo "No encuentro Python."; exit 1; }

if [ ! -d .venv ]; then
  echo "Preparando el entorno..."
  "$PY" -m venv .venv
fi
VENV_PY=".venv/bin/python"
[ -x "$VENV_PY" ] || VENV_PY=".venv/Scripts/python.exe"

if ! "$VENV_PY" -c "import pygbag" >/dev/null 2>&1; then
  echo "Instalando pygbag (compilador a web)..."
  "$VENV_PY" -m pip install --quiet --upgrade pip
  "$VENV_PY" -m pip install --quiet pygbag
fi

echo "Construyendo la version web (la primera vez descarga el runtime)..."
"$VENV_PY" -m pygbag --build main.py

WEB="build/web"
[ -d "$WEB" ] || { echo "pygbag no dejo nada en $WEB; revisa su salida de arriba."; exit 1; }

IP="$(hostname -I 2>/dev/null | awk '{print $1}')"
[ -n "${IP:-}" ] || IP="$(hostname)"
echo
echo "Sirviendo en:"
echo "  http://localhost:$PORT       (en esta maquina)"
echo "  http://$IP:$PORT             (desde el movil o otro PC de tu red)"
echo
echo "Ctrl-C para parar."
cd "$WEB"
exec "$VENV_PY" -m http.server "$PORT" --bind 0.0.0.0
