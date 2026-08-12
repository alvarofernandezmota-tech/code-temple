# ADR-001: Estructura de Issues para Documentación de Infraestructura

## Estado
✅ Aceptado

## Contexto
Necesitamos documentar completamente la infraestructura de Madre de forma sistemática y trazable.

## Decisión
Crear una estructura de issues en GitHub (#5-#20) con carpetas correspondientes en `docs/infra/madre/issues/` donde cada issue tenga:
- README.md con progreso
- commands/ con scripts
- outputs/ con resultados
- audit/ con auditorías
- decisions/ con ADRs

## Alternativas consideradas
1. **Documentar todo en un solo archivo**
   - Pros: Simple
   - Contras: Difícil de mantener, no hay trazabilidad

2. **Usar solo issues de GitHub**
   - Pros: Fácil de trackear
   - Contras: Los outputs no están versionados

3. **Estructura actual (elegida)**
   - Pros: Trazabilidad completa, versionado, fácil de auditar
   - Contras: Más archivos

## Consecuencias
- ✅ Cada comando está documentado
- ✅ Los outputs están versionados
- ✅ Fácil auditar el progreso
- ✅ Los ADRs capturan decisiones importantes

## Referencias
- [Issue #16 - Índice Maestro](https://github.com/alvarofernandezmota-tech/code-temple/issues/16)
- [Issue #17 - Estructura](https://github.com/alvarofernandezmota-tech/code-temple/issues/17)
- [Issue #19 - Workflow](https://github.com/alvarofernandezmota-tech/code-temple/issues/19)

## Firmado
- **Decisor:** @alvarofernandezmota-tech
- **Fecha:** 2026-08-12
