# Mantenimiento de documentación

**Cuándo usar:** Cada vez que se modifique la estructura del repo (añadir carpeta, mover archivos, cambiar convención) o se actualice contenido crítico.

## Matriz evento → archivo a actualizar

| Evento | Archivo(s) a actualizar | Dónde comprobarlo |
|---|---|---|
| Añadir carpeta nueva en `docs/` | `docs/README.md` (árbol de estructura), `docs/[carpeta]/README.md` (nuevo) | `docs/README.md` sección "Estructura real" |
| Mover/archivar archivo en `docs/` | `docs/[carpeta]/README.md` (índice), `docs/_archivo/README.md` (si se archivó) | README de la carpeta origen y destino |
| Cambiar convención de nombres | `docs/procedimientos/plantilla-sesion.md` o `plantilla-repo.md`, `docs/README.md` | `docs/procedimientos/` y `docs/README.md` |
| Actualizar infra de Madre | `docs/infra/madre/estado/cambios.md`, `docs/infra/madre/sistema/*.md` | `docs/infra/madre/estado/` |
| Crear ADR nuevo | `docs/adr/README.md` (índice), `docs/README.md` (si cambia estructura) | `ls docs/adr/ | sort -V | tail -1` para último número |
| Actualizar scripts/ | `scripts/README.md`, `docs/procedimientos/README.md` (si hay 1:1) | `ls scripts/*.py` |

## Reglas obligatorias

1. **Último número de ADR:** Antes de crear un ADR nuevo, comprobar con `ls docs/adr/ | sort -V | tail -1` y usar el siguiente número secuencial.
2. **Índice maestro:** `docs/README.md` debe reflejar SIEMPRE la estructura real de `docs/`. Actualizar en cada commit que toque `docs/`.
3. **README por carpeta:** Cada carpeta en `docs/` debe tener su README con diagrama vertical + índice de archivos.
4. **Documentar en sesión:** Cada cambio estructural debe quedar registrado en `docs/sesiones/YYYY/MM-mes/YYYY-MM-DD.md` con commit y razón.

## Checklist de mantenimiento (al final de cada sesión)

- [ ] Revisar `docs/ecosistema/` y `docs/adr/` por archivos obsoletos (si hay algo resuelto → archivar a `docs/_archivo/`)
- [ ] Verificar que `docs/README.md` coincide con `tree docs/` real
- [ ] Confirmar que todo README de carpeta tiene índice actualizado
- [ ] Si se tocó infra/madre → actualizar `docs/infra/madre/estado/cambios.md`

## Relacionado con

- [cierre-sesion.md](cierre-sesion.md) — checklist de cierre (paso 5: revisar mantenimiento)
- [inicio-sesion.md](inicio-sesion.md) — checklist de inicio (paso 5: confirmar 0 problemas heredados)
- [auditoria-repo.md](auditoria-repo.md) — auditoría automática (verifica estructura)
- [docs/adr/004-convencion-scripts-procedimientos.md](../adr/004-convencion-scripts-procedimientos.md) — convención 1:1
- [docs/adr/002-regla-enganche-cuadruple.md](../adr/002-regla-enganche-cuadruple.md) — regla para carpetas nuevas
