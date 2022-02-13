from typing import Iterable

from components.base import Point, Size
from components.gameObjects import floorObject
from components.objects import RenderObject, Screen

from gui.bars import HealthBar
from gui.characterIcons import CharacterIcon

from systems.stateMachine import GAME_STATE

from utils.constants import BACKGROUND, characterType


class GameScreen(Screen):
    def __init__(self, size: Size):
        super().__init__(size)

    @property
    def background(self) -> BACKGROUND:
        return BACKGROUND.GAME

    def load_pool(self) -> Iterable[RenderObject]:
        return [
            CharacterIcon(Point(10, 10), GAME_STATE[GAME_STATE.my_id].character),
            CharacterIcon(Point(1142, 10), GAME_STATE[GAME_STATE.oppent_id].character),
            HealthBar(Point(148, 40), 100),
            HealthBar(Point(826, 40), 100),
            floorObject(Point(0, 0)),
        ]
