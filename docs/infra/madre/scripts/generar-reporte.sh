#!/bin/bash
echo "=== Generar Reporte de Estado ==="
echo "Fecha: $(date)"

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOCS_DIR="$BASE_DIR/../docs/infra/madre"

echo "Estado General:"
echo "==============="
if [ -f "$DOCS_DIR/estado.md" ]; then
  grep -A 20 "Estado General" "$DOCS_DIR/estado.md" | head -15
fi

echo ""
echo "✅ Reporte generado"
