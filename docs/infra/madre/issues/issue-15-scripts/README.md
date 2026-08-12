# Issue #15 - Scripts de Auditoría Automatizada

## Estado
🟢 Completado

## Descripción
Crear scripts automatizados para auditoría periódica de toda la infraestructura de Madre.

## Scripts Creados
- [x] audit-full.sh - Auditoría completa del sistema
- [x] health-check.sh - Health check rápido
- [x] checklist-verification.sh - Checklist de verificación

## Estructura

docs/infra/madre/scripts/audit/
├── audit-full.sh
├── health-check.sh
└── checklist-verification.sh

text

## Uso

### Auditoría completa
```bash
sudo ./docs/infra/madre/scripts/audit/audit-full.sh
```

### Health check rápido
```bash
./docs/infra/madre/scripts/audit/health-check.sh
```

### Checklist de verificación
```bash
sudo ./docs/infra/madre/scripts/audit/checklist-verification.sh
```

## Próximos Pasos
1. Configurar cron jobs para ejecución periódica
2. Documentar procedimientos de auditoría
3. Crear alertas basadas en los resultados

## Referencias
- [Issue #15](https://github.com/alvarofernandezmota-tech/code-temple/issues/15)
- [Issue #19 (Workflow)](https://github.com/alvarofernandezmota-tech/code-temple/issues/19)

## Automatización

### Instalar auditoría automática (diaria a las 3 AM)
```bash
sudo mkdir -p /var/log/madre-audit
sudo chmod 755 /var/log/madre-audit
sudo cp docs/infra/madre/scripts/audit/*.sh /usr/local/bin/
sudo chmod +x /usr/local/bin/*.sh
(crontab -l 2>/dev/null; echo "0 3 * * * /usr/local/bin/audit-full.sh") | crontab -
```

### Verificar cron jobs
```bash
crontab -l
```

### Ejecutar auditoría manual
```bash
sudo /usr/local/bin/audit-full.sh
```

### Ver logs de auditoría
```bash
ls -lah /var/log/madre-audit/
```
