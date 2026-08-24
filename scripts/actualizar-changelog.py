#!/usr/bin/env python3
"""
Actualiza CHANGELOG.md con entry automático del día.

Uso: python3 scripts/actualizar-changelog.py [--fecha YYYY-MM-DD] [--titulo "Titulo opcional"]
"""
import subprocess
import sys
from pathlib import Path
from datetime import datetime

RAIZ = Path(__file__).parent.parent

def get_commits(fecha):
    cmd = f'git log --since="{fecha} 00:00:00" --until="{fecha} 23:59:59" --format="- %s"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip().split('\n') if result.stdout.strip() else []

def main():
    fecha = sys.argv[2] if len(sys.argv) > 2 else datetime.now().strftime('%Y-%m-%d')
    titulo = sys.argv[4] if len(sys.argv) > 4 else "Cambios del día"
    
    commits = get_commits(fecha)
    
    entry = f"""
## [{fecha}] - {fecha}

### {titulo}

"""
    for commit in commits:
        entry += f"{commit}\n"
    
    changelog = RAIZ / 'CHANGELOG.md'
    contenido = changelog.read_text(encoding='utf-8')
    
    # Insertar después del título "# CHANGELOG"
    lines = contenido.split('\n')
    lines.insert(2, entry)  # Después de la línea 2
    
    changelog.write_text('\n'.join(lines), encoding='utf-8')
    print(f"✅ CHANGELOG.md actualizado con {len(commits)} commits")

if __name__ == '__main__':
    main()
