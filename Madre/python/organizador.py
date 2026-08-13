"""
Organizador de archivos para Madre
"""

import os
import shutil
from datetime import datetime

def organizar_archivos_por_fecha(ruta):
    """Organiza archivos por fecha"""
    
    # Lista archivos
    archivos = os.listdir(ruta)
    
    # Clasifica por fecha
    por_fecha = {}
    for archivo in archivos:
        ruta_archivo = os.path.join(ruta, archivo)
        if os.path.isfile(ruta_archivo):
            # Obtiene fecha de modificación
            fecha_mod = os.path.getmtime(ruta_archivo)
            fecha_str = datetime.fromtimestamp(fecha_mod).strftime('%Y-%m')
            
            if fecha_str not in por_fecha:
                por_fecha[fecha_str] = []
            
            por_fecha[fecha_str].append(archivo)
    
    # Crea carpetas por mes
    for mes, archivos_mes in por_fecha.items():
        carpeta_mes = os.path.join(ruta, mes)
        os.makedirs(carpeta_mes, exist_ok=True)
        
        # Mueve archivos
        for archivo in archivos_mes:
            ruta_origen = os.path.join(ruta, archivo)
            ruta_destino = os.path.join(carpeta_mes, archivo)
            shutil.move(ruta_origen, ruta_destino)
    
    return "Archivos organizados por fecha"

def eliminar_duplicados(ruta):
    """Elimina archivos duplicados"""
    
    # Lista archivos
    archivos = os.listdir(ruta)
    
    # Calcula hashes
    hashes = {}
    duplicados = []
    
    for archivo in archivos:
        ruta_archivo = os.path.join(ruta, archivo)
        if os.path.isfile(ruta_archivo):
            # Calcula hash (simplificado)
            with open(ruta_archivo, 'rb') as f:
                contenido = f.read()
                hash_archivo = hash(contenido)
            
            if hash_archivo in hashes:
                duplicados.append(ruta_archivo)
            else:
                hashes[hash_archivo] = ruta_archivo
    
    # Elimina duplicados
    for duplicado in duplicados:
        os.remove(duplicado)
    
    return f"Eliminados {len(duplicados)} duplicados"

