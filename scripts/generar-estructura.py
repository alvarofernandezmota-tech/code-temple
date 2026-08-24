"""
Genera descripción automática de la estructura del repo.
Lee todos los READMEs de carpetas y genera un resumen jerárquico.

Uso: python scripts/generar-estructura.py > /tmp/estructura-code-temple.txt
"""
from pathlib import Path
import os

RAIZ = Path(__file__).parent.parent

def leer_readme(ruta):
    """Leer README y extraer título y descripción."""
    if not ruta.exists():
        return None
    contenido = ruta.read_text(encoding="utf-8")
    lineas = contenido.split('\n')
    
    titulo = None
    descripcion = None
    
    for i, linea in enumerate(lineas):
        if linea.startswith('# ') and not titulo:
            titulo = linea[2:].strip()
        elif linea.strip() and not descripcion and i > 0:
            descripcion = linea.strip()
            if len(descripcion) > 100:
                descripcion = descripcion[:97] + "..."
            break
    
    return f"{titulo or ruta.parent.name} — {descripcion or 'Sin descripción'}"

def listar_carpeta(carpeta_rel):
    """Listar archivos de una carpeta con descripciones."""
    carpeta = RAIZ / carpeta_rel
    if not carpeta.exists():
        return []
    
    archivos = []
    for f in sorted(carpeta.glob('*.md')):
        if f.name == 'README.md':
            continue
        desc = leer_readme(f)
        if desc:
            archivos.append(f"- {f.name} — {desc.split(' — ', 1)[1] if ' — ' in desc else 'Sin descripción'}")
    
    return archivos

def main():
    print("# Estructura del repo (generado automáticamente)\n")
    
    carpetas = [
        ("docs/", "Documentación principal"),
        ("docs/adr/", "Decisiones de arquitectura"),
        ("docs/ecosistema/", "Mapa de repos y plan del bot"),
        ("docs/infra/", "Infraestructura real"),
        ("docs/procedimientos/", "Checklists paso a paso"),
        ("docs/sesiones/", "Diario de sesiones"),
        ("docs/estandares/", "Convenciones compartidas"),
        ("docs/_archivo/", "Archivos archivados"),
        ("scripts/", "Automatizaciones"),
    ]
    
    for carpeta_rel, descripcion in carpetas:
        readme = RAIZ / carpeta_rel / "README.md"
        if readme.exists():
            info = leer_readme(readme)
            print(f"## {carpeta_rel}")
            print(f"{info}\n")
            
            archivos = listar_carpeta(carpeta_rel)
            if archivos:
                print("\n".join(archivos))
                print()
    
    print("\n## Relacionado con")
    print("- [AGENTS.md](AGENTS.md) — reglas para trabajar en este repo")
    print("- [CONTEXT.md](CONTEXT.md) — qué es este repo en 30 segundos")

if __name__ == "__main__":
    main()
