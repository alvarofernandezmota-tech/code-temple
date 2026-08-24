# ADR-004: Convención scripts + procedimientos por repo

## Estado
Aceptado

## Fecha
2026-08-24

## Contexto

Durante la sesión 2026-08-23 se creó `scripts/organizar_diario.py` en midgaror
para automatizar la organización del diario. Surgió la pregunta de dónde deben
vivir los scripts de automatización respecto a su documentación.

Dos opciones evaluadas:
1. Centralizar todos los scripts en code-temple (repo "madre")
2. Mantener scripts + procedimientos juntos, dentro de cada repo

## Decisión

Se opta por la **opción 2**: cada repo mantiene sus propios `scripts/` junto a
sus propios `docs/procedimientos/`, con la convención de nombres:

docs/procedimientos/[nombre].md ↔ scripts/[nombre].py

text

code-temple pasa a documentar el ECOSISTEMA completo (qué repos existen, para
qué sirven, dónde están), pero NO el detalle interno de cada repo. Cada repo
es autónomo y autocontenido.

Se crea `docs/procedimientos/plantilla-repo.md` en code-temple como plantilla
de referencia para crear repos nuevos con esta estructura.

## Consecuencias

**Positivas:**
- Cada repo es autocontenido: se puede clonar y entender sin depender de code-temple
- La IA (o cualquier persona) que abre un repo ve inmediatamente su procedimiento y su script juntos
- Evita acoplar todos los repos a un único punto central de scripts

**Negativas:**
- Puede haber scripts similares duplicados entre repos (ej. un futuro script de backup en varios repos)
- Requiere disciplina para mantener la convención de nombres

## Referencias
- Sesión 2026-08-23: creación de `escribir_entrada` y `organizar_diario.py` en midgaror
- `docs/procedimientos/plantilla-repo.md`
