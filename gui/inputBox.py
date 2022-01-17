from pygame import K_BACKSPACE, Surface
from pygame.constants import MOUSEBUTTONDOWN, KEYDOWN
from pygame.event import Event
from pygame.font import Font

from systems.gameObjects import Selectable

from utils.constants import WHITE
from utils.functions import load_image, render_text
from utils.paths import assetsDirs

__all__ = ["InputBox"]


class InputBox(Selectable):
    def __init__(self, pos: tuple[int, int], font: Font, filler_text: str):
        size = (306, 48)
        DEFAULT_SPRITE = load_image(f"{assetsDirs.UI}\\text-input.png", size)
        ACTIVE_SPRITE = load_image(f"{assetsDirs.UI}\\text-input-active.png", size)
        super().__init__(pos, DEFAULT_SPRITE, ACTIVE_SPRITE)

        self.text: str = ""
        self.font: Font = font
        self.filler_text: str = filler_text
        self.active = False

        self.max_length: callable = lambda: len(self.text) < 5

    def is_active(self):
        return self.active

    def capture_events(self, event: Event) -> None:
        if event.type == MOUSEBUTTONDOWN:
            if super().is_active():
                self.active = True
            else:
                self.active = False

        if event.type == KEYDOWN and self.active:
            if event.key == K_BACKSPACE:
                self.text = self.text[:-1]
            elif self.max_length():
                self.text += event.unicode

    def render(self, context: Surface):
        super().render(context)

        text_surface = render_text(self.font, self.text.upper(), WHITE)
        pos = (self.pos.x - text_surface.get_width() // 2, self.pos.y - text_surface.get_height() // 2)
        context.blit(text_surface, pos)
