# Scripts

Scripts de automatización de procedimientos de code-temple. Cada script tiene un procedimiento 1:1 en docs/procedimientos/. Convención: cada script 1:1 con un procedimiento en `docs/procedimientos/`.

## Estructura

scripts/
├── README.md
├── auditoria-repo.py ← procedimiento: docs/procedimientos/auditoria-repo.md
├── cerrar-sesion.py ← procedimiento: docs/procedimientos/cierre-sesion.md
├── generar-contexto.py ← procedimiento: docs/procedimientos/generar-contexto.md
└── nueva_sesion.py ← procedimiento: docs/procedimientos/nueva-sesion.md (pendiente)

text

## Scripts

### auditoria-repo.py
Auditoría automática del repo (enlaces rotos, frontmatter, estructura).

```bash
python3 scripts/auditoria-repo.py
```

### cerrar-sesion.py
Genera cierre automático de sesión (commits, issues, ADRs del día).

```bash
python3 scripts/cerrar-sesion.py [--fecha YYYY-MM-DD]
```

### generar-contexto.py
Volcado de contexto completo a IA (todos los archivos críticos del repo).

```bash
python3 scripts/generar-contexto.py
```

### nueva_sesion.py
Crea archivo de sesión nueva en `docs/sesiones/YYYY/MM-mes/`.

```bash
python3 scripts/nueva_sesion.py "nombre-corto"
python3 scripts/nueva_sesion.py hoy
```

## Relacionado con

- [docs/procedimientos/README.md](../docs/procedimientos/README.md) — procedimientos 1:1 con scripts
- [docs/adr/004-convencion-scripts-procedimientos.md](../docs/adr/004-convencion-scripts-procedimientos.md) — ADR de convención
