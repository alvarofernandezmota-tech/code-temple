# Changelog

## [2026-08-12] - Automatización de workflows

### Added
- Workflow `.github/workflows/update-estado.yml` para actualizar `estado.md` automáticamente
- Documentación de sesión en `docs/infra/madre/procedimientos/sesiones/`
- PAT_TOKEN como secret para permitir push desde workflows

### Changed
- `estado.md` ahora incluye fecha y hora en formato `YYYY-MM-DD HH:MM:SS`
- Permisos de GitHub Actions habilitados (Read and write)

### Fixed
- Workflow de actualización de estado.md funcionando correctamente

### Pending
- Automatización de README.md (índice de archivos)
- Automatización de cambios.md (registro de cambios)
- Notificaciones (Slack/Email)
- Workflows para security, backups, disaster-recovery, etc.
