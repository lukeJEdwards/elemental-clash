from enum import Enum

from pygame import Surface

from systems.settings import SETTINGS

from utils.functions import load_image
from utils.paths import assetsDirs

"""
all constants defined for use across the whole game
"""

ORIGIN: tuple[int, int] = (0, 0)


class BACKGROUND(Enum):
    MENU_BACKGROUND: Surface = load_image(f"{assetsDirs.BACKGROUNDS}\\menu-background.png", SETTINGS["SIZE"])
    GAME: Surface = load_image(f"{assetsDirs.BACKGROUNDS}\\game_background.png", SETTINGS["SIZE"])
    GAME_FLOOR: Surface = load_image(f"{assetsDirs.BACKGROUNDS}\\floor.png", SETTINGS["SIZE"])
    WIN: Surface = Surface(SETTINGS["SIZE"])

class Colour(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    FILLER = (255, 255, 255, 127)
    TITLE = (255, 171, 219)


class characterType(Enum):
    FIRE = "fire_knight"
    WATER = "water_priestess"
    EARTH = "ground_monk"
    AIR = "wind_hashashin"
    NONE = None


class characterState(Enum):
    AKT = "atk"
    DEATH = "death"
    DEFEND = "defend"
    IDLE = "idle"
    JUMP = "jump"

class notificationType(Enum):
    ERROR = "notification-error"
    ALERT = "notification-alert"
    SUCCESS = "notification-success"
