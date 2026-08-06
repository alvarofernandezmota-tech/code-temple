# Recuperación de Madre

## Prioridad

1. Proteger los datos.
2. Identificar el alcance del fallo.
3. No ejecutar reparaciones destructivas sin backup.
4. Registrar las acciones realizadas.

## Diagnóstico inicial

```bash
systemctl --failed --no-pager
df -h
mount
ip address
sudo ufw status verbose
docker ps -a
```

## Recuperación

Seguir el procedimiento específico del componente afectado:

- Sistema: `sistema.md`.
- Servicios: `revisar-servicios.md`.
- Docker: `docker.md`.
- Red: `red-firewall.md`.
- Backups: `backups.md`.

## Después

Actualizar:

- `estado.md`.
- El documento afectado.
- `cambios.md`.
- El ADR correspondiente si cambió la arquitectura.
