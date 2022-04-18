from enum import Enum, auto
from pygame import K_LEFT, K_LEFTBRACKET, K_RIGHT, K_RIGHTBRACKET, K_UP

from pygame.locals import K_w, K_a, K_d, K_e, K_q

"""
Setting for the game
"""

class keyMappings(Enum):
    JUMP = auto()
    LEFT = auto()
    RIGHT = auto()
    AKT = auto()
    DEFEND = auto()

SETTINGS = {
    "FULL_SCREEN": False,
    "FPS_TARGET": 60,
    "SIZE": (1280, 720),
}


PLAYER_1_KEYS = {
    keyMappings.JUMP: K_w,
    keyMappings.LEFT: K_a,
    keyMappings.RIGHT: K_d,
    keyMappings.AKT: K_q,
    keyMappings.DEFEND: K_e,
}

PLAYER_2_KEYS = {
    keyMappings.JUMP: K_UP,
    keyMappings.LEFT: K_LEFT,
    keyMappings.RIGHT: K_RIGHT,
    keyMappings.AKT: K_LEFTBRACKET,
    keyMappings.DEFEND: K_RIGHTBRACKET,
}