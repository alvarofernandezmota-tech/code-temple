# Backups de Madre

> Última verificación: 2026-08-06

## Estado actual

Madre acaba de ser reinstalada y todavía no ejecuta servicios Docker
persistentes.

| Elemento | Tamaño aproximado | Estado |
|---|---:|---|
| `~/docker/` | 28 KiB | Estructura vacía |
| `code-temple` | 684 KiB | Repo activo |
| `midgaror` | 20 MiB | Repo personal activo |
| `yggdrasil-dew` | 3,6 MiB | Histórico archivado |
| `~/docs` | 12 KiB | Documentación local |

## Espacio disponible

| Montaje | Capacidad | Usado | Libre |
|---|---:|---:|---:|
| `/` | 49 GiB | 14 GiB | 34 GiB |
| `/home` | 866 GiB | 5,2 GiB | 817 GiB |

## Datos prioritarios

1. `code-temple`
2. `midgaror`
3. `~/docs`
4. Configuración de Madre que no contenga secretos
5. Datos persistentes de Docker cuando se instalen servicios

## Estado del backup

- Destino externo: pendiente.
- Segundo dispositivo: pendiente.
- Backup automático: no configurado.
- Prueba de restauración: pendiente.
- Cifrado: pendiente de decidir.

## Política futura

Se estudiará una estrategia 3-2-1:

- Tres copias de los datos importantes.
- Dos soportes diferentes.
- Una copia fuera de Madre.

Las copias que contengan datos personales o secretos deberán cifrarse.
No se copiarán tokens, claves privadas ni archivos `.env` sin un procedimiento
seguro y explícito.

## Cuando exista Docker

Se respaldarán:

- Archivos `compose.yaml` o `docker-compose.yml`.
- Archivos `.env.example`, nunca los `.env` reales.
- Volúmenes persistentes.
- Configuraciones de servicios.
- Dumps de bases de datos.
- Procedimientos de restauración.

La copia deberá probarse mediante una restauración real, no solo comprobando
que el archivo existe.
