# Cierre de sesión

Checklist al terminar de trabajar en code-temple.

## Pasos obligatorios

1. [ ] Correr `python scripts/auditoria-repo.py` y confirmar 0 problemas (o los rotos esperados, como docs/_archivo)
2. [ ] Rellenar `docs/sesiones/AAAA/MM-mes/AAAA-MM-DD.md` con Objetivo, Hecho y Pendiente para la próxima sesión (frontmatter incluido)
3. [ ] Si hubo decisión de arquitectura → crear `docs/adr/NNN-titulo.md`
4. [ ] Si se creó/modificó algo en docs/ecosistema/, docs/adr/ o docs/estandares/ → actualizar `scripts/generar-contexto.py` (ARCHIVOS)
5. [ ] **Revisar mantenimiento:** comprobar docs/ecosistema/ y docs/adr/ por archivos obsoletos (si hay algo resuelto → archivar a docs/_archivo/)
6. [ ] Commitear y pushear

## Relacionado con

- [inicio-sesion.md](inicio-sesion.md) — checklist de inicio
- [plantilla-sesion.md](plantilla-sesion.md) — plantilla para documentar la sesión
- [auditoria-repo.md](auditoria-repo.md) — cómo usar el script de auditoría
- [mantenimiento-documentacion.md](mantenimiento-documentacion.md) — matriz evento→archivo a actualizar
