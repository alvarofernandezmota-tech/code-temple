#!/bin/bash
# Sincronización con Git

cd docs/infra/madre

# Verificar cambios
git status

# Pull y push
git pull --rebase
git push

echo "✅ Sincronización completada"
