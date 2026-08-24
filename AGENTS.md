# AGENTS.md — reglas para trabajar en este repo

## Antes de cualquier cambio en docs/infra/madre
- Correr docs/infra/madre/auditoria/revisar-madre.sh y verificar con
  docs/infra/madre/auditoria/auditoria.py antes de commitear
- Nunca dejar un .md como plantilla vacía sin dato real

## Commits
- Formato: tipo: descripción breve en presente
- Un commit por cambio lógico, no mezclar reestructuración con contenido

## Estructura del repo (no mover sin actualizar los README)
- docs/infra/ — estado real de servidores (madre, futuro acer)
- docs/sesiones/ — diario de trabajo, uno por día
- docs/ecosistema/ — mapa de repos y plan del bot bifrost
- scripts/ — automatización (auditoria-repo, generar-contexto, actualizar-agents-context, actualizar-changelog, auditoria-enlaces)
- docs/estandares/ — convenciones compartidas (frontmatter YAML)
- docs/procedimientos/ — checklists paso a paso para tareas recurrentes
- docs/adr/ — decisiones de arquitectura (5 ADRs: 001-bifrost-desde-cero.md, 002-regla-enganche-cuadruple.md, 003-orden-rollout-formatter.md, 004-convencion-scripts-procedimientos.md, 005-plan-maestro-ecosistema.md)

## Regla de mantenimiento
Cuando se cree o modifique un archivo en docs/ecosistema/, docs/adr/, docs/procedimientos/
o docs/estandares/, actualizar tambien scripts/generar-contexto.py
(lista ARCHIVOS) en el mismo commit. El volcado de contexto no puede
quedarse desactualizado.

## Arquitectura bifrost (cuando exista)
- Bifrost es solo interfaz, nunca lógica
- Toda función nueva se prueba primero en midgaror antes de exponerla
  como comando de Telegram

## Nunca hacer
- No crear automatizaciones que commiteen solas (nada de GitHub Actions
  escribiendo en docs/infra)
- No mezclar diario personal (va en midgaror) con sesiones de trabajo
  (van aquí)
- No dejar rutas relativas sin verificar tras mover archivos (usar
  auditoria.py o grep antes de dar por bueno un mv)
