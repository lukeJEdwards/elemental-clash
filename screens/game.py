from typing import Iterable

from components.character import Character
from components.base import Point, Size, staticPoint
from components.gameObjects import floorObject, ScoreObject
from components.Objects import RenderObject, Screen

from gui.characterIcons import ChosenCharacterIcon

from utils.constants import BACKGROUND


class GameScreen(Screen):
    def __init__(self, size: Size):
        super().__init__(size)

    @property
    def background(self) -> BACKGROUND:
        return BACKGROUND.GAME

    def load_pool(self) -> Iterable[RenderObject]:
        return [
            ChosenCharacterIcon(Point(10, 10), 0, (106, 106)),
            ChosenCharacterIcon(Point(1142, 10), 1, (106, 106)),
            ScoreObject(staticPoint(620,50), 0),
            ScoreObject(staticPoint(660,50), 1),
            floorObject(Point(0, 0)),
            Character(staticPoint(0, 323), 0, False),
            Character(staticPoint(608, 323), 1, True),
        ]
