"""
Genera README.md para ADR automáticamente
"""

import os

def generate_index():
    # Lista archivos .md en la carpeta
    archivos = [f for f in os.listdir('.') if f.endswith('.md') and f != 'README.md']
    
    # Genera README
    readme = "# Decisiones Arquitectónicas (ADR)\n\n"
    readme += "## Índice de ADRs\n\n"
    
    for archivo in sorted(archivos):
        readme += f"- [{archivo}]({archivo})\n"
    
    readme += "\n## Automatización\n\n"
    readme += "Este README se actualiza automáticamente con cada nuevo ADR.\n"
    
    # Guarda README
    with open('README.md', 'w') as f:
        f.write(readme)
    
    print("README.md generado para ADR")

if __name__ == '__main__':
    generate_index()
