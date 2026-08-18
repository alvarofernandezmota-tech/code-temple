# Modificar red o firewall

## Estado inicial

```bash
nmcli general status
nmcli device status
nmcli connection show
sudo ufw status verbose
sudo ufw show added
```

## Reglas

Antes de abrir un puerto se debe documentar:

- Servicio.
- Puerto.
- Protocolo.
- Red de origen.
- Motivo.
- Método de cierre.

## Validación

```bash
sudo ufw status numbered
ss -tulpn
nmcli device status
```

Actualizar `red.md` y `cambios.md`.

## Rollback

Eliminar la regla exacta usando su número:

```bash
sudo ufw status numbered
sudo ufw delete NUMERO
```
