#!/bin/bash
# Auditoría completa de Madre

DATE=$(date +%Y%m%d_%H%M%S)
AUDIT_DIR="/var/log/madre-audit/$DATE"

mkdir -p $AUDIT_DIR

# Sistema
echo "=== System Info ===" > $AUDIT_DIR/system.txt
hostnamectl >> $AUDIT_DIR/system.txt
uname -a >> $AUDIT_DIR/system.txt
cat /etc/os-release >> $AUDIT_DIR/system.txt

# Hardware
echo "=== Hardware ===" > $AUDIT_DIR/hardware.txt
lscpu >> $AUDIT_DIR/hardware.txt
free -h >> $AUDIT_DIR/hardware.txt
lsblk >> $AUDIT_DIR/hardware.txt

# Red
echo "=== Network ===" > $AUDIT_DIR/network.txt
ip addr show >> $AUDIT_DIR/network.txt
ip route show >> $AUDIT_DIR/network.txt
ss -tulpn >> $AUDIT_DIR/network.txt

# Servicios
echo "=== Services ===" > $AUDIT_DIR/services.txt
systemctl list-units --type=service --state=running >> $AUDIT_DIR/services.txt

# Seguridad
echo "=== Security ===" > $AUDIT_DIR/security.txt
last >> $AUDIT_DIR/security.txt
iptables -L -n >> $AUDIT_DIR/security.txt 2>&1

# Backups
echo "=== Backups ===" > $AUDIT_DIR/backups.txt
ls -lah /backup/ >> $AUDIT_DIR/backups.txt 2>&1

echo "Auditoría completada en $AUDIT_DIR"
