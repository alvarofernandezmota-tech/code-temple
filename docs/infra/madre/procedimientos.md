# Procedimientos de Madre

## Flujo estándar de cambio

1. Entrar en el repositorio `code-temple`.
2. Leer `normas.md`.
3. Leer el documento de Madre que será afectado.
4. Consultar un procedimiento existente.
5. Comprobar el estado inicial del sistema.
6. Preparar backup si procede.
7. Ejecutar un único cambio controlado.
8. Verificar el resultado.
9. Actualizar los documentos afectados.
10. Registrar el cambio en `cambios.md`.
11. Crear o actualizar un ADR si procede.
12. Ejecutar la auditoría aplicable.
13. Revisar el diff.
14. Crear el commit.
15. Hacer push.
16. Confirmar que el árbol Git queda limpio.

## Tipos de cambio

### Paquetes

Actualizar:

- `paquetes-explicitos.txt`.
- `software.md`.
- `servicios.md`, si procede.
- `cambios.md`.

### Servicios

Actualizar:

- `servicios.md`.
- `software.md`, si se instaló software nuevo.
- `cambios.md`.

### Docker

Actualizar:

- `docker.md`.
- `estructura.md`, si cambia la organización.
- `backups.md`, si aparecen datos persistentes.
- `cambios.md`.

### Red

Actualizar:

- `red.md`.
- `hardware.md` o `sistema.md`, si procede.
- `cambios.md`.

### Arquitectura

Crear o actualizar un ADR en:

```text
docs/infra/madre/adr/
```

## Rollback

Antes de ejecutar el cambio se debe saber:

- Qué archivos se modifican.
- Qué datos están en riesgo.
- Qué backup existe.
- Qué comando o acción deshace el cambio.
- Cómo se comprobará la recuperación.
