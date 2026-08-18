# Auditoría de Madre

Cómo se comprueba que lo documentado en `sistema.md`, `software.md` y
`docker.md` sigue siendo cierto.

## revisar-madre.sh

Script de solo lectura. No modifica nada, no se ejecuta solo (sin cron, sin
GitHub Action). Se lanza a mano cuando se quiere comprobar el estado real:

```bash
bash docs/infra/madre/revisar-madre.sh
```

Imprime kernel, hostname, distro, número de paquetes (explícitos, totales,
AUR) y versión de Docker/Compose con los contenedores activos.

## Qué hacer con la salida

Comparar cada bloque contra el `.md` correspondiente:

- `=== SISTEMA ===` contra [sistema.md](sistema.md)
- `=== PAQUETES ===` contra [software.md](software.md)
- `=== DOCKER ===` contra [docker.md](docker.md)

Si algo no coincide, se corrige el `.md` a mano, con la fecha del cambio
anotada en [cambios.md](cambios.md). El script nunca escribe en los `.md`
directamente.
