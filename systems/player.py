from dataclasses import dataclass, field

from pygame import Rect, math

from components.base import Point
from utils.constants import characterState, characterType

"""
all data needed for each player
"""


@dataclass
class Player:
    name: str = ""
    pos: math.Vector2 = field(default_factory=math.Vector2)
    collision_box: Rect = None
    atk_collision_box: Rect = None
    character: characterType = characterType.FIRE
    state: characterState = characterState.IDLE
    hit_count: int = 0
