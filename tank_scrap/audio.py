"""Sonido generado en codigo, igual que el pixel art: ni un fichero de audio.

Todo son ondas cuadradas y ruido escritos a mano en PCM de 16 bits mono. Si
la maquina no tiene tarjeta de sonido (o corre con el driver dummy en CI), la
clase se queda muda sin romper nada.
"""
import array
import random

import pygame

RATE = 22050
VOLUME = 0.35


def _samples(n):
    return array.array("h", [0]) * n


def _square(freq_from, freq_to, ms, vol=0.5, duty=0.5):
    """Onda cuadrada con barrido de frecuencia."""
    n = max(1, int(RATE * ms / 1000.0))
    buf = _samples(n)
    phase = 0.0
    for i in range(n):
        t = i / float(n)
        freq = freq_from + (freq_to - freq_from) * t
        phase += freq / RATE
        env = 1.0 - t                      # decae hasta cero
        level = vol * env * (1.0 if (phase % 1.0) < duty else -1.0)
        buf[i] = int(max(-1.0, min(1.0, level)) * 32767)
    return buf


def _noise(ms, vol=0.5, pitch=1.0):
    """Ruido blanco decayendo: explosiones y golpes."""
    n = max(1, int(RATE * ms / 1000.0))
    buf = _samples(n)
    hold = max(1, int(4 / pitch))
    value = 0.0
    for i in range(n):
        if i % hold == 0:
            value = random.uniform(-1.0, 1.0)
        env = (1.0 - i / float(n)) ** 2
        buf[i] = int(max(-1.0, min(1.0, value * vol * env)) * 32767)
    return buf


def _mix(*parts):
    """Encadena trozos uno detras de otro."""
    out = array.array("h")
    for part in parts:
        out.extend(part)
    return out


def _arpeggio(freqs, ms_each, vol=0.4):
    return _mix(*[_square(f, f, ms_each, vol, duty=0.25) for f in freqs])


def _build_bank():
    """Receta de cada efecto. Se genera una vez al arrancar."""
    return {
        "disparo": _square(760, 420, 70, 0.35, duty=0.35),
        "disparo_jefe": _square(320, 140, 140, 0.5, duty=0.5),
        "ladrillo": _noise(60, 0.35, pitch=1.6),
        "acero": _square(1500, 1100, 45, 0.3, duty=0.2),
        "explosion": _mix(_noise(180, 0.6, pitch=0.7),
                          _noise(140, 0.3, pitch=0.4)),
        "explosion_grande": _mix(_noise(260, 0.75, pitch=0.5),
                                 _noise(220, 0.4, pitch=0.3),
                                 _square(180, 60, 160, 0.3)),
        "chatarra": _square(880, 1320, 60, 0.3, duty=0.25),
        "obra": _mix(_square(220, 180, 50, 0.35, duty=0.6), _noise(40, 0.2)),
        "dano": _square(300, 120, 220, 0.45, duty=0.5),
        "sala": _arpeggio((523, 659, 784), 70),
        "mejora": _arpeggio((659, 784, 1047, 1319), 60),
        "jefe": _mix(_square(120, 90, 260, 0.5), _square(160, 110, 260, 0.5)),
        "game_over": _mix(_square(392, 330, 200, 0.45),
                          _square(330, 262, 220, 0.45),
                          _square(262, 98, 420, 0.45)),
    }


class Sfx:
    """Banco de efectos. `enabled` queda en False si no hay audio."""

    def __init__(self, muted=False):
        self.enabled = False
        self.muted = muted
        self.sounds = {}
        try:
            pygame.mixer.pre_init(RATE, -16, 1, 512)
            pygame.mixer.init(RATE, -16, 1, 512)
            self.sounds = {name: pygame.mixer.Sound(buffer=buf.tobytes())
                           for name, buf in _build_bank().items()}
            for snd in self.sounds.values():
                snd.set_volume(VOLUME)
            self.enabled = True
        except (pygame.error, AttributeError, ValueError):
            self.enabled = False          # sin tarjeta de sonido: a jugar mudo

    def play(self, name):
        if not self.enabled or self.muted:
            return
        snd = self.sounds.get(name)
        if snd is not None:
            try:
                snd.play()
            except pygame.error:
                self.enabled = False

    def toggle_mute(self):
        self.muted = not self.muted
        return self.muted


class NullSfx:
    """Version muda, para tests y para --selftest."""

    enabled = False
    muted = True

    def play(self, name):
        pass

    def toggle_mute(self):
        return True
