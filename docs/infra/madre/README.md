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
- `~/docker/`: ubicación actual de stacks, datos y backups Docker.

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

## Mantenimiento y referencias

El procedimiento para actualizar esta carpeta está en
[`procedimientos/actualizar-documentacion.md`](./procedimientos/actualizar-documentacion.md).

Las decisiones de arquitectura están en [`adr/`](./adr/). La decisión sobre la
ruta canónica de `code-temple` está documentada en
[`adr/ADR-003-ruta-canonica-code-temple.md`](./adr/ADR-003-ruta-canonica-code-temple.md).

Las tareas pendientes se gestionan mediante los
[issues abiertos de code-temple](https://github.com/alvarofernandezmota-tech/code-temple/issues).

El historial cronológico de las sesiones se conserva fuera de esta carpeta, en
[`docs/sesiones/`](../../sesiones/).

## Estructura de Issues

La documentación detallada de cada área se encuentra en el directorio [`issues/`](issues/):

- [`issues/issue-05-hardware/`](issues/issue-05-hardware/) - Hardware completo
- [`issues/issue-06-red/`](issues/issue-06-red/) - Red y firewall
- [`issues/issue-07-servicios/`](issues/issue-07-servicios/) - Servicios del sistema
- [`issues/issue-08-backups/`](issues/issue-08-backups/) - Estrategia de backups
- [`issues/issue-09-security/`](issues/issue-09-security/) - Security hardening
- [`issues/issue-10-disaster-recovery/`](issues/issue-10-disaster-recovery/) - Disaster recovery
- [`issues/issue-11-monitoring/`](issues/issue-11-monitoring/) - Monitorización
- [`issues/issue-12-performance/`](issues/issue-12-performance/) - Performance baseline
- [`issues/issue-13-change-management/`](issues/issue-13-change-management/) - Change management
- [`issues/issue-14-adr/`](issues/issue-14-adr/) - Architecture Decision Records
- [`issues/issue-15-scripts/`](issues/issue-15-scripts/) - Scripts de auditoría

Ver [`issues/README.md`](issues/README.md) para más detalles.
