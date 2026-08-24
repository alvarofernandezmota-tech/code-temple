# Índice de docs/

Documentación de code-temple, organizada según Diátaxis (procedimientos = how-to,
ecosistema/estandares/infra = referencia, adr = explicación) + sesiones como log de trabajo.

## Estructura

| Carpeta | Qué contiene | README |
|---|---|---|
| `adr/` | Decisiones de arquitectura (por qué se decidió X), numeración secuencial | [adr/README.md](adr/README.md) |
| `procedimientos/` | Guías how-to, cada una conectada 1:1 con un script en `scripts/` | [procedimientos/README.md](procedimientos/README.md) |
| `ecosistema/` | Estado vivo del ecosistema de repos (qué existe, para qué sirve) | [ecosistema/README.md](ecosistema/README.md) |
| `estandares/` | Convenciones de formato (frontmatter, nombres, etc.) | [estandares/README.md](estandares/README.md) |
| `infra/` | Referencia de las máquinas físicas (acer, madre) | [infra/README.md](infra/README.md) |
| `sesiones/` | Log de trabajo diario, un archivo por día | [sesiones/README.md](sesiones/README.md) |
| `_archivo/` | Todo lo que ya no aplica, conservado por historial | [_archivo/README.md](_archivo/README.md) |

## Regla de oro

Ningún documento vive fuera de estas 7 carpetas. Si un doc de `ecosistema/` queda
resuelto, se mueve a `_archivo/` en la MISMA sesión en que se resuelve (ver ADR-004).

Ver también: [AGENTS.md](../AGENTS.md), [CONTEXT.md](../CONTEXT.md)

## Estructura real (árbol)

docs/
├── README.md ← índice maestro (este archivo)
├── adr/
│ ├── README.md
│ ├── 001-bifrost-desde-cero.md
│ ├── 002-plantilla-repo-scripts-procedimientos.md ⚠ duplica número con el siguiente
│ ├── 002-regla-enganche-cuadruple.md ⚠ pendiente renumerar (issue #54)
│ └── 003-orden-rollout-formatter.md
├── procedimientos/
│ ├── README.md
│ ├── cierre-sesion.md
│ ├── inicio-sesion.md
│ ├── plantilla-repo.md
│ └── plantilla-sesion.md
├── ecosistema/
│ ├── README.md ⚠ no lista todos los archivos (pendiente)
│ ├── fuente-de-verdad.md
│ ├── infra-madre.md ⚠ solapa con infra/madre/ (issue #52)
│ ├── pendiente-proxima-sesion.md ⚠ pendiente archivar (issue #55)
│ ├── plan-bot.md
│ ├── repos-activos.md
│ ├── repos-archivados.md
│ └── vision.md
├── estandares/
│ ├── README.md
│ └── frontmatter.md
├── infra/
│ ├── README.md
│ ├── acer/ (sin explorar en detalle aún)
│ └── madre/
│ ├── README.md
│ ├── auditoria/
│ ├── estado/
│ └── sistema/
├── sesiones/
│ ├── README.md
│ ├── 2026/ ⚠ nombres inconsistentes (issue #59)
│ └── scripts/ ⚠ ubicación incorrecta (debería ir en /scripts)
│ ├── README.md
│ └── nueva_sesion.py ⚠ snake_case, no sigue convención kebab-case
└── _archivo/
├── README.md
├── infra-madre-estados-vacios/
├── infra-madre-gestion-proyecto/
├── infra-madre-plantillas-vacias/
└── neural-os-sesion-01/

text

**Nota:** este árbol se actualiza manualmente en cada auditoría. Los ⚠ se quitan
cuando la issue correspondiente se cierra.
