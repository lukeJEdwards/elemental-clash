import socket
from enum import Enum
from pygame import Surface

from systems.settings import SETTINGS

from utils.functions import load_image
from utils.paths import assetsDirs


ORIGIN: tuple[int, int] = (0, 0)

IP = socket.gethostbyname(socket.gethostname())
PORT = 5555
BUFFER = 512


class BACKGROUND(Enum):
    MENU_BACKGROUND: Surface = load_image(f"{assetsDirs.BACKGROUNDS}\\menu-background.png", SETTINGS["SIZE"])
    GAME: Surface = load_image(f"{assetsDirs.BACKGROUNDS}\\background_0.png", SETTINGS["SIZE"])
    GAME_FLOOR: Surface = load_image(f"{assetsDirs.BACKGROUNDS}\\floor.png", SETTINGS["SIZE"])


class BARS(Enum):
    HEALTH: Surface = load_image(f"{assetsDirs.UI}\\health_bar.png", (306, 48))
    ENERGY: Surface = load_image(f"{assetsDirs.UI}\energy_bar.png", (384, 64))


class Colour(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    FILLER = (255, 255, 255, 127)
    TITLE = (255, 171, 219)


class characterType(Enum):
    FIRE = f"{assetsDirs.ICONS}\\fire_knight.png"
    WATER = f"{assetsDirs.ICONS}\\water_priestess.png"
    EARTH = f"{assetsDirs.ICONS}\\ground_monk.png"
    AIR = f"{assetsDirs.ICONS}\\wind_hashashin.png"
    NONE = None


class characterState(Enum):
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


class notificationType(Enum):
    ERROR = "notification-error"
    ALERT = "notification-alert"
    SUCCESS = "notification-success"
