"""
Crea (o abre si ya existe) el archivo de sesion del dia en su carpeta de
mes, y lo abre en el editor para escribir. No toca sesiones existentes de
otros dias.

Uso:
  python3 nueva_sesion.py hoy                  -> docs/sesiones/AAAA/MM-mes/AAAA-MM-DD.md
  python3 nueva_sesion.py "nombre-corto-sesion" -> docs/sesiones/AAAA/MM-mes/AAAA-MM-DD-nombre-corto.md
"""

import os
import subprocess
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).parent.parent

MESES = {
    1: "enero", 2: "febrero", 3: "marzo", 4: "abril",
    5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
    9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre",
}


def ruta_carpeta_mes(hoy: date) -> Path:
    carpeta = RAIZ / str(hoy.year) / f"{hoy.month:02d}-{MESES[hoy.month]}"
    carpeta.mkdir(parents=True, exist_ok=True)
    return carpeta


def crear_o_abrir_sesion(nombre_corto: str | None) -> Path:
    hoy = date.today()
    carpeta_mes = ruta_carpeta_mes(hoy)

    if nombre_corto:
        nombre_archivo = f"{hoy.isoformat()}-{nombre_corto}.md"
    else:
        nombre_archivo = f"{hoy.isoformat()}.md"

    destino = carpeta_mes / nombre_archivo

    if destino.exists():
        print(f"Ya existe, abriendo: {destino.relative_to(RAIZ)}")
        return destino

    titulo = f"{hoy.isoformat()}" + (f" - {nombre_corto}" if nombre_corto else "")
    plantilla = f"""# Sesion {titulo}

## Objetivo

## Contexto

## Decisiones

## Cierre
"""
    destino.write_text(plantilla, encoding="utf-8")
    print(f"Creada: {destino.relative_to(RAIZ)}")
    return destino


def abrir_en_editor(ruta: Path) -> None:
    editor = os.environ.get("EDITOR", "nano")
    subprocess.call([editor, str(ruta)])


def main() -> None:
    if len(sys.argv) < 2:
        print('Uso: python3 nueva_sesion.py hoy   |   python3 nueva_sesion.py "nombre-corto"')
        sys.exit(1)

    argumento = sys.argv[1].strip().lower()
    nombre_corto = None if argumento == "hoy" else argumento.replace(" ", "-")

    destino = crear_o_abrir_sesion(nombre_corto)
    abrir_en_editor(destino)


if __name__ == "__main__":
    main()
