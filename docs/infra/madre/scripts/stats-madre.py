"""
Script de estadísticas de Madre
- Cuenta archivos por tipo
- Cuenta líneas de código
- Genera reporte
"""

import os
import json
from datetime import datetime
from pathlib import Path

def count_files(folder):
    """Cuenta archivos por tipo"""
    stats = {
        'python': 0,
        'bash': 0,
        'markdown': 0,
        'yaml': 0,
        'other': 0
    }
    
    for root, dirs, files in os.walk(folder):
        if '.git' in root:
            continue
        
        for file in files:
            if file.endswith('.py'):
                stats['python'] += 1
            elif file.endswith('.sh'):
                stats['bash'] += 1
            elif file.endswith('.md'):
                stats['markdown'] += 1
            elif file.endswith(('.yml', '.yaml')):
                stats['yaml'] += 1
            else:
                stats['other'] += 1
    
    return stats

def count_lines(folder):
    """Cuenta líneas de código"""
    total_lines = 0
    total_files = 0
    
    for root, dirs, files in os.walk(folder):
        if '.git' in root:
            continue
        
        for file in files:
            if file.endswith(('.py', '.sh', '.md')):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        lines = len(f.readlines())
                        total_lines += lines
                        total_files += 1
                except:
                    pass
    
    return total_lines, total_files

def generate_report(stats, lines, files):
    """Genera reporte de estadísticas"""
    report = f"# Estadísticas de Madre - {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
    report += "## Archivos por Tipo\n\n"
    report += f"- Python (.py): {stats['python']}\n"
    report += f"- Bash (.sh): {stats['bash']}\n"
    report += f"- Markdown (.md): {stats['markdown']}\n"
    report += f"- YAML (.yml): {stats['yaml']}\n"
    report += f"- Otros: {stats['other']}\n\n"
    report += f"## Líneas de Código\n\n"
    report += f"- Total líneas: {lines}\n"
    report += f"- Total archivos: {files}\n"
    report += f"- Promedio líneas/archivo: {lines/files:.1f}\n\n"
    
    return report

def main():
    print("=== ESTADÍSTICAS DE MADRE ===")
    
    # Cambia a la carpeta de Madre
    script_dir = os.path.dirname(os.path.abspath(__file__))
    madre_path = os.path.join(script_dir, '..')
    os.chdir(madre_path)
    
    print(f"Directorio: {os.getcwd()}")
    
    # Cuenta archivos
    stats = count_files('.')
    lines, files = count_lines('.')
    
    # Genera reporte
    report = generate_report(stats, lines, files)
    
    # Guarda reporte
    with open('ESTADISTICAS.md', 'w') as f:
        f.write(report)
    
    print(f"\n{report}")
    print("✅ Reporte guardado: ESTADISTICAS.md")
    
    return 0

if __name__ == '__main__':
    exit(main())
