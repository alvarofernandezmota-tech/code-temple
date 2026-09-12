# Plan: cómo se resuelve cada punto

Acompaña a [hoja-de-ruta.md](hoja-de-ruta.md), que dice *qué* hay que decidir.
Esto dice *cómo* se hace cada cosa: pasos, qué archivos toca, tamaño, de qué
depende y cómo sabremos que funciona.

Tamaños: **S** = un rato y un commit · **M** = varias piezas, tests nuevos ·
**L** = toca arquitectura o hace falta contenido.

---

## Paso 0 — MVP jugable *(hecho)*

El juego ya se juega en un comando, sin instalar nada a mano:

```bash
./jugar.sh          # Linux y macOS
jugar.bat           # Windows (doble clic)
```

Prepara un `.venv` propio la primera vez, instala pygame y arranca. No toca el
Python del sistema. Probado desde cero en un entorno limpio.

**Lo que falta para que sea jugable sin Python** (versión web) tiene un
bloqueo que no es de código: pygbag descarga su runtime de
`pygame-web.github.io`, y la política de red de este entorno lo rechaza con
403. En tu máquina no hay ese bloqueo, así que la versión web se puede
construir ahí — está en el punto D14, abajo.

---

## Bloque 1 — Cerrar lo que arrastra

### D1 · Mergear la PR · **S**
1. Repasar el diff completo una vez más (216 archivos, casi todo borrado de la
   documentación archivada).
2. Quitar el estado de borrador y mergear con *merge commit*, para que los
   siete commits queden legibles en el historial.
3. Borrar la rama después.

*Depende de:* nada. *Se comprueba:* `main` arranca el juego con `./jugar.sh`.

### D2 · Renombrar el repo · **S**
1. Renombrar `code-temple` → `tank-scrap` en los ajustes de GitHub (redirige
   el antiguo, no rompe clones existentes).
2. Actualizar las URLs en `README.md` y `docs/`.
3. Actualizar el `git remote` local.

*Depende de:* D1, para no renombrar con una PR abierta. *Se comprueba:* el
enlace viejo redirige y `git push` sigue funcionando.

### D3 · Licencia · **S**
1. `LICENSE` con MIT y tu nombre.
2. Una línea en el README.

*Depende de:* nada. *Se comprueba:* GitHub muestra "MIT" en la portada del repo.

### D4 · CI · **S, pero es tuyo**
Revisar el límite de gasto de Actions en la facturación de tu cuenta, o
activar Actions para el repo. El workflow ya está escrito y pasará solo.
*Se comprueba:* el check `CI / test` se pone verde sin tocar nada.

---

## Bloque 2 — Jugar antes de añadir

### Paso de juego · **tú**
Una partida de campaña y una run de arena, apuntando cinco cosas:
1. ¿El daño a tope se siente potente o absurdo? (10,57 impactos/s)
2. ¿Pararse a disparar es tenso o incómodo?
3. ¿El techo de 20 de chatarra obliga a decidir o solo molesta?
4. ¿Las salas se alargan a partir de la 15?
5. ¿El jefe aguanta bien o se hace esponja?

Están medidas en [diseno-numeros.md](diseno-numeros.md) con su rango sano, así
que cada respuesta tuya se traduce en mover un número concreto, no en rehacer
nada. Sin esto, todo lo de abajo es apostar a ciegas.

---

## Bloque 3 — El bucle de Arena gana filo

### D6 · Sala de defensa · **M**
Es la sala donde construir muro es la respuesta, no un adorno.
1. `arena.py`: tipo de sala `"defensa"` en la generación, cada 3 salas y nunca
   pegada a una de jefe.
2. Reaparece el águila en el centro de la sala y un contador de 60 s en el HUD.
3. La condición de victoria de esa sala es que el águila siga en pie al
   acabar el tiempo; los enemigos entran en oleadas continuas, no en cantidad
   fija.
4. Recompensa: chatarra a tope (llena el techo) además de la mejora.
5. Tests: la sala trae águila, el reloj gana la sala, perder el águila mata la
   run igual que quedarse sin vida.

*Depende de:* el paso de juego (si el techo molesta, la recompensa cambia).

### D7 · Mejoras con coste · **S**
1. `arena.UPGRADES`: campo nuevo `coste` con el texto del castigo.
2. Cuatro candidatas: +50 % daño / −1 vida máxima · +2 cañones / −25 % cadencia
   · bala perforante / la tuya también rompe tu muro · velocidad +40 % / −1
   vida máxima.
3. Marcadas en rojo en la oferta, con el castigo en su propia línea.
4. Test: coger una maldición aplica las dos mitades.

*Depende de:* nada.

### D9 · Dos jefes más · **M**
1. `BossTank` pasa a tener un `patron`: el actual (dos cañones), uno que
   siembra minas al moverse, y uno que embiste en línea recta rompiendo
   ladrillo.
2. Las minas son una entidad nueva en `entities.py` (aviso de 1 s y explosión).
3. El jefe que embiste necesita una fase de carga telegrafiada, o es injusto.
4. Sprites: los tres comparten chasis de 32x32 y cambian torreta y color.
5. Tests: cada patrón aparece, las minas dañan al jugador y no al jefe.

