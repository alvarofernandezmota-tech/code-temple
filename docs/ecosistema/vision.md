# Visión final del ecosistema bot

No es solo un conector de commits. El destino es un acompañante
personal que:

1. Entiende lenguaje natural, sin depender de comandos rígidos
   (Ollama local, Fase 6)
2. Recuerda el historial real del usuario — diario, sesiones,
   decisiones pasadas — vía RAG sobre midgaror/code-temple/Obsidian
   (Fase 6, Mimir)
3. Tiene una personalidad definida: cercano, informal, tipo amigo
   que acompaña, no un asistente corporativo de manual

## Por qué se construye por fases y no de golpe

Cada capa (bot->GitHub, luego Obsidian, luego Ollama/RAG, luego
personalidad) se prueba sola primero. Si algo falla, se sabe
exactamente en qué capa está el problema.

## Esta visión no cambia el orden de plan-bot.md

Sigue siendo: Fase 2 (bifrost mínimo) -> Fase 5 (Obsidian) ->
Fase 6 (Ollama, RAG, personalidad). Este documento es el "por qué",
plan-bot.md sigue siendo el "cómo y en qué orden".
