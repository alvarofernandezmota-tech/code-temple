# Madre — infraestructura completa

> Sistema reinstalado 2026-08-06 con Arch Linux puro. Reconstrucción desde cero.
> Última verificación: 2026-08-06 19:57 CEST

## Sistema base

- Hostname: `archlinux`
- Kernel: `7.1.5-arch1-2`
- Entorno de escritorio: **KDE Plasma**
- Disco: `/dev/sda2` root 49G (14G usados) · `/dev/sda3` /home 866G (5,2G usados)
- RAM: 15Gi total, ~5Gi en uso

## Paquetes instalados

- 119 explícitos, 829 totales con dependencias
- Lista completa en `docs/infra/madre/paquetes-explicitos.txt`
- AUR: yay (`~/yay-git/`)

## Estructura de directorios

~/GitHub/{personal,trabajo}/
~/Proyectos/
~/docs/legacy/
~/docker/{stacks/{ia,automation,monitoring},data,backups}/
~/yay-git/
## Servicios systemd activos

docker, containerd, NetworkManager, plasmalogin, wpa_supplicant

## Docker

docker 1:29.7.1-1, docker-compose 5.4.0-1, activo, sin contenedores todavía

## Historial

| Fecha | Qué | Comando |
|---|---|---|
| 2026-08-06 | Base + Docker | `pacman -S inetutils docker docker-compose git base-devel` |
