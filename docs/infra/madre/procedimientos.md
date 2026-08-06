# Procedimientos de Madre

## Procedimiento estándar de cambio

1. Entrar en `code-temple`.
2. Leer `normas.md` y el documento afectado.
3. Comprobar el estado actual de Madre.
4. Consultar un runbook existente.
5. Preparar backup si procede.
6. Ejecutar un único cambio controlado.
7. Verificar el resultado.
8. Actualizar la documentación de Madre.
9. Registrar el cambio en `cambios.md`.
10. Crear o actualizar un ADR si cambia la arquitectura.
11. Revisar el diff.
12. Ejecutar las comprobaciones de auditoría aplicables.
13. Crear el commit.
14. Subirlo a GitHub.
15. Confirmar que el árbol queda limpio.

## Instalación de software

- Registrar el motivo de la instalación.
- Instalar el paquete.
- Actualizar `paquetes-explicitos.txt`.
- Actualizar `software.md`.
- Comprobar si se han creado servicios.
- Registrar el cambio.
- Verificar el funcionamiento.

## Modificación de red o firewall

- Documentar el motivo.
- Comprobar las reglas actuales.
- Aplicar una sola modificación.
- Verificar conectividad.
- Verificar UFW.
- Actualizar `red.md`.
- Preparar rollback.

## Modificación de Docker

- Registrar el stack afectado.
- Revisar volúmenes y datos persistentes.
- Hacer backup si procede.
- Validar el Compose.
- Aplicar el cambio.
- Verificar contenedores, redes y volúmenes.
- Actualizar `docker.md`.
- Registrar el cambio.

## Finalización

No se considera terminado un cambio si no están actualizados el inventario,
el historial y el estado de Git.
