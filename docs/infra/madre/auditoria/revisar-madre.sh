#!/bin/bash
# Revisar estado real de Madre — solo lectura, no modifica nada.
# Uso: bash docs/infra/madre/scripts/revisar-madre.sh

echo "=== SISTEMA ==="
echo "Kernel: $(uname -r)"
echo "Hostname: $(hostname)"
echo "Distro: $(cat /etc/os-release | grep PRETTY_NAME | cut -d= -f2)"

echo ""
echo "=== PAQUETES (resumen) ==="
echo "Explícitos: $(pacman -Qe | wc -l)"
echo "Totales: $(pacman -Q | wc -l)"
echo "AUR: $(pacman -Qm | wc -l)"

echo ""
echo "=== PAQUETES (lista completa explícitos) ==="
pacman -Qe

echo ""
echo "=== DOCKER ==="
docker --version 2>/dev/null || echo "Docker no instalado o no accesible"
docker compose version 2>/dev/null
echo ""
echo "--- Contenedores (todos) ---"
docker ps -a --format "table {{.Names}}\t{{.Image}}\t{{.Status}}" 2>/dev/null
echo ""
echo "--- Imágenes ---"
docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}" 2>/dev/null

echo ""
echo "=== ESTRUCTURA ==="
tree -L 2 -d /home /srv /etc/docker 2>/dev/null || echo "tree no instalado, usa 'ls -la' a mano"
