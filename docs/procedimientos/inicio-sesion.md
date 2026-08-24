# Inicio de sesión

Checklist al empezar a trabajar en code-temple.

## Pasos obligatorios

1. [ ] Leer `docs/sesiones/AAAA/MM-mes/AAAA-MM-DD-previo.md` (última sesión) para ver pendientes heredados
2. [ ] **Revisar AGENTS.md y CONTEXT.md:** verificar que reflejan la estructura actual (si no, ejecutar `python3 scripts/actualizar-agents-context.py`)
3. [ ] **Generar contexto:** `python3 scripts/generar-contexto.py` (leer AGENTS.md, CONTEXT.md, docs/ecosistema/*, docs/adr/*, frontmatter.md, procedimientos clave) antes de nada más del ecosistema
4. [ ] **Generar estructura:** `python3 scripts/generar-estructura.py` (para ver árbol completo actualizado)
5. [ ] Revisar "Pendiente próxima sesión" del último archivo en docs/sesiones/ y de docs/ecosistema/ (si existe)
6. [ ] `python3 scripts/auditoria-repo.py` para confirmar 0 problemas heredados de la sesión anterior
7. [ ] **Revisar mantenimiento:** comprobar docs/README.md y docs/[carpeta]/README.md por actualizaciones pendientes (ver mantenimiento-documentacion.md)
8. [ ] Crear `docs/sesiones/AAAA/MM-mes/AAAA-MM-DD.md` con frontmatter (usar plantilla-sesion.md)

## Relacionado con

- [cierre-sesion.md](cierre-sesion.md) — checklist de cierre
- [plantilla-sesion.md](plantilla-sesion.md) — plantilla para documentar la sesión
- [generar-contexto.md](generar-contexto.md) — cómo usar el script de contexto
- [actualizar-agents-context.md](actualizar-agents-context.md) — actualizar AGENTS.md y CONTEXT.md
- [mantenimiento-documentacion.md](mantenimiento-documentacion.md) — matriz evento→archivo a actualizar
