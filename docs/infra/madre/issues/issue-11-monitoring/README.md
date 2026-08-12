# Issue #11 - Monitorización y alerting con métricas y dashboards

## Estado
🟡 En progreso

## Descripción
Documentar y configurar monitorización completa de Madre con métricas, alertas y dashboards.

## Progreso
- [ ] Documentar monitoring actual
- [ ] Definir métricas clave
- [ ] Configurar herramientas
- [ ] Configurar alertas

## Próximos Pasos
1. Listar métricas a trackear
2. Configurar monitoring
3. Crear dashboards

## Links
- [Issue #11](https://github.com/alvarofernandezmota-tech/code-temple/issues/11)
- [Issue #16](https://github.com/alvarofernandezmota-tech/code-temple/issues/16)
- [Issue #20](https://github.com/alvarofernandezmota-tech/code-temple/issues/20)

## Comandos Ejecutados

### 2026-08-12 - Auditoría de monitoring inicial
```bash
systemctl list-units | grep -iE "(prometheus|grafana|node|zabbix|nagios)"
ps aux | grep -iE "(prometheus|grafana|node|zabbix|nagios)"
```

**Outputs:**
- [`outputs/monitoring-services.txt`](outputs/monitoring-services.txt)
- [`outputs/monitoring-processes.txt`](outputs/monitoring-processes.txt)

## Próximos Pasos
1. Definir métricas a trackear
2. Configurar herramientas de monitoring
3. Crear dashboards
