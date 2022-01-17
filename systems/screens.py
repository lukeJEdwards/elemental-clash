from turtle import pos
from typing import Optional
from pygame import Surface

from gui import MenuButton, InputBox, GuiContainer
from systems.renderer import Screen, Renderer

from utils.constants import MENU_BACKGROUND
from utils.fonts import FONT_LIGHT_L
from utils.functions import render_text


def dummy_func():
    print("clicked")


class MainMenu(Screen):
    def __init__(self, size: tuple[int, int], renderer: Optional[Renderer] = None):
        super().__init__(size, renderer)

        self.set_background(MENU_BACKGROUND)

        MARGIN = 60
        pos = (self.width // 2, self.height // 2)

        container = GuiContainer(
            pos,
            MARGIN,
            (MenuButton, pos, "CONNECT", dummy_func),
            (MenuButton, pos, "START SERVER", dummy_func),
            (MenuButton, pos, "EXIT", dummy_func),
        )

        self.init_pool(container)

    def render(self) -> Surface:
        self.canvas = super().render()
        render_text(FONT_LIGHT_L, "ELEMENTAL CLASH", (255, 171, 219), (self.width // 2, 100), self.canvas)
        return self.canvas
