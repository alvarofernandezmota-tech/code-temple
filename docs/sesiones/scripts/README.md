# Scripts de sesiones

## nueva_sesion.py

Crea el archivo de una sesion nueva directamente en docs/sesiones/AAAA/MM-mes/,
con la fecha de hoy y una plantilla minima (Objetivo, Contexto, Decisiones,
Cierre). No modifica ni borra sesiones existentes.

python3 docs/sesiones/scripts/nueva_sesion.py "nombre-corto-sesion"

Ejemplo:

python3 docs/sesiones/scripts/nueva_sesion.py "reorganizacion-madre"

Crea: docs/sesiones/2026/08-agosto/2026-08-18-reorganizacion-madre.md

Tras crearlo, abre el archivo directamente en tu editor (usa `$EDITOR` si lo
tienes configurado; si no, `nano` por defecto), para que escribas la sesión
en el momento.
