"""
Reorganiza docs/sesiones/ en subcarpetas por mes, igual que se hizo con
diario/personal/ en midgaror.

Mueve archivos y carpetas sueltas con fecha AAAA-MM-DD en el nombre a
docs/sesiones/AAAA/MM-mes/. No toca lo que ya esté organizado, ni lo que
no tenga fecha reconocible (como neural-os-sesion-01/).
"""

import re
import shutil
from pathlib import Path

RAIZ = Path(__file__).parent / "docs" / "sesiones"

MESES = {
    "01": "enero", "02": "febrero", "03": "marzo", "04": "abril",
    "05": "mayo", "06": "junio", "07": "julio", "08": "agosto",
    "09": "septiembre", "10": "octubre", "11": "noviembre", "12": "diciembre",
}

PATRON_FECHA = re.compile(r"(\d{4})-(\d{2})-(\d{2})")


def mover(origen: Path) -> None:
    match = PATRON_FECHA.search(origen.name)
    if not match:
        print(f"⚠️  Sin fecha reconocible, no se mueve: {origen.name}")
        return
    anio, mes, _ = match.groups()
    nombre_mes = MESES.get(mes)
    if not nombre_mes:
        print(f"⚠️  Mes no reconocido en: {origen.name}")
        return
    carpeta_destino = RAIZ / anio / f"{mes}-{nombre_mes}"
    carpeta_destino.mkdir(parents=True, exist_ok=True)
    destino = carpeta_destino / origen.name
    if destino.exists():
        print(f"⚠️  Ya existe destino, revisa a mano: {destino}")
        return
    shutil.move(str(origen), str(destino))
    print(f"  {origen.name} -> {destino.relative_to(RAIZ)}")


def main() -> None:
    for item in sorted(RAIZ.iterdir()):
        if item.name in ("README.md",) or item.name.isdigit() or (item.is_dir() and re.match(r"^\d{4}$", item.name)):
            continue
        if item.is_file() or item.is_dir():
            mover(item)


if __name__ == "__main__":
    main()
