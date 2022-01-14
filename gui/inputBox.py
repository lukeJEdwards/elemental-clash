from typing import Optional

from pygame import K_RETURN, Surface
from pygame.constants import MOUSEBUTTONUP, KEYDOWN
from pygame.event import Event

from systems.gameObjects import Selctable

from utils.constants import WHITE
from utils.functions import load_image, render_text
from utils.fonts import FONT_NORMAL_L
from utils.paths import assetsDirs

__all__ = ["InputBox"]


class InputBox(Selctable):
    def __init__(self, pos: tuple[int, int], filler_text: str):
        size = (408, 64)
        DEFAULT_SPRITE = load_image(f"{assetsDirs.UI}\\text-input.png", size)
        ACTIVE_SPRITE = load_image(f"{assetsDirs.UI}\\text-input-active.png", size)
        super().__init__(pos, DEFAULT_SPRITE, ACTIVE_SPRITE)

        self.text: str = ""
        self.filler_text: str = filler_text
        self.active = False

        self.max_length: callable = lambda: len(self.text) < 5

    def capture_events(self, event: Event) -> None:
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def render(self, context: Surface):
        render_text(
            self.current_sprite,
            FONT_NORMAL_L,
            self.text,
            WHITE,
            (self.width // 2, self.height // 2),
        )
        super().render(context)
