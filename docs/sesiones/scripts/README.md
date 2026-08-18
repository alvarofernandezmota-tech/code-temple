# Scripts de sesiones

## nueva_sesion.py

Crea el archivo de una sesion nueva directamente en docs/sesiones/AAAA/MM-mes/,
con la fecha de hoy y una plantilla minima (Objetivo, Contexto, Decisiones,
Cierre), y lo abre en el editor para que escribas al momento.

python3 docs/sesiones/scripts/nueva_sesion.py "nombre-corto-sesion"

Ejemplo:

python3 docs/sesiones/scripts/nueva_sesion.py "reorganizacion-madre"

Crea: docs/sesiones/2026/08-agosto/2026-08-18-reorganizacion-madre.md, y lo
abre directamente en `$EDITOR` (o `nano` si no tienes ninguno configurado).

## Modo "hoy"

python3 docs/sesiones/scripts/nueva_sesion.py hoy

Crea (o si ya existe, abre directamente) la sesión del día en curso, sin
necesidad de darle un nombre corto. Equivalente a `python diario.py hoy` en
midgaror.
