# Pendiente para la próxima sesión

> **Estado: RESUELTO 2026-08-22.** Los 3 puntos de abajo se completaron
> en la sesion de hoy. Ver docs/sesiones/2026/08-agosto/2026-08-22.md.

Última sesión: 2026-08-21

## 1. Auditar todo lo hecho hoy
- Correr docs/infra/madre/auditoria/auditoria.py y confirmar "Todo coincide"
- Revisar que docs/ecosistema/ y docs/estandares/ siguen reflejando la realidad
- Confirmar que docs/sesiones/2026/08-agosto/2026-08-21.md quedó completo

## 2. Crear AGENTS.md y CONTEXT.md en code-temple
Siguiendo el patrón de THDORA-PERSONAL (AGENTS.md con reglas, CONTEXT.md
con resumen de 30 segundos). Contenido ya redactado, pendiente de crear
los archivos y commitear:
- AGENTS.md: reglas de esta base de código (auditoría antes de tocar
  infra/madre, formato de commits, arquitectura bifrost, lista de
  "nunca hacer")
- CONTEXT.md: qué es code-temple, sustituto de yggdrasil-dew, puntero
  a docs/ecosistema/README.md y AGENTS.md

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

## Ampliacion futura del formatter en midgaror (no en esta sesion)
**Pertenece a: midgaror + bifrost (bot), no a code-temple.**
diario/personal/ ya tiene su script (diario.py, parcheado con frontmatter
el 2026-08-22) y es lo unico probado hasta ahora.

Pendiente para cuando se retome:
- habitos/ y tareas/: necesitan su propio script equivalente a diario.py
  (mismo patron: genera el archivo del dia, inyecta frontmatter), con
  un JSON dentro de cada carpeta para el dato estructurado (no solo
  texto libre como el diario)
- formacion/: retomar los diarios de formacion de la carpeta raiz
  02-FORMACION/, actualmente aplazados; decidir si usan el mismo
  patron de script o uno propio
- La idea de fondo: completar un diario con lo que se hace por hora
  (igual que se ha hecho hoy en docs/sesiones/ de code-temple), pero
  aplicado a habitos y tareas dentro de midgaror

## Diseño futuro: diario unificado con tablas de habitos/tareas/horario
**Pertenece a: midgaror + bifrost (bot), no a code-temple.**
Decision pendiente: el diario de cada dia (diario/personal/AAAA-MM-DD.md)
deberia mostrar 3 tablas (habitos, tareas, horario del dia) ademas del
texto libre de siempre.

Propuesta de diseño (sin implementar aun):
- El dato real de habitos y tareas vive en JSON separado (uno por
  carpeta, como ya se documento arriba)
- Un script regenera las tablas markdown dentro del diario del dia a
  partir de ese JSON cada vez que cambia algo
- Asi el diario sigue siendo un unico archivo legible, pero el bot
  actualiza datos estructurados fiables, no texto libre parseado
