#!/bin/bash
echo "=== Consolidar Auditorías ==="
echo "Fecha: $(date)"

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ISSUES_DIR="$BASE_DIR/../issues"
OUTPUT_DIR="$BASE_DIR/../outputs"

mkdir -p "$OUTPUT_DIR/consolidated"

for i in 05 06 07 08 09 10 11 12 13; do
  echo "Procesando issue #$i..."
  if [ -d "$ISSUES_DIR/issue-$i-"*"/audit" ]; then
    cp -r "$ISSUES_DIR/issue-$i-"*"/audit/"* "$OUTPUT_DIR/consolidated/" 2>/dev/null || true
  fi
done

echo "✅ Auditorías consolidadas en: $OUTPUT_DIR/consolidated"
