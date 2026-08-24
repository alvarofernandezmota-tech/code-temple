# Procedimientos

Guías how-to paso a paso. Convención: si un procedimiento tiene automatización,
el script vive en `scripts/[nombre].py` con el MISMO nombre base que el documento.

## Estructura

docs/procedimientos/
├── README.md
├── cierre-sesion.md
├── inicio-sesion.md
├── plantilla-readme.md
├── plantilla-repo.md
└── plantilla-sesion.md

## Índice

- [cierre-sesion.md](cierre-sesion.md) — checklist al terminar de trabajar (conecta con scripts/auditoria-repo.py)
- [inicio-sesion.md](inicio-sesion.md) — checklist al empezar a trabajar (conecta con scripts/generar-contexto.py)
- [plantilla-readme.md](plantilla-readme.md) — patrón para todos los README de carpetas en docs/
- [plantilla-repo.md](plantilla-repo.md) — estructura mínima de un repo nuevo (ADR-004)
- [plantilla-sesion.md](plantilla-sesion.md) — plantilla para documentar cada sesión de trabajo

## Relacionado con

- [scripts/README.md](../../scripts/README.md) — índice de scripts (1:1 con procedimientos)
- [docs/adr/004-convencion-scripts-procedimientos.md](../adr/004-convencion-scripts-procedimientos.md) — ADR que define esta convención
- [docs/sesiones/README.md](../sesiones/README.md) — dónde se aplican las sesiones documentadas
