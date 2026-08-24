# Generar contexto para IA

**Script asociado:** `scripts/generar-contexto.py`

## Cuándo usar

Al empezar una sesión nueva (ver `inicio-sesion.md`), antes de tocar cualquier doc del ecosistema.

## Cómo usar

```bash
cd ~/GitHub/personal/code-temple
python scripts/generar-contexto.py
```

## Qué hace

Volcado de contexto a IA: lee todos los archivos críticos del repo (AGENTS.md, CONTEXT.md, docs/ecosistema/*, docs/adr/*, docs/estandares/frontmatter.md, procedimientos clave) y genera un prompt unificado para pasar a la IA.

## Salida esperada

- Texto plano en stdout, listo para copiar y pegar en el chat con la IA
- Incluye: estado del repo, decisiones recientes (ADR), estándares activos, procedimientos vigentes

## Relacionado con

- [inicio-sesion.md](inicio-sesion.md) — checklist de inicio (paso 2: generar contexto)
- [scripts/README.md](../../scripts/README.md) — índice de scripts
- [docs/ecosistema/README.md](../ecosistema/README.md) — qué archivos del ecosistema se incluyen
- [docs/adr/README.md](../adr/README.md) — qué ADRs se incluyen
