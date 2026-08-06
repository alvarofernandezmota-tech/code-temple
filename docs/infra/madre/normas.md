# Normas operativas de Madre

## Alcance

Estas normas se aplican exclusivamente al equipo Madre.

Las normas generales de infraestructura están fuera de esta carpeta. Este
documento añade las reglas específicas necesarias para operar Madre de forma
segura y auditable.

## Fuente de verdad

La documentación versionada de `code-temple` es la fuente de verdad
documental de Madre.

Si el sistema real y la documentación difieren:

1. Se registra la discrepancia.
2. Se comprueba cuál es el estado real.
3. Se corrige la documentación o el sistema de forma controlada.
4. Se registra el cambio en `cambios.md`.

## Reglas obligatorias

1. Leer la documentación afectada antes de modificar Madre.
2. Comprobar el estado actual antes de ejecutar cambios.
3. Realizar un único cambio importante cada vez.
4. Hacer backup cuando exista riesgo para datos o configuración.
5. No guardar contraseñas, tokens, claves privadas ni archivos `.env`.
6. No ejecutar comandos destructivos sin comprobar antes su alcance.
7. Verificar el resultado después de cada cambio.
8. Actualizar el inventario correspondiente.
9. Registrar el cambio en `cambios.md`.
10. Crear un ADR si cambia la arquitectura o una decisión estructural.
11. Mantener siempre una forma conocida de revertir los cambios.
12. Comprobar que el árbol Git queda limpio al finalizar.

## Software

Después de instalar o eliminar paquetes:

```bash
pacman -Qqe > docs/infra/madre/paquetes-explicitos.txt
```

También se deben actualizar:

- `software.md`.
- `servicios.md`, si afecta a systemd.
- `docker.md`, si afecta a Docker.
- `cambios.md`.

## Red y firewall

Toda modificación de NetworkManager, Wi-Fi, UFW, puertos o conectividad debe:

- Tener un motivo documentado.
- Registrar el estado anterior.
- Tener un rollback.
- Verificarse después del cambio.
- Actualizar `red.md`.

## Docker

Todo stack Docker debe documentar:

- Nombre.
- Servicios.
- Puertos.
- Redes.
- Volúmenes.
- Ubicación de los datos.
- Procedimiento de actualización.
- Procedimiento de backup.
- Procedimiento de restauración.

## Regla de reversión

Todo cambio relevante debe tener una forma conocida de deshacerlo antes de
ejecutarse.

## Finalización

Un cambio no se considera terminado hasta que:

- El sistema funciona.
- La documentación está actualizada.
- El cambio aparece en `cambios.md`.
- Las comprobaciones aplicables pasan.
- Git no muestra cambios pendientes.
