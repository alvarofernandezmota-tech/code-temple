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
│ └── personal/ # Entradas del diario (YYYY/MM-mes/YYYY-MM-DD.md)
│ └── bifrost/ # bifrost local (GitHub: alvarofernandezmota-tech/bifrost)
│ ├── AGENTS.md
│ ├── CONTEXT.md
│ └── README.md
└── work/ # NO EXISTE aún — futuro espacio para repos de trabajo

text

## Dependencias entre componentes

| Componente | Ruta local | Repo GitHub | Depende de |
|------------|-----------|-------------|------------|
| `diario.py` | `~/GitHub/personal/midgaror/diario/diario.py` | `midgaror` | — |
| `bifrost` (bot) | `~/GitHub/personal/midgaror/diario/bifrost/` | `bifrost` | `diario.py` |
| `code-temple` (docs) | `~/GitHub/personal/code-temple/` | `code-temple` | — |

## Reglas de ubicación

1. **Repos personales** (midgaror, bifrost) → `~/GitHub/personal/`
2. **Repos de trabajo** (thea-ia, ai-toolkit, etc.) → `~/GitHub/work/` (crear cuando exista el primer repo de trabajo)
3. **Documentación del ecosistema** → siempre en `code-temple/docs/ecosistema/`

## Próximos pasos

- [ ] Crear `~/GitHub/work/` y mover repos de trabajo allí (thea-ia, ai-toolkit, image-calculator, THDORA-PERSONAL).
- [ ] Clonar bifrost en `~/GitHub/work/bifrost/` (ubicación definitiva, separada de midgaror).
- [ ] Actualizar bifrost para que llame a `../midgaror/diario/diario.py` desde su nueva ubicación.
