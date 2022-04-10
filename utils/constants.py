from enum import Enum, auto
from pygame import Surface

from systems.settings import SETTINGS

from utils.functions import load_image
from utils.paths import assetsDirs



ORIGIN: tuple[int, int] = (0, 0)


class TAG(Enum):
    GAME_OBJ = auto()
    UI = auto()

class SCREEN(Enum):
    MENU = 0
    SELECTION = 1
    GAME = 3
    PAUSE = 4
    END = 5
    CLOSE = 6

class BACKGROUND(Enum):
    MENU_BACKGROUND: Surface = load_image(f"{assetsDirs.BACKGROUNDS}\\menu-background.png", SETTINGS["SIZE"].to_tuple())
    GAME: Surface = load_image(f"{assetsDirs.BACKGROUNDS}\\background_0.png", SETTINGS["SIZE"].to_tuple())
    GAME_FLOOR: Surface = load_image(f"{assetsDirs.BACKGROUNDS}\\floor.png", SETTINGS["SIZE"].to_tuple())

class COLOUR(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    FILLER = (255, 255, 255, 127)
    TITLE = (255, 171, 219)

class CHARACTER_TYPE(Enum):
    FIRE = f"{assetsDirs.ICONS}\\fire_knight.png"
    WATER = f"{assetsDirs.ICONS}\\water_priestess.png"
    EARTH = f"{assetsDirs.ICONS}\\ground_monk.png"
    AIR = f"{assetsDirs.ICONS}\\wind_hashashin.png"
    NONE = None

class CHARACTER_STATE(Enum):
    ATK_1 = "1_atk"
    ATK_2 = "1_atk"
    ATK_3 = "3_atk"
    ATK_SP = "sp_atk"
    DEATH = "death"
    DEFEND = "defend"
    IDLE = "idle"
    JUMP = "jump"
    ROLL = "roll"
    RUN = "run"
    TAKE_HIT = "take_hit"
    MEDITATE = "meditate"
    HEAL = "heal"