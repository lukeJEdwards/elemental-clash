from typing import Iterable

from components.base import Point, Size
from components.objects import Screen, Title
from gui.buttons import ReadyButton

from gui.characterIcons import CharacterIcon, ChosenCharacterIcon
from gui.textInput import PlayerLable
from systems.stateMachine import GAME_STATE


from utils.constants import BACKGROUND, Colour, characterType


class CharacterSelectionScreen(Screen):
    def __init__(self, size: Size):
        super().__init__(size)

    @property
    def background(self) -> BACKGROUND:
        return BACKGROUND.MENU_BACKGROUND

    def load_pool(self) -> Iterable:
        return [
            Title(Point(self.width // 2, 50), f"IP:{GAME_STATE.server_ip}", Colour.WHITE, alpha=127),
            CharacterIcon(Point(165, 194), characterType.FIRE),
            CharacterIcon(Point(393, 194), characterType.EARTH),
            CharacterIcon(Point(165, 397), characterType.WATER),
            CharacterIcon(Point(393, 397), characterType.AIR),
            PlayerLable(Point(704, 234), opponent=False),
            ChosenCharacterIcon(Point(1025, 219), opponent=False),
            PlayerLable(Point(704, 437), opponent=True),
            ChosenCharacterIcon(Point(1025, 428), opponent=True),
            ReadyButton(Point(724, 585)),
        ]
