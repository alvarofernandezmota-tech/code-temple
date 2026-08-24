# ADR — Architecture Decision Records

Decisiones de arquitectura del ecosistema, formato Michael Nygard (explicación del "por qué").

**Regla:** numeración secuencial estricta. Antes de crear un ADR nuevo, comprobar
el último número usado con `ls docs/adr/ | sort -V | tail -1`. Nunca reutilizar
ni editar retroactivamente un ADR aceptado (si cambia la decisión, se crea uno nuevo
que referencia al anterior como "supersedido").

## Estructura

docs/adr/
├── README.md
├── 001-bifrost-desde-cero.md
├── 002-regla-enganche-cuadruple.md
├── 003-orden-rollout-formatter.md
└── 004-convencion-scripts-procedimientos.md

## Índice

- [001-bifrost-desde-cero.md](001-bifrost-desde-cero.md) — decisión de crear bifrost desde cero (sin código heredado)
- [002-regla-enganche-cuadruple.md](002-regla-enganche-cuadruple.md) — regla para carpetas nuevas en docs/: README + índice + 3 docs mínimos + frontmatter
- [003-orden-rollout-formatter.md](003-orden-rollout-formatter.md) — orden de despliegue del validador de frontmatter: bifrost → midgaror → code-temple
- [004-convencion-scripts-procedimientos.md](004-convencion-scripts-procedimientos.md) — convención scripts + procedimientos por repo (1:1 entre script y doc)

## Relacionado con

- [docs/procedimientos/plantilla-repo.md](../procedimientos/plantilla-repo.md) — estructura mínima de repos (aplica ADR-004)
- [docs/ecosistema/plan-bot.md](../ecosistema/plan-bot.md) — plan que implementa ADR-001 (bifrost)
- [docs/estandares/frontmatter.md](../estandares/frontmatter.md) — estándar que implementa ADR-003
- [docs/procedimientos/plantilla-readme.md](../procedimientos/plantilla-readme.md) — plantilla usada para este README
