"""
Genera README.md para sesiones automáticamente
"""

import os

def generate_index():
    # Lista archivos .md en la carpeta
    archivos = [f for f in os.listdir('.') if f.endswith('.md') and f != 'README.md']
    
    # Genera README
    readme = "# Sesiones de Desarrollo\n\n"
    readme += "## Índice de Sesiones\n\n"
    
    for archivo in sorted(archivos, reverse=True):
        readme += f"- [{archivo}]({archivo})\n"
    
    readme += "\n## Automatización\n\n"
    readme += "Este README se actualiza automáticamente con cada nueva sesión.\n"
    
    # Guarda README
    with open('README.md', 'w') as f:
        f.write(readme)
    
    print("README.md generado para sesiones")

if __name__ == '__main__':
    generate_index()
