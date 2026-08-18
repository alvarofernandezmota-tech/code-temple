"""
Crea el archivo de una sesion nueva en la carpeta del mes correspondiente,
con la plantilla minima ya rellenada, y lo abre directamente en el editor
para escribir. No toca sesiones existentes.

Uso: python3 docs/sesiones/scripts/nueva_sesion.py "nombre-corto-sesion"
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


def crear_sesion(nombre_corto: str) -> Path:
    hoy = date.today()
    carpeta_mes = RAIZ / str(hoy.year) / f"{hoy.month:02d}-{MESES[hoy.month]}"
    carpeta_mes.mkdir(parents=True, exist_ok=True)

    nombre_archivo = f"{hoy.isoformat()}-{nombre_corto}.md"
    destino = carpeta_mes / nombre_archivo

    if destino.exists():
        print(f"Ya existe: {destino.relative_to(RAIZ)}")
        return destino

    plantilla = f"""# Sesion {hoy.isoformat()} - {nombre_corto}

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
        print('Uso: python3 nueva_sesion.py "nombre-corto-sesion"')
        sys.exit(1)
    nombre_corto = sys.argv[1].strip().lower().replace(" ", "-")
    destino = crear_sesion(nombre_corto)
    abrir_en_editor(destino)


if __name__ == "__main__":
    main()
