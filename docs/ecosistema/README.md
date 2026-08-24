# Ecosistema

Referencia viva del ecosistema de repos (qué existe, para qué sirve, estado actual).

## Estructura

docs/ecosistema/
├── README.md
├── fuente-de-verdad.md
├── infra-madre.md                    ⚠ solapa con docs/infra/madre/ (issue #52)
├── plan-bot.md
├── repos-activos.md
├── repos-archivados.md
└── vision.md

## Índice

- [fuente-de-verdad.md](fuente-de-verdad.md) — qué repo es la fuente de verdad de cada tipo de dato
- [infra-madre.md](infra-madre.md) — resumen de la máquina Madre (servidor principal) ⚠ pendiente decidir si se fusiona con docs/infra/madre/ o se archiva
- [plan-bot.md](plan-bot.md) — fases para conectar midgaror y code-temple vía bifrost (bot de Telegram)
- [repos-activos.md](repos-activos.md) — lista de repos activos y su propósito
- [repos-archivados.md](repos-archivados.md) — lista de repos congelados y por qué
- [vision.md](vision.md) — visión final del bot (ecosistema completo)

## Relacionado con

- [docs/infra/madre/](../infra/madre/) — documentación detallada de Madre (estado/, sistema/, auditoria/)
- [docs/adr/001-bifrost-desde-cero.md](../adr/001-bifrost-desde-cero.md) — decisión de crear bifrost
- [docs/procedimientos/plantilla-repo.md](../procedimientos/plantilla-repo.md) — estructura mínima de repos
- [docs/procedimientos/plantilla-readme.md](../procedimientos/plantilla-readme.md) — plantilla usada para este README
