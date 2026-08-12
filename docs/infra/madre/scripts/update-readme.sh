#!/bin/bash
# Actualizar README.md con índice de carpetas

README="docs/infra/madre/README.md"

# Listar carpetas de infraestructura
FOLDERS=$(ls -1 docs/infra/madre/ | grep -v "^\.md$" | grep -v "^issues$" | grep -v "^adr$" | grep -v "^scripts$")

# Generar índice
echo "## 📋 Índice" > /tmp/readme-index.md
echo "" >> /tmp/readme-index.md
for folder in $FOLDERS; do
  if [ -d "docs/infra/madre/$folder" ]; then
    echo "- [$folder](docs/infra/madre/$folder/)" >> /tmp/readme-index.md
  fi
done

# Insertar en README.md
sed -i '/## 📋 Índice/,/## /{//!d}' $README
sed -i '/## 📋 Índice/r /tmp/readme-index.md' $README

echo "✅ README.md actualizado"
