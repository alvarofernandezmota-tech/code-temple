# Actualizar pie de sesiones

Actualiza automáticamente el pie de página de TODOS los archivos de sesión.

## Uso

```bash
python3 scripts/actualizar-pie-sesiones.py
```

## Qué hace

Para cada archivo de sesión:
1. Obtiene primer y último commit del día
2. Calcula horas de trabajo
3. Identifica autor
4. Añade pie de página estandarizado
5. Incluye última actualización

## Cuándo usar

- Al final de cada sesión
- Cuando se actualizan archivos de sesiones antiguas
- En auditorías trimestrales

## Formato del pie

```markdown
***

**Fin de sesión YYYY-MM-DD**

- **Primer commit:** abc1234 (2026-08-24 16:04)
- **Último commit:** def5678 (2026-08-24 18:38)
- **Horas de trabajo:** 2 horas 34 minutos
- **Autor:** Tu Nombre
- **Total commits:** 58
- **Última actualización:** 2026-08-24 18:42 CEST
```

## Relacionado con

- [scripts/actualizar-pie-sesiones.py](../../scripts/actualizar-pie-sesiones.py)
- [cierre-final.md](cierre-final.md) — cierre de sesión individual
- [plantilla-sesion.md](plantilla-sesion.md) — plantilla de sesiones
