# Cierre de sesión

Checklist al terminar de trabajar en code-temple.

## Pasos obligatorios

1. [ ] Correr `python3 scripts/auditoria-repo.py` y confirmar 0 problemas (o los rotos esperados, como docs/_archivo)
2. [ ] **Actualizar AGENTS.md y CONTEXT.md:** `python3 scripts/actualizar-agents-context.py` (para reflejar cambios estructurales)
3. [ ] Rellenar `docs/sesiones/AAAA/MM-mes/AAAA-MM-DD.md` con Objetivo, Hecho y Pendiente para la próxima sesión (frontmatter incluido)
4. [ ] Si hubo decisión de arquitectura → crear `docs/adr/NNN-titulo.md`
5. [ ] Si se creó/modificó algo en docs/ecosistema/, docs/adr/ o docs/estandares/ → actualizar `scripts/generar-contexto.py` (lista ARCHIVOS)
6. [ ] **Revisar mantenimiento:** comprobar docs/ecosistema/ y docs/adr/ por archivos obsoletos (si hay algo resuelto → archivar a docs/_archivo/)
7. [ ] **Actualizar CHANGELOG.md:** añadir entry con cambios de la sesión
8. [ ] Commitear y pushear

## Relacionado con

- [inicio-sesion.md](inicio-sesion.md) — checklist de inicio
- [plantilla-sesion.md](plantilla-sesion.md) — plantilla para documentar la sesión
- [auditoria-repo.md](auditoria-repo.md) — cómo usar el script de auditoría
- [actualizar-agents-context.md](actualizar-agents-context.md) — actualizar AGENTS.md y CONTEXT.md
- [mantenimiento-documentacion.md](mantenimiento-documentacion.md) — matriz evento→archivo a actualizar
