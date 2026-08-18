#!/bin/bash
# Revisar estado real de Madre — solo lectura, no modifica nada.
# Uso: bash revisar-madre.sh
# Compara la salida con sistema.md / software.md / docker.md y actualiza a mano si algo cambió.

echo "=== SISTEMA ==="
echo "Kernel: $(uname -r)"
echo "Hostname: $(hostname)"
echo "Distro: $(cat /etc/os-release | grep PRETTY_NAME | cut -d= -f2)"

echo ""
echo "=== PAQUETES ==="
echo "Explícitos: $(pacman -Qe | wc -l)"
echo "Totales: $(pacman -Q | wc -l)"
echo "AUR: $(pacman -Qm | wc -l)"

echo ""
echo "=== DOCKER ==="
docker --version 2>/dev/null || echo "Docker no instalado o no accesible"
docker compose version 2>/dev/null
docker ps --format "table {{.Names}}\t{{.Status}}" 2>/dev/null
