# Actualizar el inventario de Madre

## Paquetes

```bash
pacman -Qqe > docs/infra/madre/paquetes-explicitos.txt
```

## Servicios

```bash
systemctl list-units --type=service --state=running --no-pager
systemctl list-unit-files --type=service --state=enabled --no-pager
```

## Docker

```bash
docker ps -a
docker images
docker network ls
docker volume ls
```

## Red

```bash
nmcli general status
nmcli device status
sudo ufw status verbose
```

## Finalización

Comparar los resultados con los documentos de Madre y actualizar únicamente
aquello que haya cambiado realmente.
