# Inicio de sesión

Checklist al empezar a trabajar en code-temple.

## Pasos obligatorios

1. [ ] Leer `docs/sesiones/AAAA/MM-mes/AAAA-MM-DD-previo.md` (última sesión) para ver pendientes heredados
2. [ ] **Generar contexto:** `python scripts/generar-contexto.py` (leer AGENTS.md, CONTEXT.md, docs/ecosistema/*, docs/adr/*, frontmatter.md, procedimientos clave) antes de nada más del ecosistema
3. [ ] Revisar "Pendiente próxima sesión" del último archivo en docs/sesiones/ y de docs/ecosistema/ (si existe)
4. [ ] `python scripts/auditoria-repo.py` para confirmar 0 problemas heredados de la sesión anterior
5. [ ] **Revisar mantenimiento:** comprobar docs/README.md y docs/[carpeta]/README.md por actualizaciones pendientes (ver mantenimiento-documentacion.md)
6. [ ] Crear `docs/sesiones/AAAA/MM-mes/AAAA-MM-DD.md` con frontmatter (usar plantilla-sesion.md)

## Relacionado con

- [cierre-sesion.md](cierre-sesion.md) — checklist de cierre
- [plantilla-sesion.md](plantilla-sesion.md) — plantilla para documentar la sesión
- [generar-contexto.md](generar-contexto.md) — cómo usar el script de contexto
- [mantenimiento-documentacion.md](mantenimiento-documentacion.md) — matriz evento→archivo a actualizar
