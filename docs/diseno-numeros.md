# Los números del juego, medidos

Ningún valor de este documento es una opinión: todos salen de
`scripts/medir_balance.py`, que ejecuta el juego sin ventana y cuenta. Para
repetir la medición tras cualquier cambio:

    SDL_VIDEODRIVER=dummy python3 scripts/medir_balance.py

Todos los valores viven en `tank_scrap/constants.py`. Si cambias uno, vuelve a
medir y actualiza la tabla; un número sin medición al lado es una opinión
disfrazada.

---

## 1. Los tres desequilibrios que encontró la medición

Estaban en el juego y no se veían jugando dos minutos, porque son de
aritmética, no de tacto.

### 1.1 La chatarra no escaseaba: sobraba

| Medición | Valor |
| --- | --- |
| Chatarra disponible, fase de campaña | 168-200 |
| Chatarra disponible, sala de arena | 48-108 (media 73) |
| Coste del anillo completo del águila | 8 (antes) |
| Chatarra en mano de un bot que no gasta nada, sala 2 | 46-79 |

Con ladrillo a 1 y acero a 6, el presupuesto era infinito: reponer el águila
costaba 8 de 172 disponibles. No había economía, había calderilla.

**Arreglo:** costes al doble (**ladrillo 2, acero 10, reroll 5**) y **techo de
20 de chatarra encima**. Lo que pasa del techo se pierde, y el marcador lo
avisa en rojo. Medido después: el mismo bot pierde **9-15 de chatarra** por no
gastar. Acumular ya cuesta.

Efecto secundario que salió de ahí: recuperar tu propio muro estando en el
techo lo borraba y no devolvía nada. Ahora **se niega a derribarlo** — perder
lo que recuperas es destruir valor en silencio.

### 1.2 El jefe moría en 1,7 segundos

Su vida crecía **+2 por ciclo** (lineal) mientras el daño del jugador crece
**multiplicando** cañones por cadencia.

| | antes | ahora |
| --- | --- | --- |
| Vida, sala 5 | 10 | 18 |
| Vida, sala 25 | 18 | 60 |
| Tiempo de caer con 2 cañones y cadencia x2, sala 5 | **1,7 s** | 3,5 s |
| Tiempo de caer a tope de mejoras, sala 5 | **0,5 s** | 1,7 s |

**Arreglo:** vida = `18 × 1,35^ciclo`, que es el orden de lo que gana el
jugador entre jefe y jefe.

### 1.3 El daño crecía sin techo

Cuatro cañones por cuatro escalones de cadencia daban **19,65 impactos/s**: la
oleada de la sala 20 entera eran 36 impactos, menos de dos segundos.

**Arreglo doble:** cada cañón extra alarga la recarga un **15 %**, y la
cadencia baja de 4 escalones a **3**. Tope nuevo: **10,57 impactos/s**.

| Cañones | cadencia x0 | x1 | x2 | x3 |
| --- | --- | --- | --- | --- |
| 1 | 1,82 | 2,33 | 2,99 | 3,83 |
| 2 | 3,16 | 4,05 | 5,20 | 6,66 |
| 3 | 4,20 | 5,38 | 6,90 | 8,84 |
| 4 | 5,02 | 6,43 | 8,24 | **10,57** |

Y para que el contenido no se consuma más rápido de lo que crece, la escolta
gana **+1 de vida a partir de la sala 11** y otro **+1 en la 21**. La sala 25
pasa de 36 a 102 de vida total: 9,7 s de fuego puro incluso a tope.

---

## 2. Tabla de constantes

Rango sano = donde el juego sigue funcionando. Fuera de él se rompe algo
concreto, y la columna dice qué.

### Jugador

