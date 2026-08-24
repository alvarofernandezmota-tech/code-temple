# Plantilla de README para carpetas de docs/

Cada README de carpeta en docs/ debe seguir esta estructura:

## Estructura obligatoria

1. **Título** — `# [Nombre de la carpeta]`
2. **Descripción** — 1-2 frases explicando qué tipo de docs hay aquí (referencia, how-to, explicación, etc.)
3. **Reglas/Convenciones** — si la carpeta tiene reglas específicas (ej: numeración secuencial en adr/, un archivo por día en sesiones/)
4. **Diagrama vertical** — árbol en texto mostrando TODOS los archivos y subcarpetas reales
5. **Índice** — lista con enlaces a cada archivo + 1 línea de descripción de qué contiene
6. **Conexiones** — sección "Relacionado con" que enlace a otras carpetas o archivos relevantes

## Ejemplo (docs/adr/)

ADR — Architecture Decision Records

Decisiones de arquitectura del ecosistema, formato Michael Nygard.

Regla: numeración secuencial estricta...
Estructura

docs/adr/
├── README.md
├── 001-bifrost-desde-cero.md
├── 002-regla-enganche-cuadruple.md
├── 003-orden-rollout-formatter.md
└── 004-convencion-scripts-procedimientos.md
Índice

    001-bifrost-desde-cero.md — decisión de crear bifrost desde cero

    002-regla-enganche-cuadruple.md — regla para carpetas nuevas en docs/
    ...

Relacionado con

    docs/procedimientos/plantilla-repo.md — estructura mínima de repos

    docs/ecosistema/plan-bot.md — plan que implementa ADR-001

text

## Cuándo actualizar

- Al añadir/quitar un archivo de la carpeta
- Al cambiar una regla de convención
- En cada auditoría trimestral (ver docs/procedimientos/mantenimiento-documentacion.md)
