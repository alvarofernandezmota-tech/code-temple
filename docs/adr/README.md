# ADR — Architecture Decision Records

Decisiones de arquitectura del ecosistema, formato Michael Nygard.

**Regla:** numeración secuencial estricta. Antes de crear un ADR nuevo, comprobar
el último número usado con `ls docs/adr/ | sort -V | tail -1`. Nunca reutilizar
ni editar retroactivamente un ADR aceptado (si cambia la decisión, se crea uno nuevo
que referencia al anterior como "supersedido").

## Índice

- [001-bifrost-desde-cero.md](001-bifrost-desde-cero.md)
- [002-regla-enganche-cuadruple.md](002-regla-enganche-cuadruple.md)
- [003-orden-rollout-formatter.md](003-orden-rollout-formatter.md)
- [004-estructura-documentacion.md](004-estructura-documentacion.md)
