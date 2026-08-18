# Infraestructura de Madre

Documentación de qué es y qué corre en Madre (servidor Arch Linux). Solo
información real y verificada — sin checklists vacíos ni automatización.

## Contenido

- [estado.md](estado.md) — estado general de la infraestructura
- [cambios.md](cambios.md) — historial de cambios reales, con fecha
- [sistema.md](sistema.md) — sistema operativo, kernel, hostname
- [software.md](software.md) — resumen de paquetes instalados (conteos)
- [programas.md](programas.md) — lista completa de paquetes explícitos
- [docker.md](docker.md) — versión de Docker, Compose, contenedores e imágenes
- [estructura.md](estructura.md) — árbol de carpetas relevantes del servidor
- [auditoria.md](auditoria.md) — cómo se comprueba que todo lo anterior sigue siendo cierto
- [scripts/](scripts/) — scripts manuales de solo lectura usados en la auditoría

## Regla

Ningún archivo aquí se actualiza solo. Todo lo que hay se escribió a mano
tras comprobar el dato real en el servidor. Si algo lleva más de un mes sin
actualizarse y ya no es cierto, se corrige o se borra — no se deja como
plantilla vacía.
