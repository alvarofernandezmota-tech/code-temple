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
