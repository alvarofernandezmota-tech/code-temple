# Pendiente para la próxima sesión

Última sesión: 2026-08-21

## 1. Auditar todo lo hecho hoy
- Correr docs/infra/madre/auditoria/auditoria.py y confirmar "Todo coincide"
- Revisar que docs/ecosistema/ y docs/estandares/ siguen reflejando la realidad
- Confirmar que docs/sesiones/2026/08-agosto/2026-08-21.md quedó completo

## 2. Crear AGENT.md y CONTEXT.md en code-temple
Siguiendo el patrón de THDORA-PERSONAL (AGENT.md con reglas, CONTEXT.md
con resumen de 30 segundos). Contenido ya redactado, pendiente de crear
los archivos y commitear:
- AGENT.md: reglas de esta base de código (auditoría antes de tocar
  infra/madre, formato de commits, arquitectura bifrost, lista de
  "nunca hacer")
- CONTEXT.md: qué es code-temple, sustituto de yggdrasil-dew, puntero
  a docs/ecosistema/README.md y AGENT.md

## 3. Documentar fuente de verdad por repo (si no se hizo ya)
docs/ecosistema/fuente-de-verdad.md — midgaror=personal,
code-temple=trabajo/infra/ecosistema, bifrost=solo interfaz

## 4. Decidir y crear el repo bifrost
Pendiente de confirmar: público, descripción "Bot conector Telegram
-> GitHub. Empieza escribiendo solo en midgaror (diario personal)"
No creado todavía — requiere confirmación explícita antes de ejecutar.

## 5. Antes de programar bifrost
Revisar si hace falta mejorar/crear funciones en midgaror (tareas,
hábitos) ANTES de exponerlas como comandos del bot. Bifrost es solo
interfaz, no lógica.

## Regla
No se empieza nada de la lista 2-4 sin repasar primero el punto 1
(auditoría de lo ya hecho).
