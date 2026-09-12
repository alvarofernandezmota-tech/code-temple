"""Mando: traduce joystick a las mismas acciones que el teclado.

El juego lee direcciones y botones en un solo sitio, asi que el mando no es un
camino aparte: rellena las mismas teclas que pulsaria una persona. Asi todo lo
que ya funciona con teclado funciona con mando sin tocarse.
"""
import pygame

from .constants import DOWN, LEFT, RIGHT, UP

AXIS_DEADZONE = 0.45          # por debajo de esto, el stick esta "en reposo"

# Mapa de botones del mando a la tecla equivalente. Los numeros son los del
# esquema habitual (XInput / mandos estilo Xbox), que es lo que usa SDL2.
BUTTON_KEYS = {
    0: pygame.K_SPACE,        # A / sur: disparar y confirmar
    2: pygame.K_b,            # X / oeste: modo obra
    1: pygame.K_x,            # B / este: recuperar muro
    3: pygame.K_e,            # Y / norte: acero en modo obra
    7: pygame.K_RETURN,       # start: menus
    6: pygame.K_p,            # select: pausa
    4: pygame.K_r,            # LB: otra oferta de mejoras
}

HAT_KEYS = {
    (0, 1): pygame.K_UP, (0, -1): pygame.K_DOWN,
    (-1, 0): pygame.K_LEFT, (1, 0): pygame.K_RIGHT,
}

DIRECTION_KEYS = {
    UP: pygame.K_UP, DOWN: pygame.K_DOWN,
    LEFT: pygame.K_LEFT, RIGHT: pygame.K_RIGHT,
}


class Pads:
    """Los mandos conectados, como una capa de entrada mas."""

    def __init__(self):
        self.pads = []
        try:
            pygame.joystick.init()
        except pygame.error:
            return
        self.rescan()

    def rescan(self):
        """Vuelve a mirar que mandos hay (al arrancar y al conectar uno)."""
        self.pads = []
        try:
            for i in range(pygame.joystick.get_count()):
                pad = pygame.joystick.Joystick(i)
                pad.init()
                self.pads.append(pad)
        except pygame.error:
            self.pads = []
        return len(self.pads)

    @property
    def connected(self):
        return bool(self.pads)

    def held_keys(self):
        """Teclas que el mando esta "pulsando" ahora mismo (stick y cruceta)."""
        keys = set()
        for pad in self.pads:
            try:
                x = pad.get_axis(0) if pad.get_numaxes() > 0 else 0.0
                y = pad.get_axis(1) if pad.get_numaxes() > 1 else 0.0
                for direction in self.axes_to_directions(x, y):
                    keys.add(DIRECTION_KEYS[direction])
                for h in range(pad.get_numhats()):
                    key = HAT_KEYS.get(pad.get_hat(h))
                    if key:
                        keys.add(key)
            except pygame.error:
                continue
        return keys

    @staticmethod
    def axes_to_directions(x, y):
        """Stick a direcciones, con zona muerta y un solo eje dominante.

        Un solo eje a la vez, porque el tanque se mueve en rejilla: en
        diagonal, manda el eje mas inclinado."""
        if max(abs(x), abs(y)) < AXIS_DEADZONE:
            return []
        if abs(x) >= abs(y):
            return [RIGHT if x > 0 else LEFT]
        return [DOWN if y > 0 else UP]

    @staticmethod
    def button_key(button):
        """Tecla equivalente a un boton, o None si ese boton no hace nada."""
        return BUTTON_KEYS.get(button)
