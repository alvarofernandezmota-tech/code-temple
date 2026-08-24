#!/usr/bin/env python3
"""
Actualiza automáticamente AGENTS.md y CONTEXT.md con la estructura actual del repo.

Uso: python3 scripts/actualizar-agents-context.py
"""
from pathlib import Path
from datetime import datetime

RAIZ = Path(__file__).parent.parent

def listar_carpeta(carpeta_rel):
    """Listar archivos .md de una carpeta."""
    carpeta = RAIZ / carpeta_rel
    if not carpeta.exists():
        return []
    return sorted([f.name for f in carpeta.glob('*.md') if f.name != 'README.md'])

def generar_agents():
    """Generar AGENTS.md actualizado."""
    adr_files = listar_carpeta('docs/adr')
    scripts_files = [f for f in (RAIZ / 'scripts').glob('*.py')]
    
    contenido = f"""# AGENTS.md — reglas para trabajar en este repo

## Antes de cualquier cambio en docs/infra/madre
- Correr docs/infra/madre/auditoria/revisar-madre.sh y verificar con
  docs/infra/madre/auditoria/auditoria.py antes de commitear
- Nunca dejar un .md como plantilla vacía sin dato real

## Commits
- Formato: tipo: descripción breve en presente
- Un commit por cambio lógico, no mezclar reestructuración con contenido

## Estructura del repo (no mover sin actualizar los README)
- docs/infra/ — estado real de servidores (madre, futuro acer)
- docs/sesiones/ — diario de trabajo, uno por día
- docs/ecosistema/ — mapa de repos y plan del bot bifrost
- scripts/ — automatización ({', '.join([f.stem for f in scripts_files[:5]])})
- docs/estandares/ — convenciones compartidas (frontmatter YAML)
- docs/procedimientos/ — checklists paso a paso para tareas recurrentes
- docs/adr/ — decisiones de arquitectura ({len(adr_files)} ADRs: {', '.join(adr_files)})

## Regla de mantenimiento
Cuando se cree o modifique un archivo en docs/ecosistema/, docs/adr/, docs/procedimientos/
o docs/estandares/, actualizar tambien scripts/generar-contexto.py
(lista ARCHIVOS) en el mismo commit. El volcado de contexto no puede
quedarse desactualizado.

## Arquitectura bifrost (cuando exista)
- Bifrost es solo interfaz, nunca lógica
- Toda función nueva se prueba primero en midgaror antes de exponerla
  como comando de Telegram

## Nunca hacer
- No crear automatizaciones que commiteen solas (nada de GitHub Actions
  escribiendo en docs/infra)
- No mezclar diario personal (va en midgaror) con sesiones de trabajo
  (van aquí)
- No dejar rutas relativas sin verificar tras mover archivos (usar
  auditoria.py o grep antes de dar por bueno un mv)
"""
    return contenido

def generar_context():
    """Generar CONTEXT.md actualizado."""
    adr_files = listar_carpeta('docs/adr')
    scripts_files = [f.stem for f in (RAIZ / 'scripts').glob('*.py')]
    
    contenido = f"""# CONTEXT.md — qué es este repo en 30 segundos

code-temple es la base técnica del ecosistema de Álvaro. Sustituye a
yggdrasil-dew (archivado). Aquí vive:

- Documentación de infraestructura real (servidor Madre, Arch Linux)
- Diario de sesiones de trabajo (no confundir con el diario personal,
  que vive en el repo midgaror)
- El plan y mapa del ecosistema completo de repos (docs/ecosistema/)
- Estándares compartidos entre repos (docs/estandares/)
- Decisiones de arquitectura (docs/adr/{', '.join(adr_files)})
- Procedimientos y scripts automatizados (docs/procedimientos/, scripts/)

## Si eres un agente/IA leyendo esto por primera vez
1. Lee docs/ecosistema/README.md para el mapa completo
2. Lee AGENTS.md para las reglas de esta base de código
3. No asumas nada de docs/infra/ sin correr antes su script de auditoría
4. Para contexto completo: `python3 scripts/generar-contexto.py`
5. Para estructura automática: `python3 scripts/generar-estructura.py`

## Estado actual ({datetime.now().strftime('%Y-%m-%d')})
- ✅ {len(adr_files)} ADRs completos ({', '.join(adr_files)})
- ✅ 7 carpetas en docs/ con READMEs alineados
- ✅ {len(scripts_files)} scripts automatizados ({', '.join(scripts_files)})
- ✅ Procedimientos 1:1 con scripts
- ✅ Lista para migrar plantilla a bifrost/midgaror
"""
    return contenido

def main():
    print("Actualizando AGENTS.md...")
    (RAIZ / 'AGENTS.md').write_text(generar_agents(), encoding='utf-8')
    
    print("Actualizando CONTEXT.md...")
    (RAIZ / 'CONTEXT.md').write_text(generar_context(), encoding='utf-8')
    
    print("✅ Actualizados AGENTS.md y CONTEXT.md")

if __name__ == '__main__':
    main()
