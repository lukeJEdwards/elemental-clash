from enum import Enum, IntEnum

from pygame import Surface

from systems.settings import SETTINGS
from utils.functions import load_background

__all__ = [
    "ORIGIN",
    "BLACK",
    "WHITE",
    "MENU_BACKGROUND",
    "screenState",
    "gameState",
]


ORIGIN: tuple[int, int] = (0, 0)
BLACK: tuple[int, int, int] = (0, 0, 0)
WHITE: tuple[int, int, int] = (255, 255, 255)


MENU_BACKGROUND: Surface = load_background("menu-background.png", SETTINGS["SIZE"])


class characterType(Enum):
    FIRE = "fire_knight"
    WATER = "water_priestess"
    EARTH = "ground_monk"
    AIR = "wind_hashashin"
    NONE = ""


class screenState(IntEnum):
    NONE = 0
    MAIN_MENU = 1
    SETTINGS = 2
    CHARACTER_SELECTION = 3
    GAME = 4


class gameState(IntEnum):
    NONE = 0
    MOVING = 1
    ATTACKING = 2
    DEFENDING = 3
