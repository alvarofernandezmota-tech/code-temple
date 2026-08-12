# Issue #6 - Documentar red completa con comandos de diagnóstico

## Estado
🟡 En progreso

## Descripción
Documentar completamente la configuración de red de Madre con todos los detalles técnicos y comandos de auditoría.

## Progreso
- [ ] Ejecutar comandos de interfaces
- [ ] Ejecutar comandos de firewall
- [ ] Ejecutar comandos de puertos
- [ ] Crear diagrama de red
- [ ] Crear auditoría completa

## Próximos Pasos
1. Ejecutar `ip addr show` en Madre
2. Guardar output en `outputs/`
3. Documentar configuración

## Links
- [Issue #6](https://github.com/alvarofernandezmota-tech/code-temple/issues/6)
- [Issue #16](https://github.com/alvarofernandezmota-tech/code-temple/issues/16)
- [Issue #20](https://github.com/alvarofernandezmota-tech/code-temple/issues/20)

## Comandos Ejecutados

### 2026-08-12 - Auditoría de red inicial
```bash
ip addr show
ip route show
ss -tulpn
sudo ufw status verbose
```

**Outputs:**
- [`outputs/interfaces.txt`](outputs/interfaces.txt)
- [`outputs/routing.txt`](outputs/routing.txt)
- [`outputs/ports.txt`](outputs/ports.txt)
- [`outputs/firewall.txt`](outputs/firewall.txt)

## Próximos Pasos
1. Analizar configuración de red
2. Documentar firewall
3. Crear diagrama de red
