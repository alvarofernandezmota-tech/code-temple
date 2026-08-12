# 🔒 SECURITY - MADRE INFRASTRUCTURE

Última actualización: 2026-08-12

## 📋 Resumen

| Componente | Estado | Última Auditoría | Próxima Auditoría |
|------------|--------|------------------|-------------------|
| Firewall | 🟢 OK | 2026-08-12 | 2026-09-12 |
| SSH | 🟢 OK | 2026-08-12 | 2026-09-12 |
| Usuarios | 🟢 OK | 2026-08-12 | 2026-09-12 |

## 🔥 Firewall

### Configuración
- **Firewall:** UFW activo
- **Estado:** 🟢 OK

### Auditorías
- [Issue #9 - Security](../issues/issue-09-security/)
- [outputs/firewall.txt](../issues/issue-09-security/outputs/firewall.txt)

## 🔑 SSH

### Configuración
- **Autenticación:** Key-based
- **Root login:** Deshabilitado
- **Estado:** 🟢 OK

### Auditorías
- [Issue #9 - Security](../issues/issue-09-security/)

## 👥 Usuarios

### Auditorías
- [Issue #9 - Security](../issues/issue-09-security/)
- [outputs/users.txt](../issues/issue-09-security/outputs/users.txt)
- [outputs/logins.txt](../issues/issue-09-security/outputs/logins.txt)

## 🔍 Comandos

```bash
sudo ufw status verbose
cat /etc/ssh/sshd_config
cat /etc/passwd
last
```

## 🔗 Links Útiles

- [README Principal](../README.md)
- [Estado](../estado.md)
- [Issue #9 - Security](../issues/issue-09-security/)

---

**Responsable:** @alvarofernandezmota-tech
**Actualización:** Mensual
