# ADR-001: Reconstrucción de Madre desde Arch Linux

- Estado: aceptado
- Fecha: 2026-08-06
- Área: sistema base

## Contexto

Madre fue reconstruida desde una instalación limpia de Arch Linux para disponer
de una base conocida, documentada y controlable.

## Problema

Era necesario eliminar configuraciones históricas no documentadas y establecer
un punto de partida fiable.

## Opciones consideradas

1. Mantener la instalación anterior.
2. Limpiar manualmente la instalación existente.
3. Reinstalar y documentar el sistema desde cero.

## Decisión

Se eligió reinstalar Madre desde cero y documentar progresivamente su estado
real.

## Consecuencias

- Se dispone de una base limpia.
- Los servicios se incorporarán de forma controlada.
- La documentación inicial debe actualizarse después de cada cambio.
- La estrategia de backups debe completarse antes de almacenar datos críticos.

## Revisión y reversión

La reversión completa consiste en reinstalar el sistema y reconstruirlo usando
la documentación, el inventario y los backups disponibles.
