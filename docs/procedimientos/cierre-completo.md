# Cierre completo de sesión

Automatiza todo el proceso de cierre de sesión.

## Uso

```bash
python3 scripts/cierre-completo.py [--fecha YYYY-MM-DD]
```

## Qué hace

1. Actualiza `AGENTS.md` y `CONTEXT.md` (llama a `actualizar-agents-context.py`)
2. Genera resumen de commits, issues y ADRs del día
3. Indica qué actualizar en `CHANGELOG.md` y archivo de sesión

## Cuándo usar

- Al terminar cada sesión de trabajo
- Antes de hacer push final del día

## Relacionado con

- [scripts/cierre-completo.py](../../scripts/cierre-completo.py)
- [scripts/actualizar-agents-context.py](../../scripts/actualizar-agents-context.py)
- [cierre-sesion.md](cierre-sesion.md) — checklist manual de cierre
