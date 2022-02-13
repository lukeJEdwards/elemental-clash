from __future__ import annotations
from uuid import uuid4

from pygame import Rect, Surface
from components.base import Location, Point, Size
from utils.constants import BACKGROUND


class gameObject(Location):
    def __init__(self, pos: Point, currrent_sprite: Surface) -> None:
        super().__init__(pos, Size(*currrent_sprite.get_size()))

        self.currrent_sprite: Surface = currrent_sprite
        self.rect: Rect = currrent_sprite.get_rect()

    def collision_check(self, __obj: gameObject) -> bool:
        return self.rect.colliderect(__obj.rect)

    def render(self, contex: Surface) -> None:
        contex.blit(self.currrent_sprite, self.pos.toTuple())


class floorObject(gameObject):
    def __init__(self, pos: Point) -> None:
        super().__init__(pos, BACKGROUND.GAME_FLOOR.value)
        self.id = uuid4()
