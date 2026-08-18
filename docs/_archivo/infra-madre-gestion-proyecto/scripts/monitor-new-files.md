# monitor-new-files.py

**Descripción:** Detecta nuevos archivos en Madre y actualiza automáticamente

**Uso:**
```bash
cd docs/infra/madre
python3 scripts/monitor-new-files.py
```

**Funciones:**
- Escanea `docs/infra/madre/`
- Detecta archivos nuevos
- Detecta archivos modificados
- Detecta archivos eliminados
- Actualiza índices automáticamente
- Guarda estado en `file_state.json`

**Automatización:** Se ejecuta cada hora mediante `monitor-new-files.yml`

**Referencias:**
- [Scripts](README.md)
- [Madre](../README.md)
- [Workflows](../../../.github/workflows/monitor-new-files.yml)
