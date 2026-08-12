# Infraestructura de Madre

Madre es el ordenador principal de trabajo del ecosistema. Ejecuta Arch Linux
con KDE Plasma y será la máquina donde se reconstruirán los servicios Docker.

> Estado documentado: 2026-08-12  
> Fase actual: inventario y documentación, sin servicios de aplicación
> desplegados.

## Resumen actual

| Área | Estado |
|---|---|
| Sistema | Arch Linux rolling |
| Kernel | `7.1.5-arch1-2` |
| Hardware | ASUS PRIME B360M-A · Intel i5-8400 |
| Memoria | 15 GiB RAM · 4 GiB zram |
| Almacenamiento | WDC 931,5 GiB · `/` y `/home` en ext4 |
| Escritorio | KDE Plasma |
| Docker | Instalado, activo y vacío |
| Red | NetworkManager y Wi-Fi activos |
| Firewall | UFW activo, logging bajo |
| Tailscale | No instalado |
| Backups | Política definida, implementación pendiente |
| Repositorio de trabajo | `code-temple` |

## Archivos de esta carpeta

| Archivo | Contenido |
|---|---|
| [`estado.md`](./estado.md) | Resumen ejecutivo del estado de Madre y fase actual |
| [`hardware.md`](./hardware.md) | Placa base, procesador, memoria, discos, firmware y virtualización |
| [`sistema.md`](./sistema.md) | Arch Linux, kernel, usuario, particiones y montajes |
| [`software.md`](./software.md) | Herramientas instaladas, versiones y paquetes AUR |
| [`servicios.md`](./servicios.md) | Servicios systemd activos y servicios habilitados al arranque |
| [`docker.md`](./docker.md) | Estado de Docker, Compose, redes, imágenes, volúmenes y estructura prevista |
| [`repos.md`](./repos.md) | Repositorios locales, ubicación y responsabilidad de cada uno |
| [`estructura.md`](./estructura.md) | Organización de carpetas de Madre y tamaños conocidos |
| [`red.md`](./red.md) | NetworkManager, Wi-Fi, UFW y futuras decisiones de conectividad |
| [`backups.md`](./backups.md) | Datos prioritarios, espacio disponible y política futura de copias |
| [`cambios.md`](./cambios.md) | Historial de reinstalación, instalación y documentación |
| `paquetes-explicitos.txt` | Inventario generado con `pacman -Qqe` |

## Organización de responsabilidades

- `code-temple`: repositorio de trabajo e infraestructura; sustituye a
  `yggdrasil-dew`.
- `midgaror`: repositorio personal para vida, diarios y formación.
- `yggdrasil-dew`: repositorio histórico archivado; no se modifica.
- `docs/infra/madre/`: documentación de este equipo.
- `docs/infra/acer/`: documentación futura del portátil Acer.
- `~/docker/`: futura ubicación de stacks, datos y backups Docker.

## Estado de reconstrucción

Actualmente Madre solo contiene la base del sistema:

- Arch Linux recién instalado.
- KDE Plasma configurado.
- Git y GitHub CLI disponibles.
- Docker y Docker Compose instalados.
- UFW activo con política restrictiva.
- Sin contenedores, imágenes ni volúmenes Docker.
- Sin Tailscale ni servicios de aplicación.

## Operación y gobierno

- [`normas.md`](./normas.md) — Normas operativas específicas de Madre.
- [`auditoria.md`](./auditoria.md) — Checklist de auditoría de Madre.
- [`procedimientos.md`](./procedimientos.md) — Flujo general de cambios.
- [`adr/`](./adr/) — Decisiones de arquitectura de Madre.
- [`procedimientos/`](./procedimientos/) — Procedimientos concretos de Madre.


## Regla de actualización

Cada cambio real en Madre debe documentarse en el archivo correspondiente.

Después de instalar o eliminar software:

```bash
pacman -Qqe > docs/infra/madre/paquetes-explicitos.txt
git add docs/infra/madre
git commit -m "docs(infra): actualizar inventario de Madre"
git push origin main
```

No se almacenan aquí contraseñas, tokens, claves privadas ni archivos `.env`.

## Seguimiento de tareas pendientes

Las tareas abiertas de Madre se gestionan como issues en `code-temple`:
https://github.com/alvarofernandezmota-tech/code-temple/issues

## Historial de sesiones relacionadas

El detalle cronológico de las sesiones de trabajo sobre Madre vive en:
[docs/sesiones/](https://github.com/alvarofernandezmota-tech/code-temple/tree/main/docs/sesiones)
