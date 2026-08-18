# ADR-004: Automatización de Documentación

## Estado
Aceptado

## Contexto
Actualmente la documentación se actualiza manualmente. Esto puede generar:
- Olvidos en actualizar `estado.md`
- Índices desactualizados en `README.md`
- Registros incompletos en `cambios.md`

## Decisión
Implementar automatización con GitHub Actions para:
- Actualizar `estado.md` cuando se actualicen carpetas de infra
- Actualizar `README.md` cuando se agreguen/eliminen carpetas
- Actualizar `cambios.md` cuando se hagan merges de PRs

## Alternativas consideradas

### Alternativa 1: Manual (actual)
- **Pros:** Control total, sin dependencias
- **Contras:** Propenso a errores, requiere disciplina

### Alternativa 2: Scripts locales
- **Pros:** Simple, sin dependencias externas
- **Contras:** Requiere ejecución manual, fácil de olvidar

### Alternativa 3: GitHub Actions (elegida)
- **Pros:** Automático, integrado en GitHub, logs disponibles
- **Contras:** Dependencia de GitHub, curva de aprendizaje

## Consecuencias

### Positivas
- Documentación siempre actualizada
- Menos errores humanos
- Trazabilidad en logs de GitHub Actions

### Negativas
- Dependencia de GitHub Actions
- Curva de aprendizaje inicial
- Posibles fallos en automatización

## Fecha
2026-08-12

## Responsables
@alvarofernandezmota-tech
