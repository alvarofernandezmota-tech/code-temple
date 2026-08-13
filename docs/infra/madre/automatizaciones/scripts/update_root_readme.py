"""
Actualiza README.md de la raíz de Madre
"""

import os
from datetime import datetime

def update_readme():
    print("=== ACTUALIZANDO README DE RAÍZ ===")
    
    # Cuenta archivos por carpeta
    folders_stats = {}
    for folder in ['sesiones', 'adr', 'security', 'red', 'performance', 'automatizaciones']:
        folder_path = folder
        if os.path.exists(folder_path):
            files = [f for f in os.listdir(folder_path) if f.endswith('.md')]
            scripts_path = f'{folder_path}/scripts'
            scripts = [f for f in os.listdir(scripts_path)] if os.path.exists(scripts_path) else []
            folders_stats[folder] = {
                'docs': len(files),
                'scripts': len(scripts)
            }
    
    # Genera README
    readme = f"# Infraestructura de Madre\n\n"
    readme += f"**Última actualización:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
    readme += f"## Resumen\n\n"
    readme += f"- **Total carpetas:** {len(folders_stats)}\n"
    readme += f"- **Total documentos:** {sum(s['docs'] for s in folders_stats.values())}\n"
    readme += f"- **Total scripts:** {sum(s['scripts'] for s in folders_stats.values())}\n\n"
    readme += f"## Carpetas\n\n"
    
    for folder, stats in folders_stats.items():
        readme += f"### {folder.capitalize()}\n\n"
        readme += f"- Documentos: {stats['docs']}\n"
        readme += f"- Scripts: {stats['scripts']}\n\n"
    
    readme += f"## Automatización\n\n"
    readme += f"Este README se actualiza automáticamente con cada cambio.\n\n"
    readme += f"## Referencias\n\n"
    readme += f"- [code-temple](../../README.md)\n"
    
    # Guarda README
    with open('README.md', 'w') as f:
        f.write(readme)
    
    print("✅ README actualizado: README.md")

if __name__ == '__main__':
    update_readme()
