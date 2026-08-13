#!/bin/bash
# Backup automático de Madre

BACKUP_DIR="/tmp/madre-backup-$(date +%Y%m%d-%H%M%S)"
mkdir -p $BACKUP_DIR

# Copiar archivos importantes
cp -r docs/infra/madre/*.md $BACKUP_DIR/
cp -r docs/infra/madre/python $BACKUP_DIR/
cp -r docs/infra/madre/scripts $BACKUP_DIR/

# Comprimir
tar -czf $BACKUP_DIR.tar.gz -C $(dirname $BACKUP_DIR) $(basename $BACKUP_DIR)

echo "✅ Backup creado: $BACKUP_DIR.tar.gz"
