# Procedimientos de Infraestructura

## Automatización

### Workflows configurados
- ✅ **estado.md** - Actualización automática de fecha y hora
- ⏳ **README.md** - Pendiente (índice de archivos)
- ⏳ **cambios.md** - Pendiente (registro de cambios)

### Documentación de workflows
- [update-estado.md](workflows/update-estado.md) - Workflow que actualiza estado.md automáticamente

### Configuración requerida
1. PAT_TOKEN en secrets del repo
2. Permisos de escritura en GitHub Actions
3. Workflow en .github/workflows/

### Sesiones de trabajo
- [2026-08-12](sesiones/2026-08-12-automatizacion-workflows.md) - Automatización de workflows

### Otros procedimientos
- [Pull Requests (PRs)](pull-requests.md) - Qué son, cuándo usarlos, flujo de trabajo

## Pendientes
- README.md automático
- cambios.md automático
- Notificaciones (Slack/Email)
- Workflows para security, backups, disaster-recovery, etc.
