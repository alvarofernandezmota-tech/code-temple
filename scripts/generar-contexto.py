"""
Genera un volcado de contexto del repo: concatena AGENTS.md, CONTEXT.md
y los documentos clave de docs/ecosistema y docs/estandares en un solo
bloque de texto, listo para pegar en una sesion de IA o indexar con
Mimir/Ollama.

Uso: python scripts/generar-contexto.py > /tmp/contexto-code-temple.txt
"""
from pathlib import Path

RAIZ = Path(__file__).parent.parent

ARCHIVOS = [
    "AGENTS.md",
    "CONTEXT.md",
    "docs/ecosistema/README.md",
    "docs/ecosistema/fuente-de-verdad.md",
    "docs/ecosistema/plan-bot.md",
    "docs/ecosistema/vision.md",
    "docs/ecosistema/pendiente-proxima-sesion.md",
    "docs/estandares/frontmatter.md",
    "docs/adr/001-bifrost-desde-cero.md",
    "docs/procedimientos/cierre-sesion.md",
    "docs/adr/002-regla-enganche-cuadruple.md",
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
