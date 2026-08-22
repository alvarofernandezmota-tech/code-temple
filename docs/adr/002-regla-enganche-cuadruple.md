---
tipo: decision
fecha: 2026-08-22
repo: code-temple
etiquetas: [arquitectura, mantenimiento]
relacionado: [AGENTS.md, docs/procedimientos/cierre-sesion.md]
---

# ADR 002: Regla de enganche cuádruple para carpetas nuevas de docs/

## Contexto
Durante la sesion del 2026-08-22 se descubrio repetidamente que crear
una carpeta nueva en docs/ (ecosistema, adr, procedimientos) no basta
por si solo: si no se referencia desde otros puntos del repo, queda
huerfana en la practica aunque el archivo exista.

## Decision
Toda carpeta nueva bajo docs/ debe engancharse en los cuatro sitios
a la vez, en el mismo commit:
1. Mapa de directorios de AGENTS.md
2. Regla de mantenimiento de AGENTS.md (si genera contenido que la IA
   deba conocer)
3. Indice de docs/ecosistema/README.md
4. Lista ARCHIVOS de scripts/generar-contexto.py

## Motivo
Sin esta regla, cada carpeta nueva repite el mismo ciclo de "se crea,
se olvida, se descubre roto en la siguiente auditoria" que ya paso
tres veces hoy (scripts/, docs/adr/, docs/procedimientos/).

## Estado
Aceptado — 2026-08-22.
