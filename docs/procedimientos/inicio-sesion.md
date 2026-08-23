---
tipo: procedimiento
fecha: 2026-08-23
repo: code-temple
etiquetas: [procedimiento]
---

# Procedimiento: iniciar una sesion de trabajo

1. `git pull origin main` en cada repo con el que se vaya a trabajar hoy
2. `python scripts/generar-contexto.py` para cargar todo el contexto.
   Esto SIEMPRE empieza leyendo AGENTS.md y CONTEXT.md (son las dos
   primeras entradas de ARCHIVOS) antes de nada mas del ecosistema.
   Ninguna sesion arranca sin pasar primero por estos dos archivos.
3. Revisar "Pendiente proxima sesion" del ultimo archivo en docs/sesiones/
   y de docs/ecosistema/pendiente-proxima-sesion.md
4. `python scripts/auditoria-repo.py` para confirmar 0 problemas heredados
   de la sesion anterior
5. Crear docs/sesiones/AAAA/MM-mes/AAAA-MM-DD-sesion-N.md con frontmatter
   y un `## Objetivo` basado en lo revisado en el paso 3
