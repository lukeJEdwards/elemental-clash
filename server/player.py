from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum, auto
from pickle import dumps, loads

from pygame import Rect

from components.base import Point
from utils.constants import characterState, characterType


class playerAuth(Enum):
    OWNER = auto()
    OPPONENT = auto()


@dataclass
class Player:
    auth: playerAuth = playerAuth.OWNER
    name: str = ""
    ready: bool = False
    pos: Point = field(default=Point)
    collision_box: Rect = None
    character: characterType = characterType.FIRE
    state: characterState = characterState.IDLE
    health: int = 100

    def pickle(self) -> bytes:
        return dumps(self.__dict__)

    def load(self, data: bytes) -> None:
        player: dict = loads(data)
        for __k in player.keys():
            self.__dict__[__k] = player[__k]
