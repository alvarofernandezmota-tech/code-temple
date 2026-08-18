# Scripts de Madre

## revisar-madre.sh

Script de solo lectura. No modifica nada, no se ejecuta solo (sin cron, sin
GitHub Action). Se lanza a mano:

bash docs/infra/madre/scripts/revisar-madre.sh

Imprime kernel, hostname, distro, resumen y lista completa de paquetes,
versión de Docker/Compose con contenedores e imágenes, y un árbol de las
carpetas relevantes del servidor.
