# CONTEXT.md — qué es este repo en 30 segundos

code-temple es la base técnica del ecosistema de Álvaro. Sustituye a
yggdrasil-dew (archivado). Aquí vive:

- Documentación de infraestructura real (servidor Madre, Arch Linux)
- Diario de sesiones de trabajo (no confundir con el diario personal,
  que vive en el repo midgaror)
- El plan y mapa del ecosistema completo de repos (docs/ecosistema/)
- Estándares compartidos entre repos (docs/estandares/)
- Decisiones de arquitectura (docs/adr/001-005)
- Procedimientos y scripts automatizados (docs/procedimientos/, scripts/)

## Si eres un agente/IA leyendo esto por primera vez
1. Lee docs/ecosistema/README.md para el mapa completo
2. Lee AGENTS.md para las reglas de esta base de código
3. No asumas nada de docs/infra/ sin correr antes su script de auditoría
4. Para contexto completo: `python3 scripts/generar-contexto.py`
5. Para estructura automática: `python3 scripts/generar-estructura.py`

## Estado actual (2026-08-24)
- ✅ 5 ADRs completos (001-005)
- ✅ 7 carpetas en docs/ con READMEs alineados
- ✅ 5 scripts automatizados (auditoria-repo, generar-contexto, generar-estructura, cerrar-sesion, nueva_sesion)
- ✅ Procedimientos 1:1 con scripts
- ✅ Lista para migrar plantilla a bifrost/midgaror
