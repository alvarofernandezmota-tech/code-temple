# Scripts de Madre

## revisar-madre.sh

Script de solo lectura. No modifica nada, no se ejecuta solo (sin cron, sin
GitHub Action). Se lanza a mano:

bash docs/infra/madre/scripts/revisar-madre.sh

Imprime kernel, hostname, distro, resumen y lista completa de paquetes,
versión de Docker/Compose con contenedores e imágenes, y un árbol de las
carpetas relevantes del servidor.

## auditoria.py

Complementa a revisar-madre.sh: no solo imprime los datos reales, sino que
los compara contra lo que ya está escrito en sistema.md, software.md y
docker.md, e imprime solo las discrepancias. Tampoco escribe en ningún .md.

python3 docs/infra/madre/scripts/auditoria.py
