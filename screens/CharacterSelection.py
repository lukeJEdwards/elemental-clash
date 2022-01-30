from gui.characterIcons import CharacterIcon
from gui.container import GuiContainer

from systems.screen import Screen
from systems.stateMachine import SCREEN_STATE

from utils.constants import MENU_BACKGROUND, characterType

__all__ = ["CharacterSelectionScreen"]


class CharacterSelectionScreen(Screen):
    def __init__(self, size: tuple[int, int]):
        super().__init__(size, MENU_BACKGROUND)

    def fill_pool(self) -> None:
        SCREEN_STATE._current_pool.append(
            [
                GuiContainer(
                    (165, 194),
                    100,
                    (CharacterIcon, characterType.FIRE),
                    (CharacterIcon, characterType.EARTH),
                    horizontal=True,
                ),
                GuiContainer(
                    (165, 397),
                    100,
                    (CharacterIcon, characterType.WATER),
                    (CharacterIcon, characterType.AIR),
                    horizontal=True,
                ),
            ]
        )
