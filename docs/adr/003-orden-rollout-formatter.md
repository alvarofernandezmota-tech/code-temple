---
tipo: decision
fecha: 2026-08-22
repo: code-temple
etiquetas: [arquitectura, formatter, bifrost]
relacionado: [docs/ecosistema/plan-bot.md, docs/sesiones/2026/08-agosto/2026-08-22-sesion-2.md]
---

# ADR 003: Orden del rollout del validador de frontmatter

## Contexto
La sesion de "formatter" tiene que decidir por donde empezar: midgaror,
code-temple, o ambos a la vez.

## Decision
El validador de frontmatter se implementa primero en midgaror, y solo
despues se migra a code-temple. Dentro de midgaror, el primer objetivo
es validar los diarios (diario.py), no otras carpetas.

## Motivo
Coherente con la Fase 2 del plan bifrost (commit 8d7bba2, 2026-08-21):
"bifrost empieza solo con midgaror, extension a code-temple despues".
El primer comando real del bot (/hoy) escribe en midgaror, asi que
la validacion tiene que existir ahi primero para poder probar la
conexion bifrost -> diario.py de extremo a extremo con confianza.

## Estado
Aceptado — 2026-08-22.
