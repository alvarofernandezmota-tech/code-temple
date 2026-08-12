# 💾 BACKUPS - MADRE INFRASTRUCTURE

Última actualización: 2026-08-12

## 📋 Resumen

| Componente | Estado | Última Auditoría | Próxima Auditoría |
|------------|--------|------------------|-------------------|
| Estrategia | 🟢 OK | 2026-08-12 | 2026-09-12 |
| Restore | 🟡 PENDIENTE | - | 2026-09-12 |
| Testing | 🟡 PENDIENTE | - | 2026-09-12 |

## 📊 Estrategia de Backups

### Regla 3-2-1
- **3 copias** de los datos (original + 2 backups)
- **2 medios diferentes** (local + externo)
- **1 copia fuera del sitio** (off-site)

### Backups implementados
- **Código:** Git (code-temple, yggdrasil-dew, midgaror)
- **Configuraciones:** Scripts de backup en Madre
- **Frecuencia:** Diaria (cron jobs)

## 📝 Procedimientos

### Backup de código
```bash
# Git ya gestiona versiones
git push origin main
```

### Backup de configuraciones
```bash
# Backup de configs del sistema
tar -czf system-config-$(date +%Y%m%d).tar.gz \
  /etc/ \
  /var/lib/systemd/ \
  /root/ \
  /home/
```

## 🔍 Auditorías

- [Issue #8 - Backups](../issues/issue-08-backups/)
- [outputs/backup-dir.txt](../issues/issue-08-backups/outputs/backup-dir.txt)
- [outputs/backup-space.txt](../issues/issue-08-backups/outputs/backup-space.txt)

## 📝 Próximos Pasos

1. ✅ Documentar estrategia de backups
2. 🟡 Crear procedimientos de restore
3. 🟡 Testear restore
4. 🟡 Documentar RTO/RPO

## 🔗 Links Útiles

- [README Principal](../README.md)
- [Estado](../estado.md)
- [Issue #8 - Backups](../issues/issue-08-backups/)

---

**Responsable:** @alvarofernandezmota-tech
**Actualización:** Semanal
