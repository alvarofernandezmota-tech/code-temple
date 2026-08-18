# Backups de Madre

## Antes de definir una copia

Identificar:

- Datos críticos.
- Configuraciones necesarias.
- Volúmenes Docker.
- Repositorios locales.
- Destino.
- Cifrado.
- Retención.
- Prueba de restauración.

## Comprobación

```bash
df -h
du -sh ~/GitHub ~/docker 2>/dev/null
```

## Documentación

Actualizar `backups.md` con la política vigente y `cambios.md` con cada cambio.

Nunca almacenar en el repositorio copias que contengan secretos sin un
procedimiento explícito de cifrado.
