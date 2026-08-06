# ADR-002: code-temple como fuente de verdad de Madre

- Estado: aceptado
- Fecha: 2026-08-06
- Área: documentación e infraestructura

## Contexto

Madre necesita una documentación versionada que permita revisar cambios,
auditar el estado y reconstruir el sistema.

## Problema

La documentación dispersa o almacenada únicamente en el propio equipo puede
perderse y no permite revisar fácilmente la evolución del sistema.

## Opciones consideradas

1. Mantener la documentación únicamente en Madre.
2. Usar archivos personales sin control de versiones.
3. Mantener la documentación en `code-temple`.

## Decisión

La documentación versionada de Madre se mantiene en:

```text
docs/infra/madre/
```

dentro del repositorio `code-temple`.

## Consecuencias

- Cada cambio documental queda registrado en Git.
- La documentación puede revisarse y recuperarse.
- El estado real de Madre debe sincronizarse periódicamente con el repositorio.
- No se almacenan secretos, tokens, claves privadas ni archivos `.env`.

## Revisión y reversión

La decisión se puede revertir trasladando la documentación a otro repositorio
versionado, manteniendo el historial y actualizando todos los enlaces.
