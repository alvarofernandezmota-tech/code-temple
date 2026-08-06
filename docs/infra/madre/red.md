# Red y firewall de Madre

## Red

- Gestor: NetworkManager
- Wi-Fi: `wpa_supplicant.service` activo
- Tailscale: todavía no instalado
- Puertos del ecosistema: ninguno publicado actualmente por Docker

## Firewall

- Firewall: UFW
- Estado: activo
- Arranque automático: habilitado
- Logging: activado en nivel bajo
- Política entrante: deny
- Política saliente: allow
- Política de tráfico reenviado: deny

## Pendiente

Registrar las reglas concretas con:

```bash
sudo ufw status numbered
```
