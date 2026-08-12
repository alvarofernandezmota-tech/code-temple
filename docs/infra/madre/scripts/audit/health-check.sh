#!/bin/bash
# Health check rápido de Madre

echo "=== Health Check ==="
echo "Hostname: $(hostname)"
echo "Uptime: $(uptime -p)"
echo ""

# Load average
echo "Load Average: $(cat /proc/loadavg)"
echo ""

# Disk
echo "Disk Usage:"
df -h / | tail -1
echo ""

# Memory
echo "Memory Usage:"
free -h | grep Mem
echo ""

# Critical services
echo "Services:"
for service in ssh docker tailscaled; do
  status=$(systemctl is-active $service 2>/dev/null || echo "not installed")
  echo "  $service: $status"
done
echo ""

echo "Health check completado"
