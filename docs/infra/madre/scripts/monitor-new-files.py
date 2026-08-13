"""
Script de monitoreo de nuevos archivos en Madre
- Detecta nuevos archivos
- Detecta archivos modificados
- Actualiza automáticamente
"""

import os
import hashlib
import json
import time
from datetime import datetime
from pathlib import Path

class FileMonitor:
    def __init__(self, folder, state_file='file_state.json'):
        self.folder = folder
        self.state_file = state_file
        self.state = self.load_state()
    
    def load_state(self):
        """Carga el estado anterior de archivos"""
        if os.path.exists(self.state_file):
            with open(self.state_file, 'r') as f:
                return json.load(f)
        return {}
    
    def save_state(self):
        """Guarda el estado actual de archivos"""
        with open(self.state_file, 'w') as f:
            json.dump(self.state, f, indent=2)
    
    def get_file_hash(self, filepath):
        """Calcula hash MD5 de un archivo"""
        hash_md5 = hashlib.md5()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def scan_folder(self):
        """Escanea la carpeta y detecta cambios"""
        print(f"\n=== ESCANEANDO {self.folder} ===")
        print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        
        new_files = []
        modified_files = []
        deleted_files = []
        current_files = {}
        
        # Escanea todos los archivos
        for root, dirs, files in os.walk(self.folder):
            if '.git' in root:
                continue
            
            for file in files:
                filepath = os.path.join(root, file)
                if os.path.isfile(filepath):
                    file_hash = self.get_file_hash(filepath)
                    rel_path = os.path.relpath(filepath, self.folder)
                    current_files[rel_path] = {
                        'hash': file_hash,
                        'mtime': os.path.getmtime(filepath)
                    }
                    
                    # Verifica si es nuevo
                    if rel_path not in self.state:
                        new_files.append(rel_path)
                        print(f"🆕 NUEVO: {rel_path}")
                    # Verifica si fue modificado
                    elif self.state[rel_path]['hash'] != file_hash:
                        modified_files.append(rel_path)
                        print(f"✏️  MODIFICADO: {rel_path}")
        
        # Verifica archivos eliminados
        for rel_path in self.state:
            if rel_path not in current_files:
                deleted_files.append(rel_path)
                print(f"🗑️  ELIMINADO: {rel_path}")
        
        # Actualiza estado
        self.state = current_files
        self.save_state()
        
        # Resumen
        print(f"\n=== RESUMEN ===")
        print(f"🆕 Nuevos: {len(new_files)}")
        print(f"✏️  Modificados: {len(modified_files)}")
        print(f"🗑️  Eliminados: {len(deleted_files)}")
        
        return new_files, modified_files, deleted_files
    
    def process_new_files(self, new_files):
        """Procesa nuevos archivos (ej: actualizar README, generar índice, etc.)"""
        print(f"\n=== PROCESANDO NUEVOS ARCHIVOS ===")
        
        for file in new_files:
            filepath = os.path.join(self.folder, file)
            
            # Si es un .md, actualizar índices
            if file.endswith('.md'):
                print(f"📝 Actualizando índices para: {file}")
                # Aquí podrías llamar a scripts de actualización
                # Ej: generate_index.py, update_readme.py, etc.
        
        print(f"✅ {len(new_files)} archivos procesados")

def main():
    print("=== MONITOR DE NUEVOS ARCHIVOS EN MADRE ===")
    
    # Cambia a la carpeta de Madre
    script_dir = os.path.dirname(os.path.abspath(__file__))
    madre_path = os.path.join(script_dir, '..')
    os.chdir(madre_path)
    
    print(f"Directorio: {os.getcwd()}")
    
    # Crea monitor
    monitor = FileMonitor('.')
    
    # Escanea
    new_files, modified_files, deleted_files = monitor.scan_folder()
    
    # Procesa nuevos archivos
    if new_files:
        monitor.process_new_files(new_files)
    
    return 0

if __name__ == '__main__':
    exit(main())
