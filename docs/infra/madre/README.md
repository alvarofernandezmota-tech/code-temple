# Infraestructura de Madre

Madre es el ordenador principal del ecosistema. Ejecuta Arch Linux con KDE
Plasma y será la máquina donde se reconstruirán los servicios Docker.

## Archivos

| Archivo | Contenido |
|---|---|
| `estado.md` | Resumen general del estado actual |
| `hardware.md` | Placa, CPU, memoria, discos y firmware |
| `sistema.md` | Arch Linux, kernel, particiones y montajes |
| `software.md` | Herramientas y versiones instaladas |
| `servicios.md` | Servicios systemd activos y habilitados |
| `docker.md` | Estado de Docker, redes, imágenes y volúmenes |
| `repos.md` | Repositorios Git locales y su función |
| `estructura.md` | Organización de carpetas de Madre |
| `red.md` | NetworkManager, UFW y estado de red |
| `backups.md` | Estado y futura estrategia de copias |
| `cambios.md` | Historial de reconstrucción de Madre |
| `paquetes-explicitos.txt` | Salida de `pacman -Qqe` |

## Regla de actualización

Después de instalar o eliminar software:

```bash
pacman -Qqe > docs/infra/madre/paquetes-explicitos.txt
git add docs/infra/madre
git commit -m "docs(infra): actualizar inventario de Madre"
git push origin main
```
