# Scripts de code-temple

Scripts de utilidad a nivel de repo completo, distintos de los scripts
propios de cada módulo (ej. docs/infra/madre/auditoria/ tiene los suyos).

## generar-contexto.py

### Qué hace
Lee AGENTS.md, CONTEXT.md y los documentos clave de docs/ecosistema/ y
docs/estandares/, y los concatena en un único bloque de texto con
separadores claros por archivo. No modifica nada, es de solo lectura.

### Por qué existe
Para no tener que abrir y copiar manualmente 6 archivos distintos cada
vez que empiezas una sesión con un agente de IA (yo, Claude Code,
Cursor, o en el futuro Mimir/Ollama). Un solo comando te da todo el
contexto necesario en un bloque listo para pegar.

### Cuándo ejecutarlo
- Al empezar una sesión nueva con cualquier agente de IA que no tenga
  ya el contexto del repo
- Antes de indexar el repo en Mimir (Fase 6 del plan del bot), como
  fuente base del volcado inicial
- Cuando añadas o cambies algo en docs/ecosistema/ y quieras verificar
  que el volcado sigue reflejando lo correcto

### Uso

```bash
python scripts/generar-contexto.py
```

Para guardarlo en un archivo en vez de verlo por pantalla:

```bash
python scripts/generar-contexto.py > /tmp/contexto-code-temple.txt
```

### Variables de entorno
Ninguna. El script usa rutas relativas a su propia ubicación
(RAIZ = carpeta padre de scripts/), así que funciona sin importar
desde dónde lo llames.

### Salida esperada
Un bloque de texto con la forma:

=== AGENTS.md ===
<contenido completo>

=== CONTEXT.md ===
<contenido completo>

...

text

Si falta algún archivo de la lista, imprime `[AVISO: falta <ruta>]` en
vez de fallar, para que el resto del volcado se genere igual.

### Mantenimiento
Si se añade un documento nuevo relevante a docs/ecosistema/ o
docs/estandares/, hay que añadirlo a la lista ARCHIVOS dentro del
propio script. No se detecta automáticamente — es intencional, para
no volcar contenido irrelevante sin revisión.
