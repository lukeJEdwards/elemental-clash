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


class characterState(Enum):
    ATK_1 = "1_atk"
    ATK_2 = "1_atk"
    ATK_3 = "3_atk"
    ATK_SP = "sp_atk"
    DEATH = ("death",)
    DEFEND = ("defend",)
    IDLE = ("idle",)
    JUMP = ("jump",)
    ROLL = ("roll",)
    RUN = ("run",)
    TAKE_HIT = ("take_hit",)
    MEDITATE = ("meditate",)
    HEAL = ("heal",)


class notificationType(Enum):
    ERROR = "notification-error"
    ALERT = "notification-alert"
    SUCCESS = "notification-success"
