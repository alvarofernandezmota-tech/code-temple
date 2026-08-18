# Auditoría de Madre

Cómo se comprueba que lo documentado en esta carpeta sigue siendo cierto.
El script que genera los datos está en [scripts/](scripts/README.md).

## Qué hacer con la salida

Comparar cada bloque contra el `.md` correspondiente y actualizar a mano lo
que no coincida, anotando la fecha en [cambios.md](cambios.md):

- `=== SISTEMA ===` → [sistema.md](sistema.md)
- `=== PAQUETES (resumen) ===` → [software.md](software.md)
- `=== PAQUETES (lista completa explícitos) ===` → [programas.md](programas.md)
- `=== DOCKER ===` → [docker.md](docker.md)
- `=== ESTRUCTURA ===` → [estructura.md](estructura.md)

El script nunca escribe en los `.md` directamente.
