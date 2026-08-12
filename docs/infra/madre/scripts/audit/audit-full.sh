#!/bin/bash
# Script de auditoría completa de Madre

DATE=$(date +%Y%m%d_%H%M%S)
AUDIT_DIR="/var/log/madre-audit/$DATE"

echo "=== Iniciando auditoría de Madre ==="
echo "Fecha: $(date)"
echo "Hostname: $(hostname)"
echo ""

mkdir -p $AUDIT_DIR

# Sistema
echo "[1/10] Auditoría de sistema..."
echo "=== System Info ===" > $AUDIT_DIR/system.txt
hostnamectl >> $AUDIT_DIR/system.txt
uname -a >> $AUDIT_DIR/system.txt
cat /etc/os-release >> $AUDIT_DIR/system.txt

# Hardware
echo "[2/10] Auditoría de hardware..."
echo "=== Hardware ===" > $AUDIT_DIR/hardware.txt
lscpu >> $AUDIT_DIR/hardware.txt
free -h >> $AUDIT_DIR/hardware.txt
lsblk >> $AUDIT_DIR/hardware.txt

# Red
echo "[3/10] Auditoría de red..."
echo "=== Network ===" > $AUDIT_DIR/network.txt
ip addr show >> $AUDIT_DIR/network.txt
ip route show >> $AUDIT_DIR/network.txt
ss -tulpn >> $AUDIT_DIR/network.txt

# Servicios
echo "[4/10] Auditoría de servicios..."
echo "=== Services ===" > $AUDIT_DIR/services.txt
systemctl list-units --type=service --state=running >> $AUDIT_DIR/services.txt

# Seguridad
echo "[5/10] Auditoría de seguridad..."
echo "=== Security ===" > $AUDIT_DIR/security.txt
last >> $AUDIT_DIR/security.txt
sudo iptables -L -n >> $AUDIT_DIR/security.txt 2>&1

# Backups
echo "[6/10] Auditoría de backups..."
echo "=== Backups ===" > $AUDIT_DIR/backups.txt
ls -lah /backup/ >> $AUDIT_DIR/backups.txt 2>&1

# Logs
echo "[7/10] Auditoría de logs..."
echo "=== Logs ===" > $AUDIT_DIR/logs.txt
journalctl -p 3 -xb --since "24 hours ago" >> $AUDIT_DIR/logs.txt 2>&1

# Performance
echo "[8/10] Auditoría de performance..."
echo "=== Performance ===" > $AUDIT_DIR/performance.txt
uptime >> $AUDIT_DIR/performance.txt
vmstat 1 5 >> $AUDIT_DIR/performance.txt

# Disk
echo "[9/10] Auditoría de disco..."
echo "=== Disk ===" > $AUDIT_DIR/disk.txt
df -h >> $AUDIT_DIR/disk.txt
iostat -x 1 5 >> $AUDIT_DIR/disk.txt 2>&1

# Users
echo "[10/10] Auditoría de usuarios..."
echo "=== Users ===" > $AUDIT_DIR/users.txt
last >> $AUDIT_DIR/users.txt
who >> $AUDIT_DIR/users.txt

echo ""
echo "=== Auditoría completada ==="
echo "Directorio: $AUDIT_DIR"
echo ""
echo "Archivos creados:"
ls -lah $AUDIT_DIR
