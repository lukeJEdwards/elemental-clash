
from dataclasses import dataclass, field

from components.base import Vec2

@dataclass
class Player:
    pos:Vec2 = field(default_factory=lambda: Vec2(0,0))

@dataclass
class PlayerStats:
    player1: Player = field(default_factory=Player)