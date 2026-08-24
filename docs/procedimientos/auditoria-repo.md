# Auditoría del repo

**Script asociado:** `scripts/auditoria-repo.py`

## Cuándo usar

Al final de cada sesión de trabajo (ver `cierre-sesion.md`), antes de commitear.

## Cómo usar

```bash
cd ~/GitHub/personal/code-temple
python scripts/auditoria-repo.py
```

## Qué verifica

- Enlaces rotos en docs/
- Archivos sin frontmatter
- Estructura de carpetas (que nada viva fuera de adr/, procedimientos/, ecosistema/, estandares/, infra/, sesiones/, _archivo/)
- READMEs desactualizados

## Salida esperada

- `0` problemas → todo correcto, puedes commitear
- `>0` problemas → revisar y corregir antes de cerrar la sesión

## Relacionado con

- [cierre-sesion.md](cierre-sesion.md) — checklist de cierre (paso 1: correr auditoria)
- [inicio-sesion.md](inicio-sesion.md) — checklist de inicio (paso 4: confirmar 0 problemas heredados)
- [scripts/README.md](../../scripts/README.md) — índice de scripts
