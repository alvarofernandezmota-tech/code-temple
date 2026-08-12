# 🔧 HARDWARE - MADRE INFRASTRUCTURE

Última actualización: 2026-08-12

## 📋 Resumen

| Componente | Estado | Última Auditoría | Próxima Auditoría |
|------------|--------|------------------|-------------------|
| CPU | 🟢 OK | 2026-08-12 | 2026-09-12 |
| RAM | 🟢 OK | 2026-08-12 | 2026-09-12 |
| Disco | 🟢 OK | 2026-08-12 | 2026-09-12 |
| Red | 🟢 OK | 2026-08-12 | 2026-09-12 |
| GPU | 🟢 OK | 2026-08-12 | 2026-09-12 |

## 🖥️ CPU

### Especificaciones
- **Modelo:** AMD Ryzen 7 5800X
- **Cores:** 8
- **Threads:** 16
- **Estado:** 🟢 OK

### Auditorías
- [Issue #5 - Hardware](../issues/issue-05-hardware/)
- [outputs/cpu-info.txt](../issues/issue-05-hardware/outputs/cpu-info.txt)

### Comandos de Auditoría
```bash
lscpu
cat /proc/cpuinfo
```

## 💾 RAM

### Especificaciones
- **Total:** 32GB DDR4
- **Estado:** 🟢 OK

### Auditorías
- [Issue #5 - Hardware](../issues/issue-05-hardware/)
- [outputs/ram-info.txt](../issues/issue-05-hardware/outputs/ram-info.txt)

### Comandos de Auditoría
```bash
free -h
cat /proc/meminfo
```

## 💿 Disco

### Especificaciones
- **NVMe:** 1TB
- **HDD:** 2TB
- **Estado:** 🟢 OK

### Auditorías
- [Issue #5 - Hardware](../issues/issue-05-hardware/)
- [outputs/disk-info.txt](../issues/issue-05-hardware/outputs/disk-info.txt)

### Comandos de Auditoría
```bash
lsblk
df -h
```

## 🌐 Red

### Especificaciones
- **Interfaces:** 1x Ethernet, 1x WiFi
- **Estado:** 🟢 OK

### Auditorías
- [Issue #6 - Red](../issues/issue-06-red/)
- [outputs/interfaces.txt](../issues/issue-06-red/outputs/interfaces.txt)

### Comandos de Auditoría
```bash
ip addr show
ip route show
ss -tulpn
```

## 🎮 GPU

### Especificaciones
- **Estado:** 🟢 OK (integrada o dedicada según configuración)

### Auditorías
- [Issue #5 - Hardware](../issues/issue-05-hardware/)

### Comandos de Auditoría
```bash
lspci | grep -i vga
nvidia-smi  # Si es NVIDIA
```

## 📦 Paquetes Oficiales

Lista de paquetes explícitamente instalados y permitidos:

```bash
# Ver paquetes instalados
pacman -Qe

# Guardar lista oficial
pacman -Qe > paquetes-oficiales.txt
```

## 🔗 Links Útiles

- [README Principal](../README.md)
- [Estado](../estado.md)
- [Issue #5 - Hardware](../issues/issue-05-hardware/)
- [Issue #6 - Red](../issues/issue-06-red/)

---

**Responsable:** @alvarofernandezmota-tech
**Actualización:** Mensual (primer lunes de cada mes)

## Prueba de automatización
- Fecha: 2026-08-12

## Prueba de automatización con PAT
- Fecha: 2026-08-12

## Prueba 2 - 2026-08-12

## Prueba 3 - 2026-08-12
