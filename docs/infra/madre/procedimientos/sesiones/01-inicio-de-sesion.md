# Procedimiento: Inicio de Sesión de Trabajo

**Versión:** 1.0  
**Fecha:** 2026-08-13  
**Responsable:** @alvarofernandezmota-tech

## Objetivo

Documentar el procedimiento estándar para iniciar una sesión de trabajo de forma impecable.

## Checklist de Inicio

### 1. Documentar Sesión (PRIMERO) ⭐

- [ ] Crear archivo de sesión con fecha
- [ ] Registrar hora de inicio
- [ ] Registrar participantes
- [ ] Registrar objetivos

**Comando:**
```bash
mkdir -p docs/sesiones/$(date +%Y-%m-%d)-sesion
cat > docs/sesiones/$(date +%Y-%m-%d)-sesion/inicio.md << 'EOFMD'
# Sesión de Trabajo

**Fecha:** $(date +%Y-%m-%d)  
**Hora Inicio:** $(date +%H:%M)  
**Participantes:** Humano + Agente IA  
**Estado:** 🟡 En curso

## Objetivos

1. [ ] 
2. [ ] 
3. [ ]

## Notas

- 
EOFMD
```

### 2. Verificar Estado del Repo

- [ ] `git status` - limpio
- [ ] `git fetch origin` - actualizado
- [ ] `git status` - alineado con origin

**Comandos:**
```bash
git status
git fetch origin
git status
```

### 3. Revisar Issues

- [ ] Listar issues disponibles
- [ ] Identificar issues pendientes
- [ ] Seleccionar issue(s) a trabajar

**Comandos:**
```bash
ls -la docs/infra/madre/issues/
cat docs/infra/madre/issues/README.md
```

### 4. Revisar Documentación Existente

- [ ] Ver README del área
- [ ] Ver procedimientos existentes
- [ ] Ver últimos commits

**Comandos:**
```bash
cat docs/infra/madre/README.md
ls -la docs/infra/madre/procedimientos/
git log --oneline -10
```

### 5. Preparar Trabajo

- [ ] Definir alcance
- [ ] Identificar dependencias
- [ ] Preparar comandos/scripts

### 6. Commit de Inicio

- [ ] Agregar archivo de inicio de sesión
- [ ] Commit con mensaje claro
- [ ] Push a GitHub

**Comandos:**
```bash
git add docs/sesiones/$(date +%Y-%m-%d)-sesion/
git commit -m "docs(sesion): Iniciar sesión $(date +%Y-%m-%d)"
git push
```

## Referencias

- [Issue #17 - Procedimientos](https://github.com/alvarofernandezmota-tech/code-temple/issues/17)
- [Issue #28 - Procedimientos](https://github.com/alvarofernandezmota-tech/code-temple/issues/28)
