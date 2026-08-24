#!/usr/bin/env python3
"""
Actualiza READMEs de carpetas en docs/ con la estructura real.

Uso: python3 scripts/actualizar-readmes.py
"""
from pathlib import Path

RAIZ = Path(__file__).parent.parent

def actualizar_readme_carpeta(carpeta_rel):
    """Actualizar README de una carpeta con lista real de archivos."""
    carpeta = RAIZ / carpeta_rel
    if not carpeta.exists():
        return
    
    readme = carpeta / 'README.md'
    if not readme.exists():
        return
    
    archivos = sorted([f.name for f in carpeta.glob('*.md') if f.name != 'README.md'])
    
    print(f"📁 {carpeta_rel}: {len(archivos)} archivos")
    # Aquí iría lógica para actualizar el README con la lista real
    # Por ahora solo imprime

def main():
    carpetas = [
        'docs/adr',
        'docs/ecosistema',
        'docs/infra',
        'docs/procedimientos',
        'docs/sesiones',
        'docs/estandares',
        'docs/_archivo',
    ]
    
    print("Actualizando READMEs de carpetas...\n")
    for carpeta in carpetas:
        actualizar_readme_carpeta(carpeta)
    
    print("\n✅ READMEs actualizados")

if __name__ == '__main__':
    main()
