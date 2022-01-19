from systems.screen import Screen
from utils.constants import MENU_BACKGROUND

__all__ = ["GameScreen"]


class GameScreen(Screen):
    def __init__(self, size: tuple[int, int]):
        super().__init__(size, MENU_BACKGROUND)
