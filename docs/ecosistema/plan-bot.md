# Plan: conectar midgaror y code-temple con un bot

## Fase 0 — Auditoría (hecho 2026-08-21)
Revisados los 22 repos, identificados 8 activos y 14 archivados.
Detectado solape con THDORA-PERSONAL, local-brain y ollama-stack.

## Fase 1 — Decidir base
Revisar THDORA-PERSONAL (código + issues) antes de crear repo nuevo.
Decidir: reutilizar o crear bifrost desde cero.

## Fase 2 — Bot conector (bifrost o adaptación de THDORA-PERSONAL)
Telegram + PyGithub, comando /hoy para escribir en midgaror y code-temple.
Correr como servicio systemd en Madre, sin Docker de momento.

## Fase 3 — Estandarizar datos
Aplicar docs/estandares/frontmatter.md a diario.py y nueva_sesion.py.

## Fase 4 — Monitorización (heimdall)
Bot separado que vigila estado de Madre (CPU, disco, Docker, servicios).

## Fase 5 — Obsidian
Vault que enlaza midgaror, code-temple y notas propias vía frontmatter.

## Fase 6 — Mimir (Ollama + RAG)
Revisar local-brain y ollama-stack antes de construir desde cero.
Indexar vault de Obsidian + repos con embeddings para que Ollama entienda
todo el ecosistema.

## Regla de este plan
No se empieza una fase sin cerrar la anterior con commit y documentación.

## Decisión Fase 2 (2026-08-21)
Bifrost se construye primero solo para midgaror (diario personal).
No se toca code-temple hasta que el bot funcione de forma estable
en midgaror durante un tiempo de uso real.

### Fase 2a — Bifrost mínimo (solo midgaror)
- Comando /hoy <texto> -> crea/actualiza diario/personal/AAAA/MM-mes/AAAA-MM-DD.md
- Solo tu chat_id de Telegram autorizado
- Sin base de datos, sin systemd todavía: correr en foreground para probar

### Fase 2b — Estabilizar
- Correr como servicio systemd en Madre
- Manejo de errores (token caducado, repo inaccesible, rate limit de GitHub)
- Uso real durante al menos 1-2 semanas

### Fase 2c — Extender a code-temple
- Solo después de 2a y 2b validadas
- Comando /sesion <texto> -> nueva_sesion.py equivalente vía bot

## Regla de arquitectura bifrost (2026-08-21)
Bifrost es solo interfaz, nunca lógica. Toda función nueva (diario,
tareas, hábitos) se construye y prueba primero como script en
midgaror. Bifrost solo expone esa función ya validada como comando
de Telegram, sin reimplementarla.

## Pendiente próxima sesión
Auditar que todo lo documentado hoy (infra madre, ecosistema, plan
bifrost) sigue siendo cierto antes de seguir avanzando.
