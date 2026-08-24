# Infraestructura física

Referencia de las máquinas físicas donde vive el ecosistema.

## Estructura

docs/infra/
├── README.md
├── acer/
│   └── estado.md                     ⚠ pendiente de auditoría
└── madre/
    ├── README.md
    ├── auditoria/
    │   ├── auditoria.py
    │   └── revisar-madre.sh
    ├── estado/
    │   ├── cambios.md
    │   └── estado.md
    └── sistema/
        ├── estructura.md
        ├── programas.md
        └── software.md

## Índice

### acer/
- [estado.md](acer/estado.md) — estado de la máquina Acer (pendiente de auditoría completa)

### madre/
- [README.md](madre/README.md) — índice de la carpeta madre/
- [auditoria/auditoria.py](madre/auditoria/auditoria.py) — script de auditoría automática
- [auditoria/revisar-madre.sh](madre/auditoria/revisar-madre.sh) — script de revisión manual
- [estado/cambios.md](madre/estado/cambios.md) — registro de cambios en la máquina
- [estado/estado.md](madre/estado/estado.md) — estado actual del sistema
- [sistema/estructura.md](madre/sistema/estructura.md) — árbol de directorios del sistema
- [sistema/programas.md](madre/sistema/programas.md) — programas instalados
- [sistema/software.md](madre/sistema/software.md) — software y servicios

## Relacionado con

- [docs/ecosistema/repos-activos.md](../ecosistema/repos-activos.md) — qué repos corren en cada máquina
- [docs/procedimientos/mantenimiento-documentacion.md](../procedimientos/mantenimiento-documentacion.md) — cuándo actualizar esta docs (issue #57)
- [docs/procedimientos/plantilla-readme.md](../procedimientos/plantilla-readme.md) — plantilla usada para este README
