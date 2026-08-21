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
