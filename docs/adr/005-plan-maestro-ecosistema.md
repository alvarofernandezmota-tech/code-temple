# ADR 005: Plan maestro del ecosistema

## Estado
Aceptado

## Fecha
2026-08-24

## Contexto
El ecosistema tiene 3 repos principales (code-temple, midgaror, bifrost) pero los planes están dispersos:
- code-temple: docs/ecosistema/plan-bot.md (solo el bot)
- midgaror: no tiene plan explícito (solo diario.py y scripts sueltos)
- bifrost: no tiene repo aún (es un plan en plan-bot.md)

Falta un plan maestro que relacione los 3 y muestre dependencias.

## Decisión
Crear un plan maestro en `docs/adr/005-plan-maestro-ecosistema.md` que:
1. Liste los 3 repos y su propósito
2. Muestre dependencias (qué repo depende de cuál)
3. Defina fases de rollout (qué se hace primero, qué depende de qué)
4. Enlace a los planes específicos de cada repo

## Plan maestro

### Repos del ecosistema

| Repo | Propósito | Estado | Plan específico |
|---|---|---|---|
| code-temple | Plantillas, procedimientos, estándares | ✅ Completo (2026-08-24) | docs/procedimientos/plantilla-repo.md |
| midgaror | Datos personales (diario, hábitos, tareas) | ✅ Scripts base (diario.py, organizar-diario.py) | docs/ecosistema/plan-bot.md (fase 2a) |
| bifrost | Bot de Telegram que conecta ambos | ⏳ Pendiente | docs/ecosistema/plan-bot.md (fases 0-3) |

### Dependencias

code-temple (base)
↓ (proporciona plantillas y procedimientos)
midgaror (datos)
↓ (proporciona funciones validadas)
bifrost (bot)

text

### Fases de rollout

1. **Fase 0 (✅ completada 2026-08-24):** code-temple completo
   - ✅ Procedimientos 1:1 con scripts
   - ✅ READMEs en todas las carpetas de docs/
   - ✅ Índice maestro docs/README.md
   - ✅ Mantenimiento documentado

2. **Fase 1 (⏳ pendiente):** bifrost mínimo (solo midgaror)
   - [ ] Crear repo bifrost
   - [ ] Bot de Telegram que lee comandos básicos
   - [ ] Conectar con diario.py de midgaror (solo lectura)

3. **Fase 2a (⏳ pendiente):** bifrost + midgaror en foreground
   - [ ] Bot responde comandos de diario (añadir entrada, listar hoy)
   - [ ] Scripts de midgaror validados 1-2 semanas

4. **Fase 2b (⏳ pendiente):** systemd + manejo de errores
   - [ ] Bot como servicio systemd
   - [ ] Reintentos, logs, alertas

5. **Fase 2c (⏳ pendiente):** extender a code-temple
   - [ ] Bot puede crear sesiones en code-temple
   - [ ] Bot puede auditar docs/

6. **Fase 3 (⏳ pendiente):** formatter completo
   - [ ] nueva_sesion.py genera frontmatter automáticamente
   - [ ] infra-madre actualizada con nuevos scripts

## Consecuencias
- Cada repo nuevo debe referenciar este plan maestro
- Los planes específicos (ej: plan-bot.md) deben enlazar a este ADR
- El rollout es secuencial: no se salta fases

## Relacionado con
- docs/ecosistema/plan-bot.md — plan específico del bot (fases 0-3)
- docs/ecosistema/vision.md — visión final del ecosistema
- docs/adr/001-bifrost-desde-cero.md — decisión de crear bifrost sin código heredado
- docs/adr/004-convencion-scripts-procedimientos.md — convención 1:1 aplicada en code-temple
