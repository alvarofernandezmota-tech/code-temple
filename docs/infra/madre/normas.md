# Normas operativas de Madre

## Alcance

Estas normas se aplican exclusivamente al equipo Madre. Las normas generales
del repositorio están en `docs/canon/`.

## Reglas obligatorias

1. Leer la documentación actual antes de modificar el sistema.
2. Comprobar el estado inicial antes de cada cambio.
3. No ejecutar varios cambios importantes a la vez.
4. Hacer copia de seguridad cuando exista riesgo de pérdida de datos.
5. No guardar contraseñas, tokens, claves privadas ni archivos `.env`.
6. Verificar el resultado después de cada cambio.
7. Actualizar el inventario correspondiente.
8. Registrar el cambio en `cambios.md`.
9. Documentar cualquier decisión estructural mediante un ADR.
10. Comprobar que el árbol Git queda limpio después del trabajo.

## Regla de reversión

Todo cambio relevante debe tener una forma conocida de deshacerlo antes de
ejecutarse.

## Fuente de verdad

La documentación versionada de `code-temple` es la fuente de verdad documental
de Madre. Si el sistema real y la documentación difieren, primero se registra
la discrepancia y después se corrige de forma controlada.
