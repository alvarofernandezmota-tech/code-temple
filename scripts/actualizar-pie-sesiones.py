#!/usr/bin/env python3
"""
Actualiza el pie de página de TODOS los archivos de sesión con:
- Primer commit
- Último commit
- Horas de trabajo
- Autor
- Última actualización

Uso: python3 scripts/actualizar-pie-sesiones.py [--archivo YYYY-MM-DD.md]
"""
import subprocess
from pathlib import Path
from datetime import datetime
import re

RAIZ = Path(__file__).parent.parent

def get_git_info(fecha):
    """Obtener info de commits para una fecha."""
    cmd = f'git log --since="{fecha} 00:00:00" --until="{fecha} 23:59:59" --format="%h %ai %an %s"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    lines = result.stdout.strip().split('\n') if result.stdout.strip() else []
    
    if not lines:
        return None
    
    primer = lines[-1].split()
    ultimo = lines[0].split()
    
    return {
        'primer_commit': f"{primer[0]} ({primer[1]} {primer[2][:5]})",
        'ultimo_commit': f"{ultimo[0]} ({ultimo[1]} {ultimo[2][:5]})",
        'autor': ' '.join(primer[3:-1]),
        'total_commits': len(lines)
    }

def calcular_horas(fecha):
    """Calcular horas de trabajo."""
    cmd = f'git log --since="{fecha} 00:00:00" --until="{fecha} 23:59:59" --format="%ai"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    lines = result.stdout.strip().split('\n') if result.stdout.strip() else []
    
    if len(lines) < 2:
        return "0 minutos"
    
    h1, m1 = int(lines[-1].split()[1].split(':')[0]), int(lines[-1].split()[1].split(':')[1])
    h2, m2 = int(lines[0].split()[1].split(':')[0]), int(lines[0].split()[1].split(':')[1])
    
    duracion_min = (h2 * 60 + m2) - (h1 * 60 + m1)
    horas = duracion_min // 60
    mins = duracion_min % 60
    
    if horas > 0:
        return f"{horas} hora{'s' if horas > 1 else ''} {mins} minutos"
    return f"{mins} minutos"

def actualizar_pie(archivo):
    """Actualizar pie de página de un archivo."""
    # Extraer fecha del nombre
    fecha = archivo.stem  # 2026-08-24
    
    info = get_git_info(fecha)
    if not info:
        print(f"⚠️  {archivo.name}: sin commits")
        return False
    
    horas = calcular_horas(fecha)
    ahora = datetime.now().strftime('%Y-%m-%d %H:%M CEST')
    
    # Leer contenido
    contenido = archivo.read_text(encoding='utf-8')
    
    # Quitar pie antiguo (si existe)
    contenido = re.sub(
        r'\n---\n\n\*\*Fin de sesión.*$',
        '',
        contenido,
        flags=re.DOTALL
    )
    
    # Añadir pie nuevo
    pie = f"""
---

**Fin de sesión {fecha}**

- **Primer commit:** {info['primer_commit']}
- **Último commit:** {info['ultimo_commit']}
- **Horas de trabajo:** {horas}
- **Autor:** {info['autor']}
- **Total commits:** {info['total_commits']}
- **Última actualización:** {ahora}
"""
    
    archivo.write_text(contenido + pie, encoding='utf-8')
    print(f"✅ {archivo.name}: actualizado")
    return True

def main():
    sesiones_dir = RAIZ / 'docs/sesiones'
    
    if not sesiones_dir.exists():
        print("❌ No existe docs/sesiones/")
        return
    
    print("🔍 Actualizando pies de sesión...\n")
    
    actualizados = 0
    for md in sesiones_dir.glob('**/*.md'):
        if md.name == 'README.md':
            continue
        if actualizar_pie(md):
            actualizados += 1
    
    print(f"\n✅ {actualizados} archivos actualizados")

if __name__ == '__main__':
    main()
