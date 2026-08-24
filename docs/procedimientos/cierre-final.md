# Cierre final de sesión

Actualiza automáticamente el archivo de sesión con horas reales de commits.

## Uso

```bash
python3 scripts/cierre-final.py [--fecha YYYY-MM-DD]
```

## Qué hace

1. Lee todos los commits del día
2. Calcula horas exactas (primer y último commit)
3. Calcula duración real
4. Actualiza el archivo `docs/sesiones/YYYY-MM-DD.md`
5. Indica comandos para commitear

## Cuándo usar

- Al terminar cada sesión de trabajo
- Después de hacer todos los commits del día

## Relacionado con

- [scripts/cierre-final.py](../../scripts/cierre-final.py)
- [cierre-completo.md](cierre-completo.md) — cierre completo (contexto, changelog, etc.)
- [cierre-sesion.md](cierre-sesion.md) — checklist manual de cierre
