# Procedimientos

Guías how-to paso a paso. Convención: si un procedimiento tiene automatización,
el script vive en `scripts/[nombre].py` con el MISMO nombre base.

## Estructura

docs/procedimientos/
├── README.md
├── auditoria-repo.md ← script: scripts/auditoria-repo.py
├── cierre-sesion.md ← script: scripts/cerrar-sesion.py
├── generar-contexto.md ← script: scripts/generar-contexto.py
├── inicio-sesion.md
├── mantenimiento-documentacion.md
├── nueva-sesion.md ← script: scripts/nueva_sesion.py
├── plantilla-readme.md
├── plantilla-repo.md
└── plantilla-sesion.md

text

## Índice

### Procedimientos con script (1:1)
- [auditoria-repo.md](auditoria-repo.md) — auditoría del repo → `scripts/auditoria-repo.py`
- [cierre-sesion.md](cierre-sesion.md) — cierre automático de sesión → `scripts/cerrar-sesion.py`
- [generar-contexto.md](generar-contexto.md) — volcado de contexto → `scripts/generar-contexto.py`
- [nueva-sesion.md](nueva-sesion.md) — crear sesión nueva → `scripts/nueva_sesion.py`

### Procedimientos de sesión (checklists)
- [inicio-sesion.md](inicio-sesion.md) — checklist al empezar
- [cierre-sesion.md](cierre-sesion.md) — checklist al terminar

### Plantillas (sin script)
- [plantilla-readme.md](plantilla-readme.md) — patrón para READMEs de carpetas
- [plantilla-repo.md](plantilla-repo.md) — estructura mínima de repo nuevo
- [plantilla-sesion.md](plantilla-sesion.md) — plantilla para sesiones

## Relacionado con

- [scripts/README.md](../../scripts/README.md) — índice de scripts
- [docs/adr/004-convencion-scripts-procedimientos.md](../adr/004-convencion-scripts-procedimientos.md)
