from pygame import Surface

from components.base import Size, Vec2
from components.objects import GUIInteractable
from components.textObject import text_surface

from utils.constants import TAG
from utils.fonts import FONT_NORMAL_L
from utils.functions import load_image
from utils.paths import assetsDirs


def make_button_sprite(text: str, active: bool) -> Surface:
    sprite = load_image(f"{assetsDirs.UI}\\menu-button{'-active.png' if active else '.png'}", (336, 76))
    sprite.blit(*text_surface(sprite.get_width() // 2, sprite.get_height() // 2, text, FONT_NORMAL_L))
    return sprite

class Button(GUIInteractable):

    def __init__(self, pos:Vec2, text:str):
        SPRITE: Surface = make_button_sprite(text, False)
        super().__init__(TAG.UI, pos, Size(SPRITE.get_size()), SPRITE)
