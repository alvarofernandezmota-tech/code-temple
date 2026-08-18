# Auditoría de Madre

Cómo se comprueba que lo documentado en `sistema.md`, `software.md`,
`programas.md`, `docker.md` y `estructura.md` sigue siendo cierto.

## scripts/revisar-madre.sh

Script de solo lectura. No modifica nada, no se ejecuta solo (sin cron, sin
GitHub Action). Se lanza a mano:

```bash
bash docs/infra/madre/scripts/revisar-madre.sh
```

## Qué hacer con la salida

Comparar cada bloque contra el `.md` correspondiente y actualizar a mano lo
que no coincida, anotando la fecha en [cambios.md](cambios.md):

- `=== SISTEMA ===` → [sistema.md](sistema.md)
- `=== PAQUETES (resumen) ===` → [software.md](software.md)
- `=== PAQUETES (lista completa explícitos) ===` → [programas.md](programas.md)
- `=== DOCKER ===` → [docker.md](docker.md)
- `=== ESTRUCTURA ===` → [estructura.md](estructura.md)

El script nunca escribe en los `.md` directamente.
