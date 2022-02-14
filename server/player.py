from __future__ import annotations
from dataclasses import dataclass, field

from pygame import Rect

from components.base import Point
from utils.constants import characterState, characterType


@dataclass
class Player:
    index: int = 0
    name: str = ""
    ready: bool = False
    pos: Point = field(default=Point)
    collision_box: Rect = None
    character: characterType = characterType.FIRE
    state: characterState = characterState.IDLE
    health: int = 100
