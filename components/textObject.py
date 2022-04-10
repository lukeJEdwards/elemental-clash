from dataclasses import dataclass

from pygame import Surface, Rect
from pygame.font import Font

from utils.constants import COLOUR
from utils.fonts import FONT_NORMAL_M


def text_surface(x: int, y: int, text:str, font:Font=FONT_NORMAL_M, colour:COLOUR=COLOUR.WHITE, alpha=225) -> tuple[Surface, Rect]:
    surf = font.render(text, True, colour.value)
    surf.set_alpha(alpha)
    rect = surf.get_rect()
    rect.center = (x, y + 4)
    return (surf, rect) 

@dataclass
class TextObject:
    text: str
    font: Font = FONT_NORMAL_M
    colour: COLOUR = COLOUR.WHITE
    alpha: int = 255

    def update(self, text: str) -> None:
        self.text = text

    def render(self, context:Surface, x: int, y: int) -> None:
        context.blit(text_surface(x, y, self.text, self.font,self.colour, self.alpha))