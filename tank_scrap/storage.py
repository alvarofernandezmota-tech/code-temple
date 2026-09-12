"""Persistencia minima: solo el record. Nada de partidas guardadas."""
import json
import os

APP_DIR = os.path.join(
    os.environ.get("XDG_DATA_HOME") or os.path.expanduser("~/.local/share"),
    "tank_scrap")
HISCORE_FILE = os.path.join(APP_DIR, "hiscore.json")


def load_hiscore():
    try:
        with open(HISCORE_FILE, "r", encoding="utf-8") as fh:
            return int(json.load(fh).get("hiscore", 0))
    except (OSError, ValueError, TypeError, AttributeError):
        return 0


def save_hiscore(score):
    """Guarda el record. Si el disco no colabora, se ignora sin romper nada."""
    try:
        os.makedirs(APP_DIR, exist_ok=True)
        with open(HISCORE_FILE, "w", encoding="utf-8") as fh:
            json.dump({"hiscore": int(score)}, fh)
        return True
    except OSError:
        return False
