---
tipo: procedimiento
fecha: 2026-08-22
repo: code-temple
etiquetas: [procedimiento]
---

# Procedimiento: cerrar una sesion de trabajo

1. Correr `python scripts/auditoria-repo.py` y confirmar 0 (o los
   rotos esperados y ya conocidos, como docs/_archivo).
2. Rellenar `docs/sesiones/AAAA/MM-mes/AAAA-MM-DD.md` con Objetivo,
   Hecho y Pendiente para la proxima sesion (frontmatter incluido).
3. Si hubo una decision de arquitectura, crear `docs/adr/NNN-titulo.md`.
4. Si se creo o modifico algo en docs/ecosistema/, docs/adr/ o
   docs/estandares/, actualizar `scripts/generar-contexto.py` (ARCHIVOS)
   en el mismo commit.
5. Verificar cada commit contra GitHub (get_commit) antes de darlo
   por bueno, no solo confiar en la salida de la terminal local.
6. Si se quiere dejar registro trazable, crear un Issue cerrado por
   cambio importante, referenciando el hash del commit.
