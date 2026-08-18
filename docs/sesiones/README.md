# Sesiones

Registro de las sesiones de trabajo en este repositorio. Cada sesión es un
archivo Markdown con fecha, agrupado por año y mes.

## Estructura

    docs/sesiones/
    ├── AAAA/
    │   └── MM-mes/
    │       └── AAAA-MM-DD-nombre-corto.md
    └── scripts/
        └── nueva_sesion.py

Cada sesión vive en `AAAA/MM-mes/`, nunca suelta en la raíz. Esto se
reorganizó completo el 2026-08-18: antes había archivos y carpetas sueltas
con fecha en el nombre directamente en `docs/sesiones/`, ahora todo pasa
por `scripts/nueva_sesion.py` para no repetir el problema.

## Cómo crear una sesión nueva

    python3 docs/sesiones/scripts/nueva_sesion.py "nombre-corto-sesion"

Crea el archivo ya ubicado en `AAAA/MM-mes/AAAA-MM-DD-nombre-corto.md`, con
una plantilla mínima (Objetivo, Contexto, Decisiones, Cierre). Más detalle
en [scripts/README.md](scripts/README.md).

## Excepciones

- `neural-os-sesion-01/` no sigue el esquema de fecha porque es de otro
  proyecto (Neural OS), no una sesión de trabajo en este repo. Se deja
  donde está, fuera de las carpetas de año/mes.

## Pendiente

El 13 de agosto de 2026 quedaron varias versiones distintas de la misma
sesión (`SESION-2026-08-13.md`, `2026-08-13-inicio.md`,
`2026-08-13-cierre.md`, `2026-08-13-sesion/`,
`2026-08-13-auditoria-infra-madre/`) mezcladas dentro de `2026/08-agosto/`.
Falta comparar su contenido y fusionarlas en una sola. Ver
[cambios.md](../infra/madre/cambios.md) — pendiente anotar aquí cuando se
resuelva.
