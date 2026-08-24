#!/usr/bin/env python3
"""
Auditoría de archivos duplicados o solapados.

Uso: python3 scripts/auditoria-duplicados.py
"""
from pathlib import Path
from collections import defaultdict

RAIZ = Path(__file__).parent.parent

def main():
    print("🔍 Auditoría de duplicados...\n")
    
    # Agrupar por nombre de archivo (sin ruta)
    por_nombre = defaultdict(list)
    
    for md in RAIZ.glob('**/*.md'):
        if '_archivo' in str(md):
            continue
        por_nombre[md.name].append(str(md.relative_to(RAIZ)))
    
    duplicados = {k: v for k, v in por_nombre.items() if len(v) > 1}
    
    if duplicados:
        print("⚠️  Archivos con mismo nombre (posibles duplicados):\n")
        for nombre, rutas in duplicados.items():
            print(f"  {nombre}:")
            for r in rutas:
                print(f"    - {r}")
    else:
        print("✅ No hay duplicados")

if __name__ == '__main__':
    main()
