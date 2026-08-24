# Plantilla de Repo Nuevo

## Estructura mínima obligatoria

nuevo-repo/
├── AGENTS.md ← Instrucciones para IA (siempre pasa por aquí al iniciar sesión)
├── CONTEXT.md ← Ubicación física y ámbito (personal/trabajo)
├── README.md ← Documentación general del repo
├── docs/
│ ├── procedimientos/
│ │ └── [nombre].md ← Cada procedimiento documentado paso a paso
│ └── sesiones/ ← (opcional, si el repo tiene sesiones propias)
│ └── YYYY/MM-mes/YYYY-MM-DD.md
└── scripts/
└── [nombre].py ← Script que automatiza ese procedimiento

text

## Convención: procedimiento ↔ script

**Regla de oro:** Si un procedimiento tiene automatización, el script debe tener el MISMO nombre base que el documento.

| Procedimiento | Script |
|---------------|--------|
| `docs/procedimientos/organizar-diario.md` | `scripts/organizar_diario.py` |
| `docs/procedimientos/cierre-sesion.md` | `scripts/cierre_sesion.py` (si aplica) |
| `docs/procedimientos/inicio-sesion.md` | `scripts/inicio_sesion.py` (si aplica) |

Esto permite que cualquiera (humano o IA) que lea el `.md` sepa inmediatamente dónde está el código que lo ejecuta.

## Checklist de creación de repo nuevo

1. `git init` (o `create_repository` en GitHub)
2. Crear `AGENTS.md` — instrucciones para que la IA sepa cómo actuar en este repo
3. Crear `CONTEXT.md` — ubicación local (`~/GitHub/personal/X` o `~/GitHub/trabajo/X`) y ámbito
4. Crear `README.md` — qué es el repo, para qué sirve
5. Crear `docs/procedimientos/` (vacío o con el primer procedimiento)
6. Crear `scripts/` (vacío o con el primer script)
7. Primer commit: "Initial commit: estructura base del repo"
8. Registrar el repo en `code-temple/docs/ecosistema/repos-activos.md`

## Ejemplo real (midgaror)

- **Procedimiento:** organizar el diario con coherencia
- **Script:** `scripts/organizar_diario.py`
- **Resultado:** cualquier texto desordenado se convierte en diario estructurado

## Dónde se registra cada repo nuevo

Todo repo nuevo debe aparecer en:

code-temple/docs/ecosistema/repos-activos.md

text

Con: nombre, ubicación local, ámbito (personal/trabajo), propósito, estado (activo/archivado).

## Notas

- No mezclar procedimientos de distintos repos — cada repo es autónomo
- code-temple documenta el ECOSISTEMA (todos los repos), no el detalle interno de cada uno
- Cada repo documenta sus PROPIOS procedimientos y scripts
