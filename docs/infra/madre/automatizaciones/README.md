# Automatizaciones de Madre

**Última actualización:** 2026-08-13 13:36

## Resumen

- **Total scripts:** 3
- **Total workflows:** 4

## Scripts Disponibles

- `generate_madre_structure.py` - Genera estructura completa de Madre
- `update_root_readme_all.py` - Actualiza README de raíz con todo el contenido
- `update_root_readme.py` - Actualiza README de raíz

## Workflows

- `auto-cierre-madre.yml` - Cierre automático de Madre
- `auto-cierre-temple.yml` - Cierre automático de Temple
- `auto-generate-all-readmes.yml` - Genera todos los READMEs
- `monitor-new-files.yml` - Monitorea nuevos archivos
- `scheduled-audits.yml` - Auditorías programadas
- `update-estado.yml` - Actualiza estado
- `update-madre-root.yml` - Actualiza estructura de Madre

## Uso

### Generar estructura

```bash
cd docs/infra/madre
python3 automatizaciones/scripts/generate_madre_structure.py
```

### Actualizar README

```bash
cd docs/infra/madre
python3 automatizaciones/scripts/update_root_readme_all.py
```

## Automatización

Estos scripts se ejecutan automáticamente mediante workflows de GitHub Actions.

## Referencias

- [Madre](../README.md)
- [Scripts](../scripts/README.md)
- [code-temple](../../README.md)
