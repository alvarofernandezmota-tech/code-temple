# Infra-madre — Mapa físico del ecosistema

## Estructura de carpetas en el servidor

/home/varopc/GitHub/
├── personal/
│ ├── code-temple/ # code-temple (GitHub: alvarofernandezmota-tech/code-temple)
│ │ └── docs/
│ │ ├── ecosistema/ # Documentación de infraestructura
│ │ │ ├── repos-activos.md # Lista de repos en GitHub
│ │ │ ├── infra-madre.md # Este archivo — mapa físico
│ │ │ └── fuente-de-verdad.md # Qué repo es la fuente de verdad para cada cosa
│ │ └── sesiones/ # Diario de trabajo
│ └── midgaror/ # midgaror (GitHub: alvarofernandezmota-tech/midgaror)
│ └── diario/
│ ├── diario.py # Función escribir_entrada() usada por bifrost
│ ├── tareas/ # tareas.py + datos/
│ ├── habitos/ # habitos.py + datos/
│ ├── personal/ # Entradas del diario (AAAA/MM-mes/AAAA-MM-DD.md)
│ └── bifrost/ # bifrost local (GitHub: alvarofernandezmota-tech/bifrost)
│ ├── AGENTS.md
│ ├── CONTEXT.md
│ └── README.md

/home/varopc/GitHub/trabajo/
├── code-temple/ # code-temple (otra copia local, en servidor de trabajo)
├── theodora/ # THDORA-PERSONAL (GitHub)
├── yggdrasil-dew/ # yggdrasil-dew (GitHub, archivado)
└── ... # Futuros repos de trabajo (thea-ia, ai-toolkit, etc. — aún no clonados)

text

## Dependencias entre componentes

| Componente | Ruta local | Repo GitHub | Depende de |
|------------|-----------|-------------|------------|
| `diario.py` | `~/GitHub/personal/midgaror/diario/diario.py` | `midgaror` | — |
| `bifrost` (bot) | `~/GitHub/personal/midgaror/diario/bifrost/` | `bifrost` | `diario.py` |
| `code-temple` (docs) | `~/GitHub/personal/code-temple/` | `code-temple` | — |

## Reglas de ubicación

1. **Repos personales** (midgaror, bifrost) → `~/GitHub/personal/`
2. **Repos de trabajo** (thea-ia, ai-toolkit, THDORA-PERSONAL, etc.) → `~/GitHub/trabajo/` (clonar cuando se necesiten)
3. **Documentación del ecosistema** → siempre en `code-temple/docs/ecosistema/`

## Estado actual

- [x] bifrost clonado en `~/GitHub/personal/midgaror/diario/bifrost/`
- [ ] bifrost en `~/GitHub/trabajo/bifrost/` (mover cuando se decida separación total)
- [ ] Repos de trabajo clonados en `~/GitHub/trabajo/` (thea-ia, ai-toolkit, image-calculator, THDORA-PERSONAL)
