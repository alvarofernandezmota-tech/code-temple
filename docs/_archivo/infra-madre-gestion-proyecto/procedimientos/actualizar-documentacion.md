# Actualizar la documentación de Madre

## Objetivo

Mantener sincronizada la documentación de Madre con el estado real del
ordenador, sus servicios, sus repositorios y su infraestructura Docker.

## Regla principal

Cada cambio real se documenta en el archivo que representa su área. No se
duplica información completa en varios archivos.

## Qué archivo actualizar

| Cambio realizado | Archivo principal |
|---|---|
| Estado general o fase de reconstrucción | `estado.md` y `README.md` |
| Hardware, discos o firmware | `hardware.md` |
| Kernel, particiones o montajes | `sistema.md` |
| Paquetes y herramientas instaladas | `software.md` y `paquetes-explicitos.txt` |
| Servicios systemd | `servicios.md` |
| Docker, Compose, redes o volúmenes | `docker.md` |
| Repositorios locales y rutas | `repos.md` |
| Carpetas y organización local | `estructura.md` |
| Red, Wi-Fi, NetworkManager o UFW | `red.md` |
| Copias de seguridad | `backups.md` |
| Decisión técnica o arquitectónica | `adr/` |
| Procedimiento operativo repetible | `procedimientos/` |
| Cualquier cambio relevante | `cambios.md` |

## Flujo obligatorio

1. Leer `../normas.md`.
2. Ejecutar el procedimiento específico del área modificada.
3. Comparar el resultado con la documentación existente.
4. Actualizar únicamente los archivos afectados.
5. Añadir una entrada en `../cambios.md`.
6. Revisar enlaces, rutas y referencias cruzadas.
7. Comprobar que no se han añadido secretos.
8. Revisar el diff con `git diff`.
9. Crear un commit descriptivo.
10. Subir los cambios a `main`.

## Comandos de revisión

```bash
cd ~/GitHub/trabajo/code-temple

git status
git diff --check
git diff -- docs/infra/madre
git grep -nE 'password|token|secret|PRIVATE KEY|\.env' -- docs/infra/madre
```

La última comprobación debe revisarse manualmente para evitar publicar
credenciales o material privado.

## Convención de commit

Usar mensajes claros con el prefijo `docs(madre)`:

```text
docs(madre): actualizar inventario de software
docs(madre): documentar cambio de red
docs(madre): actualizar estado de Docker
docs(madre): registrar decisión arquitectónica
```

## Actualización final

```bash
git add docs/infra/madre
git diff --cached --check
git commit -m "docs(madre): describir el cambio realizado"
git push origin main
```

## Relación con issues y ADRs

Los issues de `code-temple` registran tareas pendientes y su seguimiento.
Un ADR registra una decisión importante, sus alternativas y sus consecuencias.
Una sesión registra cronológicamente lo que se hizo. Ninguno de estos documentos
sustituye al archivo técnico que describe el estado actual de Madre.
