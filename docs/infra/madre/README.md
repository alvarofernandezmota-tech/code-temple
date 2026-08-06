# docs/infra/madre/ — índice

Documentación completa del equipo Madre (Arch Linux, KDE Plasma), reinstalado
desde cero el 2026-08-06.

## Archivos de esta carpeta

| Archivo | Qué contiene |
|---|---|
| [`estado.md`](./estado.md) | Estado general: sistema base, disco, RAM, estructura de directorios, servicios systemd, Docker |
| [`paquetes-explicitos.txt`](./paquetes-explicitos.txt) | Lista completa de los 119 paquetes instalados explícitamente (`pacman -Qqe`) |

## Cómo mantener esto actualizado

Cada vez que instales algo nuevo en Madre, añade una fila a la tabla
"Historial de instalación" en `estado.md` y regenera el listado de paquetes:

```bash
pacman -Qqe > docs/infra/madre/paquetes-explicitos.txt
```
