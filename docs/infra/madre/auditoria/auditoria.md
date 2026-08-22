# Auditoría de Madre

Cómo se comprueba que lo documentado en esta carpeta sigue siendo cierto.
El script que genera los datos está en [esta carpeta](README.md).

## Qué hacer con la salida

Comparar cada bloque contra el `.md` correspondiente y actualizar a mano lo
que no coincida, anotando la fecha en [cambios.md](../estado/cambios.md):

- `=== SISTEMA ===` → [sistema.md](../sistema/sistema.md)
- `=== PAQUETES (resumen) ===` → [software.md](../sistema/software.md)
- `=== PAQUETES (lista completa explícitos) ===` → [programas.md](../sistema/programas.md)
- `=== DOCKER ===` → [docker.md](../sistema/docker.md)
- `=== ESTRUCTURA ===` → [estructura.md](../sistema/estructura.md)

El script nunca escribe en los `.md` directamente.
