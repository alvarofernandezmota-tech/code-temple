#!/usr/bin/env python3
"""
Cerrar sesión: genera automáticamente la sección de cierre de sesión.

Lee commits, issues y ADRs de hoy, y genera el bloque de "Cierre de sesión"
formateado para añadir al final de docs/sesiones/YYYY/MM-mes/YYYY-MM-DD.md.

Uso:
    python scripts/cerrar-sesion.py [--fecha YYYY-MM-DD]
"""

import subprocess
import sys
from datetime import datetime

def get_commits_today(fecha):
    """Obtener commits de hoy (o fecha especificada)."""
    cmd = f'git log --since="{fecha} 00:00:00" --until="{fecha} 23:59:59" --format="%h %s"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    commits = result.stdout.strip().split('\n') if result.stdout.strip() else []
    return commits

def get_issues_closed_today(fecha):
    """Obtener issues cerradas hoy con gh CLI."""
    cmd = f'gh issue list --state closed --search "closed:{fecha}" --json number,title --template \'{{{{range .}}{{{{.number}}}}: {{{{.title}}}}\\n{{{{end}}}}\''
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    issues = result.stdout.strip().split('\n') if result.stdout.strip() else []
    return issues

def get_adrs():
    """Obtener lista de ADRs."""
    cmd = 'ls docs/adr/*.md | sort -V'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    adrs = result.stdout.strip().split('\n') if result.stdout.strip() else []
    return adrs

def generate_cierre(fecha, commits, issues, adrs):
    """Generar bloque de cierre de sesión."""
    bloque = f"""
---

## Cierre de sesión (generado automáticamente)

### Fechas y duración
- **Fecha:** {fecha}
- **Inicio:** {datetime.now().strftime('%H:%M')} CEST (aproximado, primer commit: {commits[0].split()[0] if commits else 'N/A'})
- **Fin:** {datetime.now().strftime('%H:%M')} CEST (último commit: {commits[-1].split()[0] if commits else 'N/A'})
- **Duración:** ~X horas (ajustar manualmente)

### Resumen ejecutivo
Sesión de trabajo en code-temple. Se cerraron {len(issues)} issues, se trabajó en {len(adrs)} ADRs, y se realizaron {len(commits)} commits.

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
2. [ ] Completar resumen ejecutivo con más detalle
3. [ ] Añadir próximos pasos específicos

---

**Fin de sesión {fecha}**
"""
    return bloque

def main():
    fecha = datetime.now().strftime('%Y-%m-%d')
    if len(sys.argv) > 1 and sys.argv[1] == '--fecha':
        fecha = sys.argv[2]
    
    print(f"Generando cierre de sesión para {fecha}...")
    
    commits = get_commits_today(fecha)
    issues = get_issues_closed_today(fecha)
    adrs = get_adrs()
    
    cierre = generate_cierre(fecha, commits, issues, adrs)
    
    print(cierre)
    print("\n---\n")
    print("Para añadir al final de docs/sesiones/YYYY/MM-mes/YYYY-MM-DD.md:")
    print(f"    echo '{cierre}' >> docs/sesiones/{fecha.replace('-', '/')[:7]}/{fecha}.md")

if __name__ == '__main__':
    main()
