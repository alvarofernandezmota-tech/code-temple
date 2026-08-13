# Procedimiento: Code Review con Agente IA

**Versión:** 1.0  
**Fecha:** 2026-08-13  
**Responsable:** @alvarofernandezmota-tech

## Objetivo

Automatizar la revisión de código usando agentes de IA en GitHub.

## Agentes Disponibles

### 1. GitHub Copilot Code Review (Recomendado)
- **Tipo:** Nativo de GitHub
- **Configuración:** Settings → Rules → Rulesets
- **Costo:** Incluido en Copilot

### 2. CodeRabbit
- **Tipo:** GitHub App
- **URL:** https://github.com/marketplace/code-review-ai
- **Costo:** $24/dev/mes

### 3. Greptile
- **Tipo:** GitHub App
- **URL:** https://greptile.com
- **Costo:** $30/dev/mes

## Configuración de Copilot Code Review

### Pasos:

1. Ir a Settings del repositorio
2. Code and automation → Rules → Rulesets
3. Click en "New ruleset"
4. Click en "New branch ruleset"
5. Nombre: "Copilot Review"
6. Enforcement Status: Active
7. Target branches: Include default branch (main)
8. Branch rules: "Automatically request Copilot code review"
9. Opcional: "Review new pushes"
10. Save

## Uso en Sesiones

### Al hacer PR:
1. Crear PR
2. Copilot revisa automáticamente
3. Revisar comentarios de Copilot
4. Corregir issues
5. Merge

### Revisión Manual:
1. Asignar Copilot como reviewer
2. Esperar revisión
3. Revisar comentarios
4. Corregir
5. Merge

## Referencias

- [GitHub Copilot Code Review](https://docs.github.com/en/copilot/configuring-copilot/configure-automatic-review)
- [CodeRabbit](https://github.com/marketplace/code-review-ai)
- [Greptile](https://greptile.com)
