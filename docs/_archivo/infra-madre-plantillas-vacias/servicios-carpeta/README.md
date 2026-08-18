# ⚙️ SERVICIOS - MADRE INFRASTRUCTURE

Última actualización: 2026-08-12

## 📋 Resumen

| Componente | Estado | Última Auditoría | Próxima Auditoría |
|------------|--------|------------------|-------------------|
| Servicios Críticos | 🟢 OK | 2026-08-12 | 2026-09-12 |
| Servicios Fallidos | 🟢 0 | 2026-08-12 | 2026-09-12 |

## 🔑 Servicios Críticos

### SSH
- **Estado:** 🟢 Activo
- **Puerto:** 22
- **Descripción:** Acceso remoto seguro

### Docker
- **Estado:** 🟢 Activo
- **Puerto:** 2375-2376
- **Descripción:** Contenerización

### Tailscale
- **Estado:** 🟢 Activo
- **Puerto:** 41641
- **Descripción:** VPN mesh

## 📊 Auditorías

- [Issue #7 - Servicios](../issues/issue-07-servicios/)
- [outputs/running.txt](../issues/issue-07-servicios/outputs/running.txt)
- [outputs/enabled.txt](../issues/issue-07-servicios/outputs/enabled.txt)
- [outputs/failed.txt](../issues/issue-07-servicios/outputs/failed.txt)

## 🔍 Comandos

```bash
systemctl list-units --type=service --state=running
systemctl list-unit-files --type=service --state=enabled
systemctl --failed
```

## 🔗 Links Útiles

- [README Principal](../README.md)
- [Estado](../estado.md)
- [Issue #7 - Servicios](../issues/issue-07-servicios/)

---

**Responsable:** @alvarofernandezmota-tech
**Actualización:** Mensual
