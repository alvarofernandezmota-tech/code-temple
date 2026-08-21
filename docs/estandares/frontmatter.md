# Estándar de frontmatter YAML

Todo archivo .md de diario, sesión o documentación de infra debe llevar
este encabezado YAML. Sin esto, Obsidian y el indexado de Ollama no pueden
relacionar el contenido entre repos.

## Campos obligatorios

- tipo: uno de [diario, sesion, infra, decision, auditoria]
- fecha: formato AAAA-MM-DD
- repo: uno de [midgaror, code-temple, bifrost, heimdall, mimir]

## Campos opcionales

- etiquetas: lista libre, ej. [personal, sevilla, docker, vscode]
- relacionado: lista de rutas a otros .md relacionados (cross-repo)

## Ejemplo

---
tipo: diario
fecha: 2026-08-21
repo: midgaror
etiquetas: [personal, vscode]
---

## Regla

Ningún archivo nuevo se crea sin este encabezado. Los scripts
(diario.py, nueva_sesion.py) deben generarlo automáticamente.

## Pendiente

- Revisar si diario.py y nueva_sesion.py ya generan YAML al crear archivo.
- Si no, actualizarlos antes de aplicar este estándar retroactivamente.
