#!/usr/bin/env python3
"""
Cerrar sesión: genera automáticamente la sección de cierre de sesión.
"""

import subprocess
import sys
from datetime import datetime

def get_commits_today(fecha):
    cmd = f'git log --since="{fecha} 00:00:00" --until="{fecha} 23:59:59" --format="%h %s"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    commits = result.stdout.strip().split('\n') if result.stdout.strip() else []
    return commits

def get_issues_closed_today(fecha):
    cmd = f'gh issue list --state closed --search "closed:{fecha}" --json number,title --template "{{{{range .}}{{{{.number}}}}: {{{{.title}}}}\\n{{{{end}}}}"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    issues = result.stdout.strip().split('\n') if result.stdout.strip() else []
    return issues

def get_adrs():
    cmd = 'ls docs/adr/*.md | sort -V'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    adrs = result.stdout.strip().split('\n') if result.stdout.strip() else []
    return adrs

def generate_cierre(fecha, commits, issues, adrs):
    bloque = f"""
---

## Cierre de sesión (generado automáticamente)

### Fechas y duración
- **Fecha:** {fecha}
- **Inicio:** {datetime.now().strftime('%H:%M')} CEST
- **Fin:** {datetime.now().strftime('%H:%M')} CEST
- **Duración:** ~X horas (ajustar manualmente)

### Resumen ejecutivo
Sesión de trabajo en code-temple. Se cerraron {len(issues)} issues, {len(adrs)} ADRs, {len(commits)} commits.

### Commits de la sesión ({len(commits)} commits)

"""
    for i, commit in enumerate(commits, 1):
        bloque += f"{i}. `{commit}`\n"
    
    bloque += f"""
### Issues cerradas ({len(issues)} issues)

"""
    for issue in issues:
        bloque += f"- {issue}\n"
    
    bloque += f"""
### ADRs ({len(adrs)} ADRs)

"""
    for adr in adrs:
        bloque += f"- {adr}\n"
    
    bloque += """
### Próximos pasos
1. [ ] Revisar y ajustar duración exacta
2. [ ] Completar resumen ejecutivo
3. [ ] Añadir próximos pasos específicos

---

**Fin de sesión {fecha}**
"""
    return bloque

def main():
    fecha = datetime.now().strftime('%Y-%m-%d')
    if len(sys.argv) > 1 and sys.argv[1] == '--fecha':
        fecha = sys.argv[2]
    
    print(f"Generando cierre para {fecha}...")
    
    commits = get_commits_today(fecha)
    issues = get_issues_closed_today(fecha)
    adrs = get_adrs()
    
    cierre = generate_cierre(fecha, commits, issues, adrs)
    
    print(cierre)

if __name__ == '__main__':
    main()
