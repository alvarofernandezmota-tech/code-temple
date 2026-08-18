# backup-madre.sh

**Descripción:** Backup automático de Madre

**Uso:**
```bash
cd docs/infra/madre
./scripts/backup-madre.sh
```

**Funciones:**
- Copia archivos importantes (.md, python/, scripts/)
- Comprime en `.tar.gz`
- Guarda en `/tmp/madre-backup-YYYYMMDD-HHMMSS.tar.gz`

**Referencias:**
- [Scripts](README.md)
- [Madre](../README.md)
- [Backups](../backups/README.md)
