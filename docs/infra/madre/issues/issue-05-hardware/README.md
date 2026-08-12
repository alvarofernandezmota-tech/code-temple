# Issue #5 - Documentar hardware completo con comandos de auditoría

## Estado
🟡 En progreso

## Descripción
Documentar TODO el hardware de Madre con especificaciones técnicas completas y comandos para auditoría periódica.

## Progreso
- [ ] Ejecutar comandos de CPU
- [ ] Ejecutar comandos de RAM
- [ ] Ejecutar comandos de disco
- [ ] Ejecutar comandos de red
- [ ] Crear auditoría completa
- [ ] Actualizar hardware.md

## Próximos Pasos
1. Ejecutar `lscpu -e` en Madre
2. Guardar output en `outputs/`
3. Crear auditoría en `audit/`

## Links
- [Issue #5](https://github.com/alvarofernandezmota-tech/code-temple/issues/5)
- [Issue #16](https://github.com/alvarofernandezmota-tech/code-temple/issues/16)
- [Issue #20](https://github.com/alvarofernandezmota-tech/code-temple/issues/20)

## Comandos Ejecutados

### 2026-08-12 - Auditoría de hardware inicial
```bash
lscpu -e
cat /proc/cpuinfo
sudo dmidecode -t memory
free -h
lsblk -o NAME,MODEL,SERIAL,SIZE,TYPE,MOUNTPOINT
sudo fdisk -l
```

**Outputs:**
- [`outputs/2026-08-12-hardware/cpu-info.txt`](outputs/cpu-info.txt)
- [`outputs/2026-08-12-hardware/cpu-detailed.txt`](outputs/cpu-detailed.txt)
- [`outputs/2026-08-12-hardware/ram-info.txt`](outputs/ram-info.txt)
- [`outputs/2026-08-12-hardware/ram-summary.txt`](outputs/ram-summary.txt)
- [`outputs/2026-08-12-hardware/disk-info.txt`](outputs/disk-info.txt)
- [`outputs/2026-08-12-hardware/disk-partitions.txt`](outputs/disk-partitions.txt)

**Notas:**
- Auditoría inicial completada
- Pendiente analizar outputs y crear auditoría formal

## Auditorías
- [ ] Crear auditoría formal en `audit/2026-08-12-hardware-audit.md`

## Próximos Pasos
1. Analizar outputs de CPU
2. Analizar outputs de RAM
3. Analizar outputs de disco
4. Crear auditoría formal
5. Actualizar hardware.md
