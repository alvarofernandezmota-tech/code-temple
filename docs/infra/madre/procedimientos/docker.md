# Operar Docker en Madre

## Comprobación inicial

```bash
docker info
docker ps -a
docker images
docker network ls
docker volume ls
```

## Antes de modificar un stack

- Identificar los datos persistentes.
- Revisar el archivo Compose.
- Comprobar puertos.
- Comprobar redes.
- Hacer backup si procede.

## Validación

Desde la carpeta del stack:

```bash
docker compose config
docker compose ps
docker compose logs --tail=100
```

## Documentación

Actualizar `docker.md`, `estructura.md`, `backups.md` y `cambios.md` cuando
corresponda.
