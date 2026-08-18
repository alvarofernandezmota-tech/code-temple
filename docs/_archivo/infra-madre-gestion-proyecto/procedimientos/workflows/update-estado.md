# Workflow: Update estado.md

## Descripción
Workflow que actualiza automáticamente la fecha y hora en `estado.md` cuando se modifican archivos en las carpetas de infraestructura.

## Archivo
- `.github/workflows/update-estado.yml`

## Trigger
Se ejecuta cuando hay un `push` en las siguientes carpetas:
- `docs/infra/madre/hardware/**`
- `docs/infra/madre/red/**`
- `docs/infra/madre/servicios/**`
- `docs/infra/madre/security/**`
- `docs/infra/madre/backups/**`
- `docs/infra/madre/disaster-recovery/**`
- `docs/infra/madre/monitoring/**`
- `docs/infra/madre/performance/**`
- `docs/infra/madre/change-management/**`
- `docs/infra/madre/procedimientos/**`

## Acción
Actualiza el campo `Última actualización` en `docs/infra/madre/estado.md` con la fecha y hora actual en formato `YYYY-MM-DD HH:MM:SS`.

## Configuración requerida
1. **PAT_TOKEN** en secrets del repo
   - URL: https://github.com/settings/tokens
   - Scopes: `repo`, `workflow`
   - Nombre: `code-temple-automation`

2. **Permisos de GitHub Actions**
   - URL: https://github.com/alvarofernandezmota-tech/code-temple/settings/actions
   - Workflow permissions: "Read and write permissions"
   - Allow GitHub Actions to create and approve pull requests: ✅

## Ejemplo de ejecución
Trigger: Push en docs/infra/madre/hardware/README.md
→ Workflow se ejecuta
→ Actualiza estado.md con fecha: 2026-08-12 21:00:00
→ Hace commit y push automático

text

## Referencias
- Issue: #17
- Sesión: [2026-08-12](../sesiones/2026-08-12-automatizacion-workflows.md)
- CHANGELOG: [2026-08-12](../../../../CHANGELOG.md)
