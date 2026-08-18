# cleanup-temp.sh

**Descripción:** Limpia archivos temporales en Madre

**Uso:**
```bash
cd docs/infra/madre
./scripts/cleanup-temp.sh
```

**Funciones:**
- Elimina archivos `.pyc`
- Elimina carpetas `__pycache__`
- Elimina archivos `.tmp`
- Elimina archivos vacíos
- Elimina carpetas vacías

**Automatización:** Se ejecuta automáticamente antes de cada commit

**Referencias:**
- [Scripts](README.md)
- [Madre](../README.md)
