# Scripts de Madre

**Última actualización:** 2026-08-13 13:36

## Resumen

- **Total scripts:** 9
- **Scripts Python:** 4
- **Scripts Bash:** 5

## Scripts Disponibles

### Limpieza y Mantenimiento

- `cleanup-temp.sh` - Limpia archivos temporales (.pyc, __pycache__, .tmp, vacíos)

### Monitoreo y Validación

- `monitor-new-files.py` - Detecta nuevos archivos y actualiza automáticamente
- `validate-structure.py` - Valida estructura de Madre (carpetas, READMEs, archivos sueltos)

### Estadísticas y Reportes

- `stats-madre.py` - Genera estadísticas de archivos y líneas de código
- `generar-reporte.sh` - Genera reportes consolidados

### Auditoría

- `audit-full.sh` - Auditoría completa de Madre
- `checklist-verification.sh` - Checklist de verificación
- `health-check.sh` - Verificación de salud de Madre

### Utilidades

- `analizar-outputs.sh` - Analiza outputs de Madre
- `consolidar-auditorias.sh` - Consolida auditorías
- `update-readme.sh` - Actualiza READMEs automáticamente
- `backup-madre.sh` - Backup automático de Madre
- `sync-git.sh` - Sincronización con Git

## Uso

### Limpieza

```bash
cd docs/infra/madre
./scripts/cleanup-temp.sh
```

### Monitoreo

```bash
cd docs/infra/madre
python3 scripts/monitor-new-files.py
```

### Validación

```bash
cd docs/infra/madre
python3 scripts/validate-structure.py
```

### Estadísticas

```bash
cd docs/infra/madre
python3 scripts/stats-madre.py
```

## Automatización

Estos scripts se ejecutan automáticamente mediante:

- `auto-cierre-madre.yml` - Cierre automático
- `monitor-new-files.yml` - Monitoreo de nuevos archivos
- `scheduled-audits.yml` - Auditorías programadas

## Referencias

- [Madre](../README.md)
- [Automatizaciones](../automatizaciones/README.md)
- [code-temple](../../README.md)
