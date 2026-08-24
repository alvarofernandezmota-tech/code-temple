# Actualizar AGENTS.md y CONTEXT.md

Actualizar automáticamente AGENTS.md y CONTEXT.md con la estructura actual del repo.

## Uso

```bash
python3 scripts/actualizar-agents-context.py
```

## Qué actualiza

- **AGENTS.md**: lista de scripts, ADRs, estructura del repo
- **CONTEXT.md**: estado actual, número de ADRs y scripts

## Cuándo usar

- Después de crear un nuevo script en `scripts/`
- Después de crear un nuevo ADR en `docs/adr/`
- Después de mover/renombrar carpetas en `docs/`
- Antes de commitear cambios estructurales

## Relacionado con

- [scripts/actualizar-agents-context.py](../../scripts/actualizar-agents-context.py)
- [AGENTS.md](../../AGENTS.md)
- [CONTEXT.md](../../CONTEXT.md)
