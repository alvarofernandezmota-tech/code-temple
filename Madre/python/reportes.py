"""
Generador de reportes para Madre
"""

from datetime import datetime, timedelta
from utils import generar_tabla

def generar_reporte_semanal(entradas):
    """Genera reporte semanal"""
    
    # Filtra entradas de la semana
    hoy = datetime.now()
    semana_pasada = hoy - timedelta(days=7)
    
    entradas_semana = [
        entrada for entrada in entradas
        if datetime.strptime(entrada['fecha'], '%Y-%m-%d') >= semana_pasada
    ]
    
    # Calcula estadísticas
    total_entradas = len(entradas_semana)
    total_palabras = sum(entrada['palabras'] for entrada in entradas_semana)
    
    # Cuenta categorías
    categorias = {}
    for entrada in entradas_semana:
        categoria = entrada['categoria']
        categorias[categoria] = categorias.get(categoria, 0) + 1
    
    # Genera tabla
    tabla = generar_tabla(categorias)
    
    # Crea reporte
    reporte = f"""
# Reporte Semanal

**Fecha:** {hoy.strftime('%d/%m/%Y')}

## Estadísticas

- Total entradas: {total_entradas}
- Total palabras: {total_palabras}

## Categorías

{tabla}

## Aprendizajes

[Aquí irían los aprendizajes de la semana]

## Próximos Pasos

[Aquí irían los próximos pasos]
"""
    
    return reporte

def generar_reporte_mensual(entradas):
    """Genera reporte mensual"""
    
    # Filtra entradas del mes
    hoy = datetime.now()
    mes_pasado = hoy.replace(day=1) - timedelta(days=1)
    
    entradas_mes = [
        entrada for entrada in entradas
        if datetime.strptime(entrada['fecha'], '%Y-%m-%d') >= mes_pasado
    ]
    
    # Calcula estadísticas
    total_entradas = len(entradas_mes)
    total_palabras = sum(entrada['palabras'] for entrada in entradas_mes)
    
    # Cuenta categorías
    categorias = {}
    for entrada in entradas_mes:
        categoria = entrada['categoria']
        categorias[categoria] = categorias.get(categoria, 0) + 1
    
    # Genera tabla
    tabla = generar_tabla(categorias)
    
    # Crea reporte
    reporte = f"""
# Reporte Mensual

**Mes:** {hoy.strftime('%B %Y')}

## Estadísticas

- Total entradas: {total_entradas}
- Total palabras: {total_palabras}

## Categorías

{tabla}

## Aprendizajes

[Aquí irían los aprendizajes del mes]

## Próximos Pasos

[Aquí irían los próximos pasos]
"""
    
    return reporte