*Depende de:* saber si el jefe actual se hace esponja (paso de juego).

---

## Bloque 4 — Comodidad y contenido

### D13 · Mando · **S**
1. `pygame.joystick` en `game.py`: stick y cruceta a dirección, botón sur a
   disparo, botón oeste a modo obra, start a pausa.
2. El teclado sigue funcionando a la vez; se detecta el mando al arrancar y al
   conectarlo.
3. Test: la capa de entrada traduce eventos de mando a las mismas acciones
   (sin mando físico, con eventos sintéticos).

### D10 · Ocho fases de campaña · **M**
1. Cinco mapas nuevos en `levels.py`, 13x13, escritos a mano.
2. Criterio de progresión: la 1-2 enseñan, la 3-4 introducen acero y agua, la
   5-6 aprietan los caminos hacia el águila, la 7-8 mezclan hielo con pasillos
   estrechos.
3. `medir_balance.py` ya cuenta la chatarra disponible por fase: cada mapa
   nuevo pasa por ahí para que no se dispare.
4. Test: sigue valiendo el que comprueba 13x13 y un solo águila.

### D11 · Dos jugadores en local · **L**
1. `PlayerTank` ya está aislado; hace falta una lista de jugadores en `Game` y
   que el HUD muestre dos columnas.
2. Teclas: jugador 1 flechas + espacio, jugador 2 WASD + ctrl derecho.
3. **La decisión de diseño de verdad:** ¿chatarra compartida o cada uno la
   suya? Compartida genera las discusiones que hacen gracia; separada es más
   justa. Recomiendo compartida, con el techo también compartido.
4. La cámara no cambia (pantalla fija), así que no hay trabajo de scroll.
5. Tests: dos jugadores se bloquean entre sí, las balas de uno no matan al
   otro, y perder a uno no acaba la partida.

*Depende de:* D13 sería mejor tenerlo antes (dos jugadores a teclado en el
mismo teclado es incómodo).

---

## Bloque 5 — Que lo pueda jugar cualquiera

### D14 · Web e itch.io · **M, en tu máquina** *(la mitad ya está)*
1. ~~`main.py` con el bucle en `async`~~ **hecho**: mismo `Game`, un
   `await asyncio.sleep(0)` por fotograma. Probado nativo (240 fotogramas,
   salida limpia).
2. ~~Script de construcción y servidor~~ **hecho**: `scripts/servir_web.sh`
   instala pygbag, construye y sirve en la red local (imprime la IP para
   abrirlo desde el móvil).
3. **Pendiente, en tu máquina:** ejecutar ese script una vez. Aquí no se
   puede: la red de este entorno rechaza `pygame-web.github.io` con 403 y es
   de donde pygbag baja su runtime. El paso de construcción es, por tanto, lo
   único de este repo que no he podido probar.
4. Subir `build/web` a itch.io como HTML5 (o a GitHub Pages) cuando el juego
   esté como quieres: cada publicación es una versión que la gente ve.

*Si la construcción falla en tu máquina*, lo típico es la versión de Python
(pygbag pide 3.8-3.12) o que el firewall bloquee la descarga del runtime.

*Depende de:* D1 (mergeado) y de que el juego esté como quieres, porque cada
publicación es una versión que la gente ve.

---

## Bloque 6 — Cuando el resto esté asentado

### D8 · Torretas plantables · **M**
Entidad nueva que dispara sola, cuesta ~12 de chatarra (más de media mochila)
y dura hasta que la rompen. *Antes:* que el techo y los costes estén probados
jugando, o es un cuarto sumidero sin balancear.

### D12 · Música · **M**
El sintetizador de `audio.py` ya vale; hace falta un secuenciador mínimo
(patrones de notas con duración) y dos temas: título y combate. *Antes:* todo
lo demás, porque es lo primero que cansa si está mal.

### D5 · Meta-progresión · **L**
Guardar estado de verdad (no solo el récord): mejoras permanentes compradas
con la chatarra que sobrevive. *Antes:* saber que la run base engancha. Si no
engancha, esto lo tapa en vez de arreglarlo.

### D15 · Idioma · **S**
Queda en español. Si algún día se traduce, el HUD son ~30 cadenas en
`game.py`; se saca a un diccionario y listo.

---

## Resumen en una tabla

| Punto | Qué es | Tamaño | Depende de |
| --- | --- | --- | --- |
| D1 | mergear | S | — |
| D2 | renombrar repo | S | D1 |
| D3 | licencia MIT | S | — |
| D4 | activar Actions | S | tuyo |
| — | **jugar una partida** | tú | D1 |
| D6 | sala de defensa | M | jugar |
| D7 | mejoras con coste | S | — |
| D9 | dos jefes más | M | jugar |
| D13 | mando | S | — |
| D10 | ocho fases | M | — |
| D11 | dos jugadores | L | D13 |
| D14 | web + itch.io | M | D1, tu máquina |
| D8 | torretas | M | jugar |
| D12 | música | M | el resto |
| D5 | meta-progresión | L | que la run engancha |
| D15 | idioma | S | — |
