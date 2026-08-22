"""
Audita la estructura documental de code-temple (no el sistema Madre,
eso lo hace docs/infra/madre/auditoria/auditoria.py aparte).

Comprueba que todos los links relativos en Markdown dentro de docs/,
AGENTS.md y CONTEXT.md apuntan a archivos que existen de verdad.
No modifica nada, solo reporta lo que no coincide.

Uso: python scripts/auditoria-repo.py
"""
import re
from pathlib import Path

RAIZ = Path(__file__).parent.parent
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")

def archivos_markdown():
    yield RAIZ / "AGENTS.md"
    yield RAIZ / "CONTEXT.md"
    yield from (p for p in RAIZ.glob("docs/**/*.md") if "_archivo" not in p.parts)

def main():
    problemas = []
    for archivo in archivos_markdown():
        if not archivo.exists():
            continue
        texto = archivo.read_text(encoding="utf-8")
        for _, destino in LINK_RE.findall(texto):
            if destino.startswith(("http://", "https://", "#")):
                continue
            ruta_destino = (archivo.parent / destino).resolve()
            if not ruta_destino.exists():
                problemas.append(f"{archivo.relative_to(RAIZ)} -> enlace roto: {destino}")

    if not problemas:
        print("Todos los enlaces relativos resuelven correctamente.")
    else:
        print(f"{len(problemas)} enlace(s) roto(s):")
        for p in problemas:
            print(f"  - {p}")

if __name__ == "__main__":
    main()
