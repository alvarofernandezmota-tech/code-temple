---
tipo: decision
fecha: 2026-08-22
repo: code-temple
etiquetas: [arquitectura, bifrost]
relacionado: [docs/ecosistema/plan-bot.md]
---

# ADR 001: Bifrost se construye desde cero, no se adapta THDORA-PERSONAL

## Contexto
La Fase 1 del plan del bot pedía revisar THDORA-PERSONAL (código +
issues) antes de decidir si reutilizar su base o crear un repo nuevo
llamado bifrost.

## Decisión
Se reaprovecha el patrón de documentación de THDORA-PERSONAL
(AGENTS.md con reglas + CONTEXT.md con resumen de 30 segundos), pero
el bot bifrost se construye desde cero como repositorio nuevo.

## Motivo
La regla de arquitectura definida para bifrost (solo interfaz, nunca
lógica; toda función nueva se construye y prueba primero como script
en midgaror) no encaja con reciclar el código de THDORA-PERSONAL, que
mezclaba lógica e interfaz.

## Estado
Aceptado — 2026-08-22.
