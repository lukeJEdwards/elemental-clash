from typing import Iterable

from components.base import Point, Size
from components.Objects import Screen
from gui.buttons import ReadyButton

from gui.characterIcons import CharacterIcon, ChosenCharacterIcon
from gui.textInput import PlayerLable


from utils.constants import BACKGROUND, characterType


class CharacterSelectionScreen(Screen):
    def __init__(self, size: Size):
        super().__init__(size)

    @property
    def background(self) -> BACKGROUND:
        return BACKGROUND.MENU_BACKGROUND

    def load_pool(self) -> Iterable:
        return [
            CharacterIcon(Point(165, 194), characterType.FIRE),
            CharacterIcon(Point(393, 194), characterType.EARTH),
            CharacterIcon(Point(165, 397), characterType.WATER),
            CharacterIcon(Point(393, 397), characterType.AIR),
            PlayerLable(Point(704, 234), 0),
            ChosenCharacterIcon(Point(1025, 219), 0),
            PlayerLable(Point(704, 437), 1),
            ChosenCharacterIcon(Point(1025, 428), 1),
            ReadyButton(Point(724, 585)),
        ]
