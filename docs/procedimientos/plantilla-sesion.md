# Plantilla de Sesiones de Trabajo

## Uso

Cada sesión de trabajo debe seguir esta estructura. Crear un nuevo archivo en:

docs/sesiones/YYYY/MM-mes/YYYY-MM-DD.md

text

## Estructura de la sesión

```markdown
## Sesión YYYY-MM-DD

### Plan original
1. [Tarea 1]
2. [Tarea 2]
3. [Tarea 3]

### Ejecución real vs Plan original

#### Plan original (inicio de sesión HH:MM)
1. ✅ [Tarea completada]
2. ✅ [Tarea completada]
3. ⏳ [Tarea aplazada]

#### Lo que realmente pasó (ejecución en paralelo)

**Fase 1: [Nombre de la fase] (HH:MM-HH:MM)**
- HH:MM - [repo]: [acción]
- HH:MM - [repo]: [acción]
- ✅ **COMPLETADO** - [resultado]

**Fase 2: [Nombre de la fase] (HH:MM-HH:MM)**
...

### Errores y correcciones durante la sesión

1. **[Error 1]** - [descripción y corrección]
2. **[Error 2]** - [descripción y corrección]

### Lo que NO se hizo (queda para próximas sesiones)

1. ⏳ **[Tarea pendiente 1]** - [razón]
2. ⏳ **[Tarea pendiente 2]** - [razón]

### Trabajo no planificado (se hizo de más)

El plan original era solo "[plan original]", pero se hizo mucho más:

#### No estaba en el plan original ✅
1. **[Tarea no planificada 1]** - [descripción]
2. **[Tarea no planificada 2]** - [descripción]

#### ¿Dónde está documentado cada avance?

```
docs/
├── procedimientos/
│   ├── inicio-sesion.md ← CREADO hoy (no planificado)
│   └── cierre-sesion.md ← ACTUALIZADO hoy (no planificado)
├── ecosistema/
│   ├── infra-madre.md ← CREADO hoy (no planificado)
│   ├── repos-activos.md ← ACTUALIZADO hoy (no planificado)
│   └── fuente-de-verdad.md ← Ya existía
├── adr/
│   └── 001-bifrost-desde-cero.md ← Ya existía
└── sesiones/
    └── YYYY/
        └── MM-mes/
            └── YYYY-MM-DD.md ← ESTA SESIÓN

Balance: Plan vs Realidad
Concepto	Plan original	Realidad
Commits	~X commits	Y commits
Archivos creados	X	Y
Documentación	Mínima	Completa
Tiempo estimado	~X min	~Y horas (HH:MM-HH:MM)
Repos tocadas	X (repo1, repo2)	Y (repo1, repo2, repo3)

Conclusión: [resumen del balance]
Lecciones aprendidas

    [Lección 1] - [descripción]

    [Lección 2] - [descripción]

    [Lección 3] - [descripción]

text

## Procedimiento de sesión

### 1. Inicio de cada sesión nueva

```bash
# Verificar sesión anterior
cd ~/GitHub/personal/code-temple
git log --oneline -10  # Ver últimos commits
git status  # Verificar que todo está limpio

# Si hay algo pendiente → corregir primero
# Si todo limpio → iniciar sesión nueva
```

### 2. Documentar al inicio

- Abrir `docs/sesiones/YYYY/MM-mes/YYYY-MM-DD.md`
- Copiar esta plantilla
- Anotar plan original
- Empezar a trabajar

### 3. Durante la sesión

- Documentar errores y correcciones
- Registrar tiempo real
- Ir haciendo commits

### 4. Cierre de sesión

- Añadir: ejecución real vs plan
- Añadir: errores y correcciones
- Añadir: trabajo no planificado
- Añadir: balance plan vs realidad
- Añadir: lecciones aprendidas
- Commit y push

## Checklist de cierre

- [ ] Todos los commits están en GitHub
- [ ] `git status` está limpio
- [ ] Diario personal actualizado (midgaror)
- [ ] Sesión documentada en code-temple
- [ ] Próxima sesión planificada

## Notas

- No usar comandos automáticos de contexto/auditoría
- Documentación manual captura mejor la realidad
- Cada sesión es única, adaptar la plantilla según sea necesario
