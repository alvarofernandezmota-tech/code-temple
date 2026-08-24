#!/usr/bin/env python3
"""
Auditoría de enlaces rotos en archivos .md.

Uso: python3 scripts/auditoria-enlaces.py
"""
import re
from pathlib import Path

RAIZ = Path(__file__).parent.parent

def buscar_enlaces(archivo):
    """Buscar enlaces Markdown en un archivo."""
    contenido = archivo.read_text(encoding='utf-8')
    # Enlaces Markdown: [texto](ruta)
    enlaces = re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', contenido)
    return enlaces

def main():
    print("🔍 Auditoría de enlaces rotos...\n")
    
    archivos_md = list(RAIZ.glob('**/*.md'))
    problemas = []
    
    for md in archivos_md:
        if '_archivo' in str(md):
            continue  # Saltar archivos archivados
        
        enlaces = buscar_enlaces(md)
        for texto, ruta in enlaces:
            if ruta.startswith('http'):
                continue  # Saltar enlaces externos
            
            # Resolver ruta relativa
            ruta_abs = (md.parent / ruta).resolve()
            if not ruta_abs.exists():
                problemas.append(f"{md.relative_to(RAIZ)}: [{texto}]({ruta}) → NO EXISTE")
    
    if problemas:
        print("❌ Enlaces rotos encontrados:\n")
        for p in problemas:
            print(f"  {p}")
    else:
        print("✅ No hay enlaces rotos")

if __name__ == '__main__':
    main()
