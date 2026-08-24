# Infra-madre — Mapa físico del ecosistema

## Separación Trabajo / Personal

| Ámbito | Repos | Ruta local | Propósito |
|--------|-------|-----------|-----------|
| **Personal** | `midgaror`, `bifrost`, `impresion-3d` | `~/GitHub/personal/` | Diario, hábitos, vida privada, hobbies |
| **Trabajo** | `code-temple`, `thea-ia`, `ai-toolkit`, `THDORA-PERSONAL`, `image-calculator` | `~/GitHub/trabajo/` | Infraestructura técnica, proyectos IA, bots, portfolio |

## Estructura completa de carpetas

/home/varopc/GitHub/
├── personal/
│ ├── midgaror/
│ │ └── diario/
│ │ ├── diario.py # Función escribir_entrada()
│ │ ├── tareas/
│ │ ├── habitos/
│ │ ├── personal/ # Entradas del diario
│ │ └── bifrost/ # Bot Telegram (Fase 2a)
│ └── impresion-3d/
└── trabajo/
├── code-temple/ # Documentación del ecosistema
├── theodora/ # THDORA-PERSONAL (bot Telegram antiguo)
└── yggdrasil-dew/ # (archivado)

text

## Cómo acceder a cada componente (comandos rápidos)

### Personal

```bash
# Diario personal
cd ~/GitHub/personal/midgaror/diario
python diario.py hoy                    # Crear/abrir entrada de hoy
python diario.py escribir "texto"       # Añadir texto sin editor (usa bifrost)
python diario.py listar                 # Ver últimas entradas

# Bifrost (bot Telegram)
cd ~/GitHub/personal/midgaror/diario/bifrost
# (aquí irá el código del bot cuando se implemente)
```

### Trabajo

```bash
# code-temple (documentación)
cd ~/GitHub/trabajo/code-temple
cd docs/sesiones/                       # Diario de trabajo
cd docs/ecosistema/                     # Infraestructura

# THDORA-PERSONAL (bot Telegram antiguo)
cd ~/GitHub/trabajo/theodora/
```

## Dependencias entre componentes

| Componente | Ruta local | Repo GitHub | Ámbito | Depende de |
|------------|-----------|-------------|--------|------------|
| `diario.py` | `~/GitHub/personal/midgaror/diario/diario.py` | `midgaror` | Personal | — |
| `bifrost` | `~/GitHub/personal/midgaror/diario/bifrost/` | `bifrost` | Personal | `diario.py` |
| `code-temple` | `~/GitHub/trabajo/code-temple/` | `code-temple` | Trabajo | — |

## Documentación en cada repo

Cada repo debe tener en su `README.md` o `CONTEXT.md`:
1. **Ruta local** donde vive en este servidor.
2. **Ámbito** (trabajo o personal).
3. **Comandos básicos** para acceder y usar sus funciones principales.
