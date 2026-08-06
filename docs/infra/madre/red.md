# Red y firewall de Madre

> Última verificación: 2026-08-06

## Red

- Gestor de red: NetworkManager
- Wi-Fi: `wpa_supplicant.service` activo
- Tailscale: no instalado
- Contenedores Docker expuestos: ninguno
- Puertos del ecosistema publicados: ninguno

## Firewall

- Firewall: UFW
- Estado: activo
- Servicio: habilitado y activo
- Logging: activo, nivel bajo
- Política entrante por defecto: `deny`
- Política saliente por defecto: `allow`
- Política de tráfico reenviado: `deny`

## Reglas explícitas

La auditoría con:

```bash
sudo ufw status numbered
```

devuelve `Status: active` sin mostrar reglas numeradas. Actualmente no hay
reglas explícitas añadidas mediante UFW.

## Comprobaciones utilizadas

```bash
sudo ufw status verbose
sudo ufw status numbered
systemctl is-active ufw
systemctl is-enabled ufw
```

## Pendiente

Antes de instalar servicios, registrar cualquier regla nueva indicando:

- Puerto o servicio.
- Protocolo.
- Dirección del tráfico.
- Motivo.
- Fecha.
- Servicio que la necesita.

Tailscale se estudiará posteriormente y no forma parte de esta instalación base.
