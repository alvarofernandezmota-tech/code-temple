# Sesiones de trabajo

Log diario de trabajo en code-temple. Un archivo por día.

**Regla:** `YYYY-MM-DD.md` — un único archivo por día, con secciones internas si hay varios bloques de trabajo en el mismo día (usar plantilla-sesion.md).

## Estructura

docs/sesiones/
├── README.md
├── 2026/
│   └── 08-agosto/
│       ├── 2026-08-06-madre-documentacion.md
│       ├── 2026-08-12-infra-madre-auditoria.md
│       ├── 2026-08-13-cierre.md          ⚠ formato inconsistente (debería ser 2026-08-13.md)
│       ├── 2026-08-13-inicio.md          ⚠ formato inconsistente
│       ├── 2026-08-13-sesion/            ⚠ carpeta suelta (debería ser archivo)
│       ├── 2026-08-13-auditoria-infra-madre/ ⚠ carpeta suelta
│       ├── SESION-2026-08-13.md          ⚠ formato antiguo (mayúsculas)
│       ├── 2026-08-16-auditoria-reconciliacion.md
│       ├── 2026-08-18-reorganizacion-madre.md
│       ├── 2026-08-18.md
│       ├── 2026-08-21.md
│       ├── 2026-08-22-sesion-2.md        ⚠ formato inconsistente (debería ser 2026-08-22.md con secciones)
│       ├── 2026-08-22-sesion-3.md        ⚠ formato inconsistente
│       ├── 2026-08-22.md
│       ├── 2026-08-23.md
│       └── 2026-08-24.md
└── scripts/                              ⚠ ubicación incorrecta (debería ir en /scripts de la raíz)
    ├── README.md
    └── nueva_sesion.py                   ⚠ snake_case, no kebab-case

## Índice

- [2026/](2026/) — sesiones organizadas por año/mes
- [scripts/](scripts/) ⚠ pendiente mover a `scripts/` en la raíz del repo

## Relacionado con

- [docs/procedimientos/plantilla-sesion.md](../procedimientos/plantilla-sesion.md) — plantilla para documentar sesiones
- [docs/procedimientos/inicio-sesion.md](../procedimientos/inicio-sesion.md) — checklist al empezar
- [docs/procedimientos/cierre-sesion.md](../procedimientos/cierre-sesion.md) — checklist al terminar
- [docs/procedimientos/plantilla-readme.md](../procedimientos/plantilla-readme.md) — plantilla usada para este README
