"""
Procesador de entradas para Madre
"""

from utils import limpiar_texto, extraer_fechas, extraer_emails, clasificar_categoria, contar_palabras

def procesar_entrada_diaria(entrada):
    """Procesa una entrada diaria"""
    
    # 1. Limpia texto
    entrada_limpia = limpiar_texto(entrada)
    
    # 2. Extrae fechas
    fechas = extraer_fechas(entrada_limpia)
    
    # 3. Extrae emails
    emails = extraer_emails(entrada_limpia)
    
    # 4. Clasifica por categoría
    categoria = clasificar_categoria(entrada_limpia)
    
    # 5. Cuenta palabras
    palabras = contar_palabras(entrada_limpia)
    
    # 6. Crea resultado
    resultado = {
        'texto_limpio': entrada_limpia,
        'fechas': fechas,
        'emails': emails,
        'categoria': categoria,
        'palabras': palabras,
    }
    
    return resultado

def generar_resumen_entradas(entradas):
    """Genera resumen de múltiples entradas"""
    
    total_entradas = len(entradas)
    total_palabras = sum(entrada['palabras'] for entrada in entradas)
    
    # Cuenta categorías
    categorias = {}
    for entrada in entradas:
        categoria = entrada['categoria']
        categorias[categoria] = categorias.get(categoria, 0) + 1
    
    # Genera tabla
    from utils import generar_tabla
    tabla = generar_tabla(categorias)
    
    # Crea resumen
    resumen = f"""
# Resumen de Entradas

- Total entradas: {total_entradas}
- Total palabras: {total_palabras}

## Categorías

{tabla}
"""
    
    return resumen

