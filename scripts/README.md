# Scripts

Scripts de automatización de procedimientos de code-temple. Cada script tiene un procedimiento 1:1 en `docs/procedimientos/`.

## Estructura

scripts/
├── README.md
├── actualizar-agents-context.py   ← docs/procedimientos/actualizar-agents-context.md
├── actualizar-changelog.py        ← docs/procedimientos/actualizar-changelog.md (pendiente)
├── actualizar-readmes.py          ← docs/procedimientos/actualizar-readmes.md (pendiente)
├── auditoria-duplicados.py        ← docs/procedimientos/auditoria-duplicados.md (pendiente)
├── auditoria-enlaces.py           ← docs/procedimientos/auditoria-enlaces.md (pendiente)
├── auditoria-frontmatter.py       ← docs/procedimientos/auditoria-frontmatter.md (pendiente)
├── auditoria-repo.py              ← docs/procedimientos/auditoria-repo.md
├── cerrar-sesion.py               ← docs/procedimientos/cierre-sesion.md
├── cierre-completo.py             ← docs/procedimientos/cierre-completo.md
├── generar-contexto.py            ← docs/procedimientos/generar-contexto.md
├── generar-estructura.py          ← docs/procedimientos/generar-estructura.md (pendiente)
└── nueva_sesion.py                ← docs/procedimientos/nueva-sesion.md

## Scripts de actualización

### actualizar-agents-context.py
Actualiza automáticamente AGENTS.md y CONTEXT.md con la estructura actual.

```bash
python3 scripts/actualizar-agents-context.py
```

### actualizar-changelog.py
Añade entry automático al CHANGELOG.md con commits del día.

```bash
python3 scripts/actualizar-changelog.py [--fecha YYYY-MM-DD]
```

### actualizar-readmes.py
Actualiza READMEs de carpetas en docs/ con estructura real.

```bash
python3 scripts/actualizar-readmes.py
```

## Scripts de auditoría

### auditoria-duplicados.py
Busca archivos duplicados o solapados.

```bash
python3 scripts/auditoria-duplicados.py
```

### auditoria-enlaces.py
Verifica enlaces rotos en archivos .md.

```bash
python3 scripts/auditoria-enlaces.py
```

### auditoria-frontmatter.py
Verifica frontmatter YAML en archivos .md.

```bash
python3 scripts/auditoria-frontmatter.py
```

### auditoria-repo.py
Auditoría completa del repo (enlaces, frontmatter, estructura).

```bash
python3 scripts/auditoria-repo.py
```

## Scripts de sesión

### cerrar-sesion.py
Genera cierre automático de sesión (commits, issues, ADRs del día).

```bash
python3 scripts/cerrar-sesion.py [--fecha YYYY-MM-DD]
```

### cierre-completo.py
Automatiza cierre completo (actualiza AGENTS/CONTEXT, CHANGELOG, genera resumen).

```bash
python3 scripts/cierre-completo.py [--fecha YYYY-MM-DD]
```

### generar-contexto.py
Volcado de contexto completo a IA (todos los archivos críticos del repo).

```bash
python3 scripts/generar-contexto.py > /tmp/contexto.txt
```

### generar-estructura.py
Describe automáticamente toda la estructura del repo.

```bash
python3 scripts/generar-estructura.py > /tmp/estructura.txt
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
