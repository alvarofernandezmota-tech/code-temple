# 📖 PROCEDIMIENTOS - MADRE INFRASTRUCTURE

Última actualización: 2026-08-12

## 📋 Índice

- [Auditorías](auditorias.md) - Procedimiento de auditorías
- [Updates](updates.md) - Procedimiento de actualizaciones
- [Rollback](rollback.md) - Procedimiento de rollback

## 🔍 Auditorías

### Auditoría Completa
```bash
sudo /usr/local/bin/audit-full.sh
```

### Health Check
```bash
/usr/local/bin/health-check.sh
```

### Checklist
```bash
sudo /usr/local/bin/checklist-verification.sh
```

### Ver Logs
```bash
ls -lah /var/log/madre-audit/
```

## 🔄 Updates

### Actualizar Sistema
```bash
sudo pacman -Syu
```

### Ver Paquetes Instalados
```bash
pacman -Qe
```

## ↩️ Rollback

### Restaurar Paquetes
```bash
# Restaurar desde lista
sudo pacman -S - < paquetes-backup.txt
```

## 🔗 Links Útiles

- [README Principal](../README.md)
- [Estado](../estado.md)
- [Scripts](../scripts/)

---

**Responsable:** @alvarofernandezmota-tech
**Actualización:** Con cada cambio de procedimientos
