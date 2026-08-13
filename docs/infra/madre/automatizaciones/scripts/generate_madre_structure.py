"""
Genera estructura completa de Madre
"""

import os

def generate_structure():
    print("=== GENERANDO ESTRUCTURA DE MADRE ===")
    
    # Lista todas las carpetas
    folders = []
    for root, dirs, files in os.walk('docs/infra/madre/'):
        level = root.replace('docs/infra/madre/', '').count(os.sep)
        indent = ' ' * 2 * level
        folders.append(f'{indent}{os.path.basename(root)}/')
        
        subindent = ' ' * 2 * (level + 1)
        for file in sorted(files)[:5]:  # Primeros 5 archivos
            folders.append(f'{subindent}{file}')
    
    # Guarda estructura
    structure = '\n'.join(folders)
    with open('docs/infra/madre/ESTRUCTURA_COMPLETA.md', 'w') as f:
        f.write(f"# Estructura Completa de Madre\n\n```\n{structure}\n```\n")
    
    print("✅ Estructura generada: docs/infra/madre/ESTRUCTURA_COMPLETA.md")

if __name__ == '__main__':
    generate_structure()
