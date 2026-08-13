#!/bin/bash
# Limpieza de archivos temporales en Madre

echo "=== LIMPIEZA DE ARCHIVOS TEMPORALES ==="

# Eliminar archivos .pyc
find . -name "*.pyc" -delete
echo "✅ .pyc eliminados"

# Eliminar __pycache__
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
echo "✅ __pycache__ eliminados"

# Eliminar .tmp
find . -name "*.tmp" -delete
echo "✅ .tmp eliminados"

# Eliminar archivos vacíos
find . -type f -empty -delete
echo "✅ Archivos vacíos eliminados"

# Eliminar carpetas vacías
find . -type d -empty -delete 2>/dev/null
echo "✅ Carpetas vacías eliminadas"

echo "✅ LIMPIEZA COMPLETADA!"
