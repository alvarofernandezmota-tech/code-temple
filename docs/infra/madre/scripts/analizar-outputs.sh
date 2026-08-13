#!/bin/bash
echo "=== Analizar Outputs ==="
echo "Fecha: $(date)"

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUTS_DIR="$BASE_DIR/../issues"

echo "Analizando CPU..."
if [ -f "$OUTPUTS_DIR/issue-05-hardware/outputs/$(date +%Y-%m-%d)/cpu-info.txt" ]; then
  cat "$OUTPUTS_DIR/issue-05-hardware/outputs/$(date +%Y-%m-%d)/cpu-info.txt"
fi

echo "Analizando RAM..."
if [ -f "$OUTPUTS_DIR/issue-05-hardware/outputs/$(date +%Y-%m-%d)/ram-info.txt" ]; then
  cat "$OUTPUTS_DIR/issue-05-hardware/outputs/$(date +%Y-%m-%d)/ram-info.txt"
fi

echo "Analizando Disk..."
if [ -f "$OUTPUTS_DIR/issue-05-hardware/outputs/$(date +%Y-%m-%d)/disk-info.txt" ]; then
  cat "$OUTPUTS_DIR/issue-05-hardware/outputs/$(date +%Y-%m-%d)/disk-info.txt"
fi

echo "✅ Análisis completado"