| Constante | Valor | Rango sano | Qué se rompe fuera |
| --- | --- | --- | --- |
| `PLAYER_SPEED` | 0.85 | 0.6 - 1.1 | por debajo no escapas de una bala; por encima el ajuste al medio subtile se nota como resbalón |
| `PLAYER_BULLET_SPEED` | 2.6 | 2.0 - 3.5 | por debajo los enemigos esquivan sin querer; por encima la bala atraviesa un subtile por fotograma y se cuela por las esquinas |
| `PLAYER_FIRE_INTERVAL` | 0.55 | 0.4 - 0.8 | es el eje de toda la curva de daño: tocarlo mueve las 12 casillas de la tabla de arriba |
| `MULTI_BARREL_PENALTY` | 0.15 | 0.10 - 0.25 | a 0 el daño vuelve a ser lineal en cañones (19,7 de tope); por encima de 0.25 el segundo cañón es un castigo |
| `PLAYER_MAX_BULLETS` | 1 | 1 - 2 | base de campaña; en arena lo suben las mejoras hasta 4 |
| `PLAYER_LIVES` | 3 | 2 - 5 | solo campaña |
| `ARENA_PLAYER_HP` | 4 | 3 - 6 | a 3 la sala 15 es una lotería; a 6 no hay tensión antes de la 20 |
| `PLAYER_SPAWN_SHIELD` | 2.5 s | 1.5 - 3.5 | por debajo mueres en la reaparición; por encima se usa para colarse |
| `ARENA_MOVING_FIRE_PENALTY` | 1.6 | 1.0 - 2.0 | a 1.0 el disparo automático deja de tener sentido; a 2.0 obliga a pararse siempre |

### Chatarra

| Constante | Valor | Rango sano | Qué se rompe fuera |
| --- | --- | --- | --- |
| `SCRAP_PER_BRICK` | 1 | 1 | subirlo multiplica un presupuesto ya holgado |
| `COST_BRICK` | 2 | 2 - 3 | a 1 vuelve la calderilla; a 4 no se construye nunca |
| `COST_STEEL` | 10 | 8 - 14 | a 6 el acero es la opción obvia siempre; por encima de 14 es decorado |
| `SCRAP_CAP` | 20 | 15 - 30 | por debajo de 15 no da para un búnker; por encima de 30 vuelve el acaparamiento |
| `REROLL_COST` | 5 | 3 - 8 | a 3 se tira hasta que salga lo que quieres; a 8 nadie lo usa |
| `SCRAP_LIFETIME` | 14 s | 8 - 20 | por debajo no llegas a la chatarra del otro extremo; por encima no hay que ir a por ella |
| `SCRAP_START` | 4 | 0 - 6 | dos ladrillos de arranque |

### Enemigos

| Constante | Valor | Rango sano | Qué se rompe fuera |
| --- | --- | --- | --- |
| `ENEMY_FIRE_MIN/MAX` | 0.6 / 2.1 s | 0.5-0.8 / 1.5-3.0 | con el mínimo por debajo de 0.5 y cinco enemigos en pantalla no hay hueco por donde pasar |
| `ENEMY_TURN_CHANCE` | 0.02 | 0.01 - 0.05 | por encima tiemblan en el sitio; por debajo van en línea recta como trenes |
| `ENEMY_HUNT_CHANCE` | 0.65 | 0.4 - 0.8 | a 0.8 te acosan sin descanso; a 0.4 pasean |
| `ENEMY_SPAWN_DELAY` | 1.6 s | 1.0 - 2.5 | en arena se multiplica por 0.6 |
| `ENEMIES_ON_FIELD` | 4 | 3 - 6 | en arena sube a 5-7 según avanza |
| `BOSS_HP_BASE` | 18 | 15 - 25 | a 10 muere en 1,7 s (era el bug) |
| `BOSS_HP_GROWTH` | 1.35 | 1.25 - 1.45 | a 1.0 el jefe 5 es de adorno; a 1.5 el de la sala 25 son 25 s de aguantar |
| `BOSS_SCRAP_DROP` | 12 | 8 - 16 | con techo 20, más de 16 se desperdicia entero |

---

## 3. Lo que la medición no puede decidir

Esto es lo que hay que jugar. Ningún script lo sabe:

1. **Si 10,57 impactos/s a tope se siente potente o absurdo.** La aritmética
   dice que ya no rompe el contenido; el tacto no lo dice un número.
2. **Si pararse a disparar es tenso o incómodo.** La penalización de ×1.6 al
   disparar en marcha es la palanca, y el rango sano es ancho (1.0 a 2.0).
3. **Si el techo de 20 obliga a decidir o solo molesta.** El bot pierde 9-15
   por no gastar, que era el objetivo; si jugando se siente como un castigo
   arbitrario, la respuesta no es subir el techo sino abaratar el acero.
4. **Si las salas duran demasiado a partir de la 15.** 10,8 s de fuego puro
   más el movimiento pueden ser dos minutos reales de sala.
5. **Si el jefe aguanta bien 3,5 s o se hace esponja.** Si se hace esponja, la
   solución no es bajarle la vida: es darle fases, para que esos segundos
   cambien de ritmo.

La regla: **medir lo que es aritmética, jugar lo que es tacto.** Mezclar las
dos es lo que produce números puestos a ojo que nadie se atreve a tocar.
