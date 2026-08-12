# Pull Requests (PRs)

## ¿Qué es un PR?
Un Pull Request (PR) es una solicitud formal para fusionar cambios de una rama a otra en GitHub.

## ¿Cuándo usar PRs?
- ✅ Nuevas funcionalidades
- ✅ Corrección de bugs
- ✅ Cambios importantes en la infraestructura
- ✅ Cambios que requieren revisión

## ¿Cuándo NO usar PRs?
- ❌ Cambios menores (documentación, typos)
- ❌ Cambios automatizados (workflows)
- ❌ Cambios urgentes (hotfixes)

## Flujo de trabajo
1. Crear rama: `git checkout -b feature/nueva-funcionalidad`
2. Hacer cambios y commit
3. Push: `git push origin feature/nueva-funcionalidad`
4. Crear PR en GitHub
5. Esperar revisión
6. Merge a main

## Plantilla de PR
- Título descriptivo
- Descripción de cambios
- Referencia a issues (Refs: #XX)
- Checklist de verificación
