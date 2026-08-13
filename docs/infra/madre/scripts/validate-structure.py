"""
Script de validación de estructura de Madre
- Verifica que todas las carpetas tengan README.md
- Verifica que no haya archivos sueltos
- Reporta errores
"""

import os
import sys
from datetime import datetime

def validate_structure(folder):
    """Valida estructura de Madre"""
    print("=== VALIDANDO ESTRUCTURA DE MADRE ===")
    
    errors = []
    warnings = []
    
    # Carpetas esperadas
    expected_folders = [
        'python', 'sesiones', 'adr', 'security', 'red', 'performance',
        'automatizaciones', 'backups', 'change-management', 'disaster-recovery',
        'hardware', 'issues', 'monitoring', 'procedimientos', 'scripts',
        'scriptscd', 'servicios'
    ]
    
    # Verifica carpetas
    for folder_name in expected_folders:
        folder_path = os.path.join(folder, folder_name)
        if os.path.exists(folder_path):
            # Verifica README.md
            readme_path = os.path.join(folder_path, 'README.md')
            if not os.path.exists(readme_path) and folder_name not in ['python', 'scripts', 'scriptscd']:
                warnings.append(f"⚠️  {folder_name}/ no tiene README.md")
        else:
            errors.append(f"❌ Carpeta esperada: {folder_name}/")
    
    # Verifica archivos sueltos en la raíz
    root_files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    allowed_root_files = [
        '.gitignore', 'README.md', 'ESTRUCTURA_COMPLETA.md', 
        'ESTADISTICAS.md', 'file_state.json',
        # Archivos de índice/enlace
        'estado.md', 'backups.md', 'cambios.md', 'change-management.md',
        'disaster-recovery.md', 'hardware.md', 'monitoring.md', 'performance.md',
        'red.md', 'security.md', 'servicios.md', 'sesiones.md'
    ]
    for file in root_files:
        if file not in allowed_root_files:
            errors.append(f"❌ Archivo suelto en raíz: {file}")
    
    # Reporta
    print(f"\n=== RESULTADOS ===")
    print(f"✅ Errores: {len(errors)}")
    print(f"⚠️  Advertencias: {len(warnings)}")
    
    if errors:
        print("\nErrores:")
        for error in errors:
            print(f"  {error}")
    
    if warnings:
        print("\nAdvertencias:")
        for warning in warnings:
            print(f"  {warning}")
    
    if not errors and not warnings:
        print("\n✅ ESTRUCTURA VÁLIDA!")
        return 0
    else:
        return 1

def main():
    print("=== VALIDACIÓN DE ESTRUCTURA ===")
    print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    # Cambia a la carpeta de Madre
    script_dir = os.path.dirname(os.path.abspath(__file__))
    madre_path = os.path.join(script_dir, '..')
    os.chdir(madre_path)
    
    print(f"Directorio: {os.getcwd()}")
    
    # Valida
    result = validate_structure('.')
    
    return result

if __name__ == '__main__':
    exit(main())
