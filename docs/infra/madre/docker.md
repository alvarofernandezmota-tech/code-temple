# Docker en Madre

## Instalación

- Docker Engine `29.7.1` instalado.
- Docker Compose `5.4.0` instalado.
- containerd `2.3.3`.
- runc `1.5.1`.
- `docker.service` activo y habilitado.
- `containerd.service` activo.

## Estado de inventario

- Contenedores: 0
- Imágenes: 0
- Volúmenes: 0
- Redes estándar: `bridge`, `host`, `none`

## Estructura actual

```text
~/docker/
├── stacks/
│   ├── ia/
│   ├── automation/
│   └── monitoring/
├── data/
└── backups/
```

No se crea ningún stack hasta terminar la documentación de la infraestructura.
