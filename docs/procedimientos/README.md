# Procedimientos

Guías how-to paso a paso. Convención: si un procedimiento tiene automatización,
el script vive en `scripts/[nombre].py` con el MISMO nombre base que el documento.

## Estructura

docs/procedimientos/
├── README.md
├── auditoria-repo.md              ← script: scripts/auditoria-repo.py
├── cierre-sesion.md
├── generar-contexto.md            ← script: scripts/generar-contexto.py
├── inicio-sesion.md
├── plantilla-readme.md
├── plantilla-repo.md
└── plantilla-sesion.md

## Índice

### Procedimientos con script (1:1)
- [auditoria-repo.md](auditoria-repo.md) — auditoría del repo (enlaces rotos, frontmatter, estructura) → `scripts/auditoria-repo.py`
- [generar-contexto.md](generar-contexto.md) — volcado de contexto a IA → `scripts/generar-contexto.py`

### Procedimientos de sesión (checklists)
- [cierre-sesion.md](cierre-sesion.md) — checklist al terminar de trabajar (paso 1: correr auditoria-repo.py)
- [inicio-sesion.md](inicio-sesion.md) — checklist al empezar a trabajar (paso 2: generar contexto con generar-contexto.py)

### Plantillas (sin script, son docs base)
- [plantilla-readme.md](plantilla-readme.md) — patrón para todos los README de carpetas en docs/
- [plantilla-repo.md](plantilla-repo.md) — estructura mínima de un repo nuevo (ADR-004)
- [plantilla-sesion.md](plantilla-sesion.md) — plantilla para documentar cada sesión de trabajo

## Relacionado con

- [scripts/README.md](../../scripts/README.md) — índice de scripts (1:1 con procedimientos con script)
- [docs/adr/004-convencion-scripts-procedimientos.md](../adr/004-convencion-scripts-procedimientos.md) — ADR que define esta convención
- [docs/sesiones/README.md](../sesiones/README.md) — dónde se aplican las sesiones documentadas
