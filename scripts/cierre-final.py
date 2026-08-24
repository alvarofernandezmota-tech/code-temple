#!/usr/bin/env python3
"""
Cierre final de sesión: actualiza automáticamente el archivo de sesión con horas reales.

Uso: python3 scripts/cierre-final.py --fecha 2026-08-24
"""
import subprocess
import sys
from pathlib import Path
from datetime import datetime
import re

RAIZ = Path(__file__).parent.parent

def get_commits(fecha):
    cmd = f'git log --since="{fecha} 00:00:00" --until="{fecha} 23:59:59" --format="%h %ai %s"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    lines = result.stdout.strip().split('\n') if result.stdout.strip() else []
    return lines

def get_horas(fecha):
    commits = get_commits(fecha)
    if not commits:
        return None, None, "0 minutos"
    
    primer = commits[-1].split()[1:3]  # 2026-08-24 16:04:36 +0200
    ultimo = commits[0].split()[1:3]   # 2026-08-24 18:38:XX +0200
    
    # Calcular duración
    h1, m1 = int(primer[1].split(':')[0]), int(primer[1].split(':')[1])
    h2, m2 = int(ultimo[1].split(':')[0]), int(ultimo[1].split(':')[1])
    
    duracion_min = (h2 * 60 + m2) - (h1 * 60 + m1)
    horas = duracion_min // 60
    mins = duracion_min % 60
    
    if horas > 0:
        duracion_str = f"{horas} hora{'s' if horas > 1 else ''} {mins} minutos"
    else:
        duracion_str = f"{mins} minutos"
    
    return f"{primer[0]} {primer[1][:5]} CEST", f"{ultimo[0]} {ultimo[1][:5]} CEST", duracion_str

def actualizar_sesion(fecha, inicio, fin, duracion):
    archivo = RAIZ / f'docs/sesiones/{fecha[:7].replace("-", "/")}/{fecha}.md'
    if not archivo.exists():
        print(f"❌ No existe {archivo}")
        return False
    
    contenido = archivo.read_text(encoding='utf-8')
    
    # Actualizar horas
    contenido = re.sub(
        r'Inicio:\*\* \d{4}-\d{2}-\d{2} [\d:]+ CEST',
        f'Inicio:** {inicio}',
        contenido
    )
    contenido = re.sub(
        r'Fin:\*\* \d{4}-\d{2}-\d{2} [\d:]+ CEST',
        f'Fin:** {fin}',
        contenido
    )
    contenido = re.sub(
        r'Duración total:\*\* .+',
        f'Duración total:** {duracion}',
        contenido
    )
    
    archivo.write_text(contenido, encoding='utf-8')
    print(f"✅ {archivo.name} actualizado")
    return True

def main():
    fecha = sys.argv[2] if len(sys.argv) > 2 else datetime.now().strftime('%Y-%m-%d')
    
    print(f"🔍 Cierre final para {fecha}...\n")
    
    commits = get_commits(fecha)
    if not commits:
        print(f"❌ No hay commits para {fecha}")
        return
    
    inicio, fin, duracion = get_horas(fecha)
    
    print(f"📅 Primer commit: {inicio}")
    print(f"📅 Último commit: {fin}")
    print(f"⏱️  Duración: {duracion}")
    print(f"📝 Total commits: {len(commits)}\n")
    
    if actualizar_sesion(fecha, inicio, fin, duracion):
        print(f"\n✅ Cierre final completado")
        print(f"   Para commitear: git add docs/sesiones/{fecha[:7].replace('-', '/')}/{fecha}.md")
        print(f"   git commit -m 'docs(sesion): actualiza horas reales de cierre ({duracion})'")
        print(f"   git push")

if __name__ == '__main__':
    main()
