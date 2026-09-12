# TANK SCRAP 1990 — hoja de ruta y decisiones abiertas

Estado a 2026-09-12. Seis commits en `claude/tank-game-pixel-twist-zuqnhj`
([PR #62](https://github.com/alvarofernandezmota-tech/code-temple/pull/62)),
2.749 líneas, 28 tests en verde.

Este documento existe porque las decisiones estaban repartidas por la
conversación. Cada una lleva **recomendación**, para que decidir sea decir sí
o no en vez de empezar de cero.

---

## 1. Qué ya está hecho

| Bloque | Estado |
| --- | --- |
| Campo de subtiles de 8 px, colisiones, agua/hielo/árboles | hecho |
| Chatarra: recoger, construir ladrillo/acero, recuperar, oxidarse | hecho |
| 4 tipos de enemigo con silueta propia + IA con sesgo al objetivo | hecho |
| Modo CAMPAÑA: 3 fases, águila, vidas, cortinilla, recuento | hecho |
| Modo ARENA: salas generadas, 1 de 3 mejoras, vida, rerolls | hecho |
| Jefe de 32x32 cada 5 salas, con barra de vida | hecho |
| Pixel art, tipografía 3x5 y sonido, todo generado en código | hecho |
| Récord persistido, autotests sin ventana, CI escrita | hecho |

---

## 2. Decisiones abiertas

Ordenadas por cuánto bloquean lo demás. Las tres primeras cambian
arquitectura o identidad del proyecto; el resto son de contenido.

### 2.1 Proyecto

**D1. ¿Se mergea la PR a `main`?**
La rama lleva seis commits y el repo estaba archivado. Mientras no se mergee,
`main` sigue siendo la documentación vieja.
→ *Recomendación: sí, mergear.* Nada depende ya del contenido archivado, que
sigue en el historial y en `midgaror`.

**D2. ¿El repo se queda llamándose `code-temple`?**
El nombre no dice nada del juego y arrastra el pasado de repo de documentación.
→ *Recomendación: renombrar a `tank-scrap`* (GitHub redirige el antiguo, no
rompe nada). Alternativa: repo nuevo y dejar `code-temple` archivado de verdad.

**D3. ¿Licencia?**
No hay `LICENSE`. Sin licencia, nadie —tú incluido en el futuro— tiene permiso
claro para reutilizar el código, y en itch.io o GitHub Pages eso importa.
→ *Recomendación: MIT*, por ser lo más simple. Si prefieres que nadie lo
reutilice comercialmente, otra opción es dejarlo privado y sin licencia, a
sabiendas.

**D4. CI bloqueada** *(no es una decisión, es una acción tuya)*
Los jobs no reciben runner: Actions sin minutos o deshabilitado en tu cuenta.
Hay que revisarlo en la facturación del owner. El workflow ya está y pasará en
verde solo.

### 2.2 Diseño — lo que cambia cómo se juega

**D5. ¿Meta-progresión entre runs de Arena?**
Hoy la chatarra sobrante se funde en puntos y la run empieza siempre desnuda.
La alternativa roguelite es que parte de la chatarra sobreviva y compre mejoras
permanentes (más vida inicial, empezar con 10 de chatarra...).
→ *Recomendación: no, todavía.* Primero hay que ver si la run base engancha;
la meta-progresión tapa un bucle flojo en vez de arreglarlo. Y obliga a
guardar estado de verdad, no solo un récord.

**D6. ¿Salas especiales en Arena?**
Ahora todas las salas son "mata a todos". Candidatas:
- **Defensa**: aguanta 60 s protegiendo un águila — es donde construir muro
  brilla de verdad.
- **Tienda**: gastas chatarra en mejoras a la carta en vez de 1 de 3.
- **Forja**: cambias vida máxima por potencia.
→ *Recomendación: la de defensa primero.* Es la única que usa la mecánica
propia del juego en vez de importar una convención de otro.

**D7. ¿Mejoras con coste (maldiciones)?**
Tipo "+50% de daño, -1 de vida máxima". Da decisiones con filo en vez de
mejoras que siempre son un sí.
→ *Recomendación: sí, 3 o 4, marcadas en rojo en la oferta.*

**D8. ¿Torretas plantables con chatarra?**
Lo mencionamos y se quedó fuera. Cuarto destino para la chatarra.
→ *Recomendación: después de D6 y D7.* Añadir otro sumidero antes de que los
tres actuales estén balanceados solo hace ruido.

**D9. ¿Más jefes?**
Solo hay uno y aparece cada 5 salas: a la tercera vez ya no sorprende.
→ *Recomendación: dos más, con patrón distinto* (uno que siembra minas, otro
que embiste y rompe el escenario).

### 2.3 Contenido y alcance

**D10. ¿Cuántas fases tiene la campaña?**
Hay 3 y se reciclan. El Battle City original tenía 35.
→ *Recomendación: 8 a mano.* Suficiente para una progresión con carácter, y
escritas a mano tienen intención; generadas serían como las de Arena.

**D11. ¿Dos jugadores en local?**
El original lo tenía y es media identidad del juego en el sofá.
→ *Recomendación: sí, en campaña.* La chatarra compartida es un buen
generador de discusiones, que es exactamente lo que se busca.

**D12. ¿Música, además de efectos?**
El sintetizador ya está; una melodía chiptune de bucle es más trabajo que 13
bleeps, pero el mismo camino.
→ *Recomendación: al final.* Es lo primero que cansa si está mal.

**D13. ¿Mando / gamepad?**
→ *Recomendación: sí, es media hora* con `pygame.joystick` y se juega mucho
mejor que con teclado.

**D14. ¿Empaquetado y publicación?**
Hoy se juega clonando el repo. Opciones: ejecutable con PyInstaller, o
compilar a web con pygbag y subirlo a itch.io / GitHub Pages.
→ *Recomendación: pygbag a itch.io*, porque un enlace que abre el juego en el
navegador se prueba; un `.zip` de 40 MB, no.

**D15. ¿Idioma?**
Todo está en español (código, HUD, docs).
→ *Recomendación: dejarlo así.* Si algún día se publica fuera, se traduce el
HUD, que son 30 cadenas.

---

## 3. Lo que falta que no es decisión

- **Balance real.** Los números (coste de muro, vida, cadencias,
  penalización al disparar en marcha) están puestos a ojo y probados con un
  bot tonto, no jugados. Hace falta que juegues y digas qué se siente lento o
  injusto; eso no lo puedo medir yo.
- **Sin pausa en la oferta de mejoras.** Al elegir mejora el mundo se detiene
  por completo; conviene comprobar que no rompe el ritmo.
- **Sin `CLAUDE.md`/`AGENTS.md` para el modo Arena** más allá de las reglas
  actuales; si crece, conviene separar reglas de contenido.

---

## 4. El cómo

Los pasos concretos de cada punto —qué archivos toca, tamaño, dependencias y
cómo se comprueba— están en [plan.md](plan.md).

## 5. Orden propuesto

1. **D1, D2, D3** — mergear, renombrar, licencia. Media hora y dejan de
   arrastrarse.
2. **Juegas una partida de cada modo** y dices qué se siente mal. Todo lo de
   abajo mejora con esa información; sin ella, es adivinar.
3. **D6 (sala de defensa) + D7 (maldiciones)** — el bucle de Arena gana filo.
4. **D13 (mando) + D10 (más fases)** — contenido y comodidad.
5. **D11 (dos jugadores)**.
6. **D14 (publicar en itch.io)** cuando haya algo que valga la pena enseñar.
7. **D9 (más jefes), D8 (torretas), D12 (música), D5 (meta-progresión)** —
   cuando el resto esté asentado.

La idea de fondo: primero cerrar lo que bloquea, después jugar, y solo
entonces añadir. Cada cosa nueva que se mete antes de jugar es una apuesta a
ciegas.
