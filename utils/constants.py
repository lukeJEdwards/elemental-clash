from enum import Enum

from pygame import Surface

from systems.settings import SETTINGS
from utils.functions import load_background

__all__ = ["ORIGIN", "BLACK", "WHITE", "MENU_BACKGROUND"]


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
