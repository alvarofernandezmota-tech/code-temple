"""
Actualiza README.md de la raíz de Madre con TODO el contenido
"""

import os
from datetime import datetime

def update_readme():
    print("=== ACTUALIZANDO README DE RAÍZ ===")
    
    # Lee ESTRUCTURA_COMPLETA.md
    estructura = ""
    if os.path.exists('ESTRUCTURA_COMPLETA.md'):
        with open('ESTRUCTURA_COMPLETA.md', 'r') as f:
            estructura = f.read()
    
    # Cuenta archivos por carpeta
    folders_stats = {}
    for folder in ['python', 'sesiones', 'adr', 'security', 'red', 'performance', 'automatizaciones']:
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
    readme += f"- **Total scripts:** {sum(s['scripts'] for s in folders_stats.values())}\n"
    readme += f"- **Total workflows:** 4\n\n"
    readme += f"## Automatización\n\n"
    readme += f"✅ Scripts: {sum(s['scripts'] for s in folders_stats.values())}\n"
    readme += f"✅ Workflows: 4\n"
    readme += f"✅ Auditorías: 5\n"
    readme += f"✅ Actualización: Automática\n\n"
    readme += f"## Carpetas\n\n"
    
    for folder, stats in folders_stats.items():
        readme += f"### {folder.capitalize()}\n\n"
        readme += f"- Documentos: {stats['docs']}\n"
        readme += f"- Scripts: {stats['scripts']}\n\n"
    
    readme += f"## Workflows\n\n"
    readme += f"- `update-estado.yml` - Actualiza fecha y hora\n"
    readme += f"- `auto-generate-all-readmes.yml` - Genera READMEs\n"
    readme += f"- `update-madre-root.yml` - Actualiza estructura\n"
    readme += f"- `scheduled-audits.yml` - Auditorías programadas\n\n"
    
    readme += f"## Auditorías\n\n"
    readme += f"- `audit_security.py` - Seguridad\n"
    readme += f"- `audit_workflows.py` - Workflows\n"
    readme += f"- `audit_docs.py` - Documentación\n"
    readme += f"- `check_status.py` - Estado\n"
    readme += f"- `monitor_changes.py` - Cambios\n\n"
    
    readme += f"## Estructura Completa\n\n"
    readme += f"Ver: [ESTRUCTURA_COMPLETA.md](ESTRUCTURA_COMPLETA.md)\n\n"
    readme += f"## Referencias\n\n"
    readme += f"- [code-temple](../../README.md)\n"
    readme += f"- [temple](../../temple/PLAN_MAESTRO.md)\n"
    
    # Guarda README
    with open('README.md', 'w') as f:
        f.write(readme)
    
    print("✅ README actualizado: README.md")

if __name__ == '__main__':
    update_readme()
