"""
Genera un volcado de contexto del repo: concatena AGENTS.md, CONTEXT.md,
todos los READMEs de docs/, todos los ADRs, y procedimientos clave.

Uso: python scripts/generar-contexto.py > /tmp/contexto-code-temple.txt
"""
from pathlib import Path

RAIZ = Path(__file__).parent.parent

ARCHIVOS = [
    # Raíz
    "AGENTS.md",
    "CONTEXT.md",
    "docs/README.md",
    
    # Ecosistema
    "docs/ecosistema/README.md",
    "docs/ecosistema/fuente-de-verdad.md",
    "docs/ecosistema/plan-bot.md",
    "docs/ecosistema/vision.md",
    "docs/ecosistema/repos-activos.md",
    "docs/ecosistema/repos-archivados.md",
    
    # Infra
    "docs/infra/README.md",
    
    # ADRs (todos)
    "docs/adr/README.md",
    "docs/adr/001-bifrost-desde-cero.md",
    "docs/adr/002-regla-enganche-cuadruple.md",
    "docs/adr/003-orden-rollout-formatter.md",
    "docs/adr/004-convencion-scripts-procedimientos.md",
    "docs/adr/005-plan-maestro-ecosistema.md",
    
    # Procedimientos
    "docs/procedimientos/README.md",
    "docs/procedimientos/plantilla-readme.md",
    "docs/procedimientos/plantilla-repo.md",
    "docs/procedimientos/plantilla-sesion.md",
    "docs/procedimientos/inicio-sesion.md",
    "docs/procedimientos/cierre-sesion.md",
    "docs/procedimientos/auditoria-repo.md",
    "docs/procedimientos/generar-contexto.md",
    "docs/procedimientos/mantenimiento-documentacion.md",
    "docs/procedimientos/nueva-sesion.md",
    
    # Sesiones
    "docs/sesiones/README.md",
    
    # Estándares
    "docs/estandares/README.md",
    "docs/estandares/frontmatter.md",
    
    # Scripts
    "scripts/README.md",
    
    # Archivo
    "docs/_archivo/README.md",
]

def main():
    for rel in ARCHIVOS:
        ruta = RAIZ / rel
        if not ruta.exists():
            print(f"[AVISO: falta {rel}]\n")
            continue
        print(f"=== {rel} ===")
        print(ruta.read_text(encoding="utf-8"))
        print()

if __name__ == "__main__":
    main()
