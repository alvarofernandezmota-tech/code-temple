#!/usr/bin/env python3
"""
Auditoría de frontmatter YAML en archivos .md.

Uso: python3 scripts/auditoria-frontmatter.py
"""
import re
from pathlib import Path

RAIZ = Path(__file__).parent.parent

def tiene_frontmatter(archivo):
    """Verificar si un archivo tiene frontmatter YAML."""
    contenido = archivo.read_text(encoding='utf-8')
    return contenido.startswith('---\n')

def main():
    print("🔍 Auditoría de frontmatter YAML...\n")
    
    carpetas_con_frontmatter = [
        'docs/sesiones',
        'docs/infra',
        'docs/adr',
    ]
    
    sin_frontmatter = []
    
    for carpeta_rel in carpetas_con_frontmatter:
        carpeta = RAIZ / carpeta_rel
        if not carpeta.exists():
            continue
        
        for md in carpeta.glob('**/*.md'):
            if md.name == 'README.md':
                continue
            if not tiene_frontmatter(md):
                sin_frontmatter.append(str(md.relative_to(RAIZ)))
    
    if sin_frontmatter:
        print("❌ Archivos sin frontmatter:\n")
        for f in sin_frontmatter:
            print(f"  {f}")
    else:
        print("✅ Todos los archivos tienen frontmatter")

if __name__ == '__main__':
    main()
