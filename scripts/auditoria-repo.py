"""
Audita la estructura documental de code-temple (no el sistema Madre,
eso lo hace docs/infra/madre/auditoria/auditoria.py aparte).

Comprueba que todos los links relativos en Markdown dentro de docs/,
AGENTS.md y CONTEXT.md apuntan a archivos que existen de verdad.
Tambien comprueba que todo .md en docs/ecosistema, docs/adr,
docs/procedimientos y docs/estandares esta registrado en
scripts/generar-contexto.py (ARCHIVOS), para que el volcado de
contexto nunca se quede desactualizado en silencio.
No modifica nada, solo reporta lo que no coincide.

Uso: python scripts/auditoria-repo.py
"""
import re
from pathlib import Path

RAIZ = Path(__file__).parent.parent
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
CARPETAS_REGISTRADAS = [
    "docs/ecosistema", "docs/adr", "docs/procedimientos", "docs/estandares"
]

def archivos_markdown():
    yield RAIZ / "AGENTS.md"
    yield RAIZ / "CONTEXT.md"
    yield from (p for p in RAIZ.glob("docs/**/*.md") if "_archivo" not in p.parts)

def enlaces_rotos():
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
    return problemas

def archivos_registrados_en_contexto():
    ruta = RAIZ / "scripts" / "generar-contexto.py"
    texto = ruta.read_text(encoding="utf-8")
    bloque = texto.split("ARCHIVOS = [", 1)[1].split("]", 1)[0]
    return {linea.strip().strip('",') for linea in bloque.splitlines() if linea.strip()}

def archivos_huerfanos():
    registrados = archivos_registrados_en_contexto()
    problemas = []
    for carpeta in CARPETAS_REGISTRADAS:
        for p in (RAIZ / carpeta).glob("*.md"):
            rel = str(p.relative_to(RAIZ))
            if rel not in registrados:
                problemas.append(f"{rel}: existe pero no esta en ARCHIVOS de generar-contexto.py")
    return problemas

def main():
    problemas = enlaces_rotos() + archivos_huerfanos()
    if not problemas:
        print("Todos los enlaces relativos resuelven correctamente y ARCHIVOS esta al dia.")
    else:
        print(f"{len(problemas)} problema(s):")
        for p in problemas:
            print(f"  - {p}")

if __name__ == "__main__":
    main()
