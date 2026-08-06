# Madre — infraestructura completa

> Sistema reinstalado 2026-08-06 con Arch Linux puro. Reconstrucción desde cero.

## Sistema base

- OS: [pendiente: `cat /etc/os-release`]
- Kernel: [pendiente: `uname -r`]
- Hostname: [pendiente: `hostname`]
- Disco: /dev/sda2 (root, 49G) · /dev/sda3 (/home, 866G)
- RAM: 15Gi total

## Paquetes instalados

(lista de `pacman -Q` relevante — se actualiza según se instale)

## Estructura de directorios

(árbol real de /home y configuración — se documenta a medida que se crea)

## Servicios / Docker

(vacío — a reconstruir; el stack anterior de 23 contenedores ya no existe)

## Historial de instalación

| Fecha | Qué se instaló | Comando |
|---|---|---|
| 2026-08-06 | Base + Docker | `pacman -S inetutils docker docker-compose git base-devel` |
