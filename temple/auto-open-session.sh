#!/bin/bash
# Apertura automática de sesión con checklist

echo "=== APERTURA AUTOMÁTICA DE SESIÓN ==="
echo "Fecha: $(date)"

# 1. Verificar cambios pendientes
echo "\n=== VERIFICANDO CAMBIOS ==="
git status

# 2. Verificar issues abiertos
echo "\n=== ISSUES ABIERTOS ==="
gh issue list --state open --limit 5

# 3. Verificar workflows fallidos
echo "\n=== WORKFLOWS ==="
gh run list --limit 5

# 4. Checklist de apertura
echo "\n=== CHECKLIST DE APERTURA ==="
echo "1. [ ] Verificar cambios pendientes"
echo "2. [ ] Revisar issues abiertos"
echo "3. [ ] Revisar workflows fallidos"
echo "4. [ ] Ejecutar limpieza"
echo "5. [ ] Planificar tareas del día"

# 5. Ejecutar limpieza
echo "\n=== LIMPIEZA ==="
./docs/infra/madre/scripts/cleanup-temp.sh

# 6. Guardar estado
date +%s > /tmp/last_activity
echo "Sesión abierta" > /tmp/session_status

echo "\n✅ APERTURA AUTOMÁTICA COMPLETADA!"
