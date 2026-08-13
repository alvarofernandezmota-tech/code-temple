"""
Script de cierre automático de Madre
- Actualiza README y estructura
- Detecta archivos duplicados
- Detecta archivos fuera de lugar
- Detecta carpetas vacías
- Verifica documentación
"""

import os
import hashlib
from datetime import datetime
from pathlib import Path

def get_file_hash(filepath):
    """Calcula hash MD5 de un archivo"""
    hash_md5 = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def find_duplicates(folder):
    """Encuentra archivos duplicados por hash"""
    print("\n=== BUSCANDO DUPLICADOS ===")
    hashes = {}
    duplicates = []
    
    for root, dirs, files in os.walk(folder):
        if '.git' in root:
            continue
        
        for file in files:
            filepath = os.path.join(root, file)
            if os.path.isfile(filepath):
                file_hash = get_file_hash(filepath)
                if file_hash in hashes:
                    duplicates.append((filepath, hashes[file_hash]))
                    print(f"❌ Duplicado: {filepath}")
                    print(f"   Original: {hashes[file_hash]}")
                else:
                    hashes[file_hash] = filepath
    
    return duplicates

def find_empty_folders(folder):
    """Encuentra carpetas vacías"""
    print("\n=== BUSCANDO CARPETAS VACÍAS ===")
    empty = []
    
    for root, dirs, files in os.walk(folder, topdown=False):
        if '.git' in root:
            continue
        
        if not os.listdir(root) and root != folder:
            empty.append(root)
            print(f"❌ Carpeta vacía: {root}")
    
    return empty

def find_misplaced_files(folder, valid_folders):
    """Encuentra archivos fuera de lugar"""
    print("\n=== BUSCANDO ARCHIVOS FUERA DE LUGAR ===")
    misplaced = []
    
    root_files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    if root_files:
        for file in root_files:
            if file not in ['.gitignore', 'README.md', 'ESTRUCTURA_COMPLETA.md']:
                misplaced.append(os.path.join(folder, file))
                print(f"❌ Archivo en raíz: {file}")
    
    root_folders = [f for f in os.listdir(folder) if os.path.isdir(os.path.join(folder, f)) and f not in valid_folders and f != '.git']
    if root_folders:
        for folder_name in root_folders:
            misplaced.append(os.path.join(folder, folder_name))
            print(f"❌ Carpeta inválida: {folder_name}")
    
    return misplaced

def check_documentation(folder):
    """Verifica que cada carpeta tenga README.md"""
    print("\n=== VERIFICANDO DOCUMENTACIÓN ===")
    missing_readme = []
    
    for root, dirs, files in os.walk(folder):
        if '.git' in root:
            continue
        
        if 'README.md' not in files and os.path.basename(root) not in ['python', 'scripts', 'scriptscd']:
            if not os.path.exists(os.path.join(root, 'README.md')):
                missing_readme.append(root)
                print(f"⚠️  Sin README: {root}")
    
    return missing_readme

def update_readme():
    """Actualiza README automáticamente"""
    print("\n=== ACTUALIZANDO README ===")
    
    folders_stats = {}
    for folder in ['python', 'sesiones', 'adr', 'security', 'red', 'performance', 'automatizaciones', 'backups', 'change-management', 'disaster-recovery', 'hardware', 'issues', 'monitoring', 'procedimientos', 'scripts', 'scriptscd', 'servicios']:
        folder_path = folder
        if os.path.exists(folder_path):
            files = [f for f in os.listdir(folder_path) if f.endswith('.md')]
            scripts_path = f'{folder_path}/scripts'
            scripts = [f for f in os.listdir(scripts_path)] if os.path.exists(scripts_path) else []
            folders_stats[folder] = {
                'docs': len(files),
                'scripts': len(scripts)
            }
    
    readme = "# Infraestructura de Madre\n\n"
    readme += f"**Última actualización:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
    readme += "## Resumen\n\n"
    readme += f"- **Total carpetas:** {len(folders_stats)}\n"
    readme += f"- **Total documentos:** {sum(s['docs'] for s in folders_stats.values())}\n"
    readme += f"- **Total scripts:** {sum(s['scripts'] for s in folders_stats.values())}\n"
    readme += "- **Total workflows:** 4\n\n"
    readme += "## Automatización\n\n"
    readme += f"✅ Scripts: {sum(s['scripts'] for s in folders_stats.values())}\n"
    readme += "✅ Workflows: 4\n"
    readme += "✅ Auditorías: 5\n"
    readme += "✅ Actualización: Automática\n\n"
    readme += "## Carpetas\n\n"
    
    for folder, stats in folders_stats.items():
        readme += f"### {folder.capitalize()}\n\n"
        readme += f"- Documentos: {stats['docs']}\n"
        readme += f"- Scripts: {stats['scripts']}\n\n"
    
    with open('README.md', 'w') as f:
        f.write(readme)
    
    print("✅ README actualizado")

def main():
    print("=== AUTO CIERRE DE MADRE ===")
    print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    madre_path = os.path.join(script_dir, '..')
    os.chdir(madre_path)
    
    print(f"\nDirectorio: {os.getcwd()}")
    
    valid_folders = [
        'python', 'sesiones', 'adr', 'security', 'red', 'performance',
        'automatizaciones', 'backups', 'change-management', 'disaster-recovery',
        'hardware', 'issues', 'monitoring', 'procedimientos', 'scripts',
        'scriptscd', 'servicios'
    ]
    
    duplicates = find_duplicates('.')
    empty_folders = find_empty_folders('.')
    misplaced = find_misplaced_files('.', valid_folders)
    missing_docs = check_documentation('.')
    
    update_readme()
    
    print("\n=== RESUMEN ===")
    print(f"✅ Duplicados: {len(duplicates)}")
    print(f"✅ Carpetas vacías: {len(empty_folders)}")
    print(f"✅ Archivos fuera de lugar: {len(misplaced)}")
    print(f"✅ Carpetas sin README: {len(missing_docs)}")
    
    if duplicates or empty_folders or misplaced or missing_docs:
        print("\n⚠️  Hay problemas que revisar!")
        return 1
    else:
        print("\n✅ TODO LIMPIO!")
        return 0

if __name__ == '__main__':
    exit(main())
