"""
Funciones utilitarias para Madre
"""

def limpiar_texto(texto):
    """Limpia y normaliza texto"""
    # Elimina espacios extra
    texto = ' '.join(texto.split())
    
    # Normaliza mayúsculas/minúsculas
    texto = texto.strip()
    
    return texto

def extraer_fechas(texto):
    """Extrae fechas de texto"""
    import re
    
    # Patrón para fechas (DD/MM/YYYY)
    patron = r'\d{2}/\d{2}/\d{4}'
    fechas = re.findall(patron, texto)
    
    return fechas

def extraer_emails(texto):
    """Extrae emails de texto"""
    import re
    
    # Patrón para emails
    patron = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(patron, texto)
    
    return emails

def clasificar_categoria(texto):
    """Clasifica texto por categoría"""
    categorias = {
        'personal': ['yo', 'mi', 'mío', 'personal'],
        'trabajo': ['trabajo', 'reunión', 'proyecto', 'tarea'],
        'aprendizaje': ['aprender', 'estudiar', 'curso', 'libro'],
        'salud': ['salud', 'ejercicio', 'comida', 'dormir'],
    }
    
    texto_lower = texto.lower()
    
    for categoria, palabras in categorias.items():
        for palabra in palabras:
            if palabra in texto_lower:
                return categoria
    
    return 'general'

def contar_palabras(texto):
    """Cuenta palabras en texto"""
    palabras = texto.split()
    return len(palabras)

def generar_tabla(datos):
    """Genera tabla en Markdown"""
    tabla = "| Categoría | Cantidad |\n"
    tabla += "|-----------|----------|\n"
    
    for categoria, cantidad in datos.items():
        tabla += f"| {categoria} | {cantidad} |\n"
    
    return tabla

