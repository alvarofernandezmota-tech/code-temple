# Fuente de verdad por repo

Cada repo es dueño exclusivo de un tipo de dato. Nadie más escribe ahí.

## midgaror
- diario/personal/ -> diario PERSONAL (vida, salud, ideas)
- NUNCA contiene sesiones de trabajo ni documentación técnica

## code-temple
- docs/sesiones/ -> diario de TRABAJO (sesiones, decisiones técnicas)
- docs/infra/ -> estado real de servidores (Madre, Acer)
- docs/ecosistema/ -> mapa y plan del ecosistema de repos
- docs/estandares/ -> convenciones compartidas (frontmatter, etc.)

## bifrost (cuando exista)
- No almacena nada propio
- Solo escribe en midgaror o code-temple según el tipo de contenido
- /hoy <texto> personal -> midgaror
- /sesion <texto> trabajo -> code-temple (fase 2c, no ahora)
