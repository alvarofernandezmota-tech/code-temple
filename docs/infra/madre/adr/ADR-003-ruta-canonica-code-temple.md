# ADR-003: Ruta canónica de code-temple en Madre — trabajo/, no personal/

- Estado: aceptado
- Fecha: 2026-08-12
- Área: documentación e infraestructura

## Contexto

Al retomar el trabajo en Madre se clonó `code-temple` en `~/GitHub/personal/code-temple`,
sin comprobar antes si ya existía una copia local en otra ruta.

## Problema

Existía ya una copia funcional y sincronizada en `~/GitHub/trabajo/code-temple`,
con historial de commits al día. Mantener dos clones del mismo repositorio en
rutas distintas genera riesgo de trabajar sobre una copia desactualizada o de
perder cambios por confusión de ruta.

## Opciones consideradas

1. Mantener ambas copias (`personal/` y `trabajo/`) sincronizadas manualmente.
2. Eliminar la copia de `trabajo/` y trabajar solo en `personal/`.
3. Eliminar la copia de `personal/` y fijar `trabajo/` como ruta única y oficial.

## Decisión

Se eliminó `~/GitHub/personal/code-temple` (sin cambios sin commitear) y se
fijó `~/GitHub/trabajo/code-temple` como ruta canónica única de trabajo.
Se corrigió `docs/infra/madre/estructura.md` para reflejarlo (commit `5c9eb82`).

## Consecuencias

- Una sola copia local de `code-temple`, sin riesgo de divergencia por ruta.
- `estructura.md` y `repos.md` quedan alineados con la ubicación real.
- Cualquier clon futuro de `code-temple` en Madre debe hacerse en `~/GitHub/trabajo/`.

## Revisión y reversión

Revertir implica clonar de nuevo en `~/GitHub/personal/code-temple`, migrar
esa ruta como oficial en `estructura.md` y `repos.md`, y eliminar la copia de `trabajo/`.
