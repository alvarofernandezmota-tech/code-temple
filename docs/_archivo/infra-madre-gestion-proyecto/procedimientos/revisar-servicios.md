# Revisar servicios systemd

## Comprobación

```bash
systemctl list-units --type=service --state=running --no-pager
systemctl list-unit-files --type=service --state=enabled --no-pager
systemctl --failed --no-pager
```

## Para un servicio concreto

```bash
systemctl status nombre.service --no-pager
journalctl -u nombre.service -b --no-pager
```

## Documentación

Actualizar `servicios.md` y `cambios.md` si existe una diferencia respecto al
inventario anterior.

## Precaución

No habilitar, deshabilitar, iniciar o detener servicios sin conocer su función,
dependencias y procedimiento de reversión.
