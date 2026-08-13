# validate-structure.py

**Descripción:** Valida estructura de Madre

**Uso:**
```bash
cd docs/infra/madre
python3 scripts/validate-structure.py
```

**Funciones:**
- Verifica que todas las carpetas tengan README.md
- Verifica que no haya archivos sueltos en la raíz
- Reporta errores y advertencias
- Valida estructura esperada

**Carpetas esperadas:**
- python, sesiones, adr, security, red, performance
- automatizaciones, backups, change-management, disaster-recovery
- hardware, issues, monitoring, procedimientos, scripts, scriptscd, servicios

**Referencias:**
- [Scripts](README.md)
- [Madre](../README.md)
