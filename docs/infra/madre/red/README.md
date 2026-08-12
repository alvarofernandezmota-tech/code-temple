# 🌐 RED - MADRE INFRASTRUCTURE

Última actualización: 2026-08-12

## 📋 Resumen

| Componente | Estado | Última Auditoría | Próxima Auditoría |
|------------|--------|------------------|-------------------|
| Interfaces | 🟢 OK | 2026-08-12 | 2026-09-12 |
| Firewall | 🟢 OK | 2026-08-12 | 2026-09-12 |
| Puertos | 🟢 OK | 2026-08-12 | 2026-09-12 |
| DNS | 🟢 OK | 2026-08-12 | 2026-09-12 |

## 🔌 Interfaces

### Configuración
- **Ethernet:** 1x
- **WiFi:** 1x
- **Estado:** 🟢 OK

### Auditorías
- [Issue #6 - Red](../issues/issue-06-red/)
- [outputs/interfaces.txt](../issues/issue-06-red/outputs/interfaces.txt)

### Comandos
```bash
ip addr show
ip route show
```

## 🔥 Firewall

### Configuración
- **Firewall:** UFW
- **Estado:** Activo
- **Estado:** 🟢 OK

### Auditorías
- [Issue #6 - Red](../issues/issue-06-red/)
- [outputs/firewall.txt](../issues/issue-06-red/outputs/firewall.txt)

### Comandos
```bash
sudo ufw status verbose
sudo iptables -L -n -v
```

## 🔌 Puertos

### Puertos Abiertos
- **22:** SSH
- **443:** HTTPS

### Auditorías
- [Issue #6 - Red](../issues/issue-06-red/)
- [outputs/ports.txt](../issues/issue-06-red/outputs/ports.txt)

### Comandos
```bash
ss -tulpn
sudo netstat -tulpn
```

## 🌐 DNS

### Configuración
- **DNS:** Configurado
- **Estado:** 🟢 OK

### Comandos
```bash
cat /etc/resolv.conf
nmcli dev show | grep DNS
```

## 🔗 Links Útiles

- [README Principal](../README.md)
- [Estado](../estado.md)
- [Issue #6 - Red](../issues/issue-06-red/)

---

**Responsable:** @alvarofernandezmota-tech
**Actualización:** Mensual
