"""
Auditoría de Madre — de solo lectura, no modifica nada.

Ejecuta los mismos chequeos que revisar-madre.sh pero además compara
los datos reales contra lo que ya está escrito en sistema.md, software.md
y docker.md, e imprime solo lo que NO coincide. No escribe en ningun .md.

Uso: python3 docs/infra/madre/scripts/auditoria.py
"""

import re
import subprocess
from pathlib import Path

RAIZ = Path(__file__).parent.parent


def ejecutar(comando: str) -> str:
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    return resultado.stdout.strip()


def leer_md(nombre: str) -> str:
    return (RAIZ / nombre).read_text(encoding="utf-8")


def comprobar_sistema() -> list[str]:
    avisos = []
    kernel_real = ejecutar("uname -r")
    contenido = leer_md("sistema.md")
    if kernel_real and kernel_real not in contenido:
        avisos.append(f"sistema.md desactualizado: kernel real es {kernel_real}")
    return avisos


def comprobar_paquetes() -> list[str]:
    avisos = []
    explicitos_real = ejecutar("pacman -Qe | wc -l")
    contenido = leer_md("software.md")
    match = re.search(r"Expl[íi]citos:\s*(\d+)", contenido)
    if match and match.group(1) != explicitos_real:
        avisos.append(
            f"software.md desactualizado: dice {match.group(1)} explícitos, "
            f"el real es {explicitos_real}"
        )
    return avisos


def comprobar_docker() -> list[str]:
    avisos = []
    version_real = ejecutar("docker --version")
    contenido = leer_md("docker.md")
    if version_real and version_real.split(",")[0].split()[-1] not in contenido:
        avisos.append(f"docker.md podría estar desactualizado: docker real reporta '{version_real}'")
    return avisos


def main() -> None:
    avisos = comprobar_sistema() + comprobar_paquetes() + comprobar_docker()
    if not avisos:
        print("Todo coincide. Nada que corregir a mano.")
        return
    print(f"{len(avisos)} discrepancia(s) encontrada(s):")
    for aviso in avisos:
        print(f"  - {aviso}")


if __name__ == "__main__":
    main()
