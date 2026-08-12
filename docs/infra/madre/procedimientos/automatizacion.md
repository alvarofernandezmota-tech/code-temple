# Automatización de Documentación

## Objetivo
Automatizar la actualización de archivos de raíz y carpetas cuando se actualice documentación.

## Archivos y Carpetas

### 1. Carpetas de Infraestructura (10 carpetas)

**Carpetas:**
- `hardware/`
- `red/`
- `servicios/`
- `security/`
- `backups/`
- `disaster-recovery/`
- `monitoring/`
- `performance/`
- `change-management/`
- `procedimientos/`

**Automatización:**
- **Cuándo:** Cuando se actualice el `README.md` de una carpeta
- **Qué actualizar:**
  - `estado.md` → Fecha de última auditoría
  - `cambios.md` → Registro del cambio
- **Script:** `.github/workflows/update-estado.yml`

### 2. `adr/` (Decisiones Arquitecturales)

**Automatización:**
- **Cuándo:** Cuando se cree una nueva decisión arquitectónica
- **Qué actualizar:**
  - `adr/README.md` → Índice de ADRs
  - `cambios.md` → Registro del cambio
- **Script:** `.github/workflows/update-adr-index.yml`

### 3. `issues/` (Auditorías Detalladas)

**Automatización:**
- **Cuándo:** Cuando se complete una auditoría
- **Qué actualizar:**
  - GitHub Issues → Cerrar issue correspondiente
  - `cambios.md` → Registro del cambio
- **Script:** `.github/workflows/close-issue.yml`

### 4. `scripts/` (Scripts de Auditoría)

**Automatización:**
- **Cuándo:** Semanalmente (cron job)
- **Qué actualizar:**
  - Ejecutar scripts de auditoría
  - Generar reportes en `issues/`
- **Script:** `.github/workflows/run-audit-scripts.yml`

## Archivos de Raíz

### 1. `README.md`

**Automatización:**
- **Cuándo:** Cuando se agregue/elimine una carpeta
- **Qué actualizar:** Índice de carpetas
- **Script:** `scripts/update-readme.sh`

### 2. `estado.md`

**Automatización:**
- **Cuándo:** Cuando se actualice una carpeta de infra
- **Qué actualizar:** Fecha de última auditoría
- **Script:** `.github/workflows/update-estado.yml`

### 3. `cambios.md`

**Automatización:**
- **Cuándo:** Cuando se haga merge de un PR
- **Qué actualizar:** Registro del cambio
- **Script:** `.github/workflows/update-cambios.yml`

## Scripts de Automatización

### 1. `scripts/update-readme.sh`

**Función:** Actualizar índice de `README.md`

**Uso:**
```bash
./scripts/update-readme.sh
```

**Documentación:** [`scripts/update-readme.sh`](scripts/update-readme.sh)

### 2. `.github/workflows/update-estado.yml`

**Función:** Actualizar `estado.md` cuando cambie una carpeta

**Trigger:** Push en carpetas de infra

**Documentación:** [`.github/workflows/update-estado.yml`](.github/workflows/update-estado.yml)

### 3. `.github/workflows/update-cambios.yml`

**Función:** Actualizar `cambios.md` cuando se haga merge

**Trigger:** Pull request merged

**Documentación:** [`.github/workflows/update-cambios.yml`](.github/workflows/update-cambios.yml)

## Monitoreo

- Revisar logs de GitHub Actions semanalmente
- Verificar que los archivos se actualicen correctamente
- Reportar errores en issues

## Responsables

- **Desarrollo:** @alvarofernandezmota-tech
- **Revisión:** @alvarofernandezmota-tech
- **Mantenimiento:** @alvarofernandezmota-tech

## Fecha de creación

- **Creado:** 2026-08-12
- **Última actualización:** 2026-08-12
