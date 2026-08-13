#!/bin/bash
# Comando para añadir contexto completo del repositorio

echo "=== CONTEXTO COMPLETO DE CODE-TEMPLE ==="
echo ""

# 1. Estructura general
echo "## Estructura del Repositorio"
find . -type d -maxdepth 2 ! -path './.git/*' | sort
echo ""

# 2. Temple (Plan Maestro)
echo "## Temple (Plan Maestro)"
if [ -f temple/PLAN_MAESTRO.md ]; then
    echo "- PLAN_MAESTRO.md existe"
    cat temple/PLAN_MAESTRO.md | head -20
else
    echo "- PLAN_MAESTRO.md no existe"
fi
echo ""

# 3. Madre (Infraestructura)
echo "## Madre (Infraestructura)"
echo "### Estructura"
find docs/infra/madre -type d -maxdepth 2 | sort | head -20
echo ""

echo "### Scripts Principales"
echo "- cleanup-temp.sh - Limpieza"
echo "- monitor-new-files.py - Monitoreo"
echo "- validate-structure.py - Validación"
echo "- stats-madre.py - Estadísticas"
echo "- backup-madre.sh - Backup"
echo "- sync-git.sh - Sincronización"
echo ""

echo "### Estadísticas"
if [ -f docs/infra/madre/ESTADISTICAS.md ]; then
    cat docs/infra/madre/ESTADISTICAS.md | grep -A 10 "Archivos por Tipo"
fi
echo ""

# 4. Workflows
echo "## Workflows"
ls -1 .github/workflows/*.yml | xargs -n1 basename
echo ""

# 5. Issues
echo "## Issues"
echo "### Abiertos"
gh issue list --state open --limit 10 2>/dev/null || echo "No se pudo obtener lista"
echo ""

# 6. Estado actual
echo "## Estado Actual"
git status --short | head -10
echo ""

# 7. Últimos commits
echo "## Últimos Commits"
git log --oneline -5
echo ""

# 8. Fases
echo "## Fases del Proyecto"
echo "### FASE 0 (Madre) - COMPLETADA"
echo "- 12 scripts Python"
echo "- 20 scripts Bash"
echo "- 104 Markdown"
echo "- 10 workflows"
echo "- Issue #37 cerrado"
echo ""

echo "### FASE 1 (Theodora) - EN PROGRESO"
echo "- Base de datos"
echo "- IA (Ollama, Open WebUI, Litellm)"
echo "- Automatización"
echo "- Issue #46 abierto"
echo ""

echo "CONTEXTO COMPLETO ANADIDO!"
