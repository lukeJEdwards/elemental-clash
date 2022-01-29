from gui.buttons import MainMenuButton
from gui.container import GuiContainer
from gui.textInput import TextInput

from systems.screen import Screen
from systems.settings import SETTINGS
from systems.stateMachine import SCREEN_STATE
from utils.constants import MENU_BACKGROUND

__all__ = ["MainMenuScreen"]


class MainMenuScreen(Screen):
    def __init__(self, size: tuple[int, int]):
        super().__init__(size, MENU_BACKGROUND)

        SCREEN_STATE._current_pool.append(
            [
                GuiContainer(
                    (312, 242),
                    60,
                    (MainMenuButton, "CONNECT"),
                    (MainMenuButton, "START SERVER"),
                    (MainMenuButton, "EXIT", exit),
                ),
                GuiContainer(
                    (797, 341),
                    60,
                    (TextInput, "ENTER NAME", SETTINGS["NAME"]),
                    (TextInput, "ENTER IP", SETTINGS["IP"]),
                ),
            ]
        )
