#!/bin/bash
# Checklist de verificación de Madre

echo "=== Checklist de Verificación ==="
echo ""

# CPU
echo "[ ] CPU usage < 80%"
top -bn1 | grep "Cpu(s)" | awk '{print $2}'

# RAM
echo "[ ] RAM usage < 85%"
free | grep Mem | awk '{print $3/$2 * 100.0}'

# Disco
echo "[ ] Disco usage < 80%"
df -h / | tail -1 | awk '{print $5}'

# Servicios críticos
echo "[ ] SSH activo"
systemctl is-active sshd

echo "[ ] Docker activo"
systemctl is-active docker

echo "[ ] Backups recientes"
ls -lt /backup/ 2>/dev/null | head -5

# Logs de error
echo "[ ] Sin errores críticos en logs"
journalctl -p 3 -xb --since "24 hours ago" 2>/dev/null | wc -l

echo ""
echo "Verificación completada"
