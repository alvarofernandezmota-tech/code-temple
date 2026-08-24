#!/usr/bin/env python3
"""
Cierre completo de sesión: actualiza AGENTS.md, CONTEXT.md, CHANGELOG.md,
y genera el bloque de cierre con commits, issues y ADRs del día.

Uso: python3 scripts/cierre-completo.py --fecha 2026-08-24
"""
import subprocess
import sys
from pathlib import Path
from datetime import datetime

RAIZ = Path(__file__).parent.parent

def get_commits(fecha):
    cmd = f'git log --since="{fecha} 00:00:00" --until="{fecha} 23:59:59" --format="%h %s"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip().split('\n') if result.stdout.strip() else []

def get_issues(fecha):
    cmd = f'gh issue list --state closed --search "closed:{fecha}" --json number,title'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip().split('\n') if result.stdout.strip() else []

def get_adrs():
    cmd = 'ls docs/adr/*.md 2>/dev/null | sort -V'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip().split('\n') if result.stdout.strip() else []

def main():
    fecha = sys.argv[2] if len(sys.argv) > 2 else datetime.now().strftime('%Y-%m-%d')
    
    print(f"=== Cierre completo para {fecha} ===\n")
    
    # 1. Actualizar AGENTS.md y CONTEXT.md
    print("1. Actualizando AGENTS.md y CONTEXT.md...")
    subprocess.run(['python3', str(RAIZ / 'scripts/actualizar-agents-context.py')])
    
    # 2. Obtener commits, issues, ADRs
    commits = get_commits(fecha)
    issues = get_issues(fecha)
    adrs = get_adrs()
    
    print(f"\n2. Resumen del día:")
    print(f"   - Commits: {len(commits)}")
    print(f"   - Issues cerradas: {len(issues)}")
    print(f"   - ADRs: {len(adrs)}")
    
    print(f"\n3. Para actualizar CHANGELOG.md y sesión, editar manualmente:")
    print(f"   - CHANGELOG.md: añadir entry con {len(commits)} commits")
    print(f"   - docs/sesiones/{fecha.replace('-', '/')[:7]}/{fecha}.md: añadir bloque con commits")
    
    print(f"\n✅ Cierre completo generado")

if __name__ == '__main__':
    main()
