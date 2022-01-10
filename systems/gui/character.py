
__all__ = ['CharacterIcon']

from pygame import Surface
from pygame.constants import SRCALPHA

from utils import load_images, assetsDirs, ORIGIN
from systems.gameObjects import RenderObject, SelectableGuiObject

def get_sprite(filename:str, active:bool):
    filenames = (f'{assetsDirs.ICONS}\\{filename}.png', f'{assetsDirs.UI.BORDERS}\\player-border.png', f'{assetsDirs.UI.BORDERS}\\player-border-background.png')
    scales = ((106, 106), (128, 128), (128, 128))
    canvas = Surface(scales[2], SRCALPHA)
    icon, border, background = load_images(filenames, scales)
    if not active:
        canvas.blit(background, ORIGIN)
    icon_pos = (scales[1][1] - scales[0][1])//2
    canvas.blits(((icon, (icon_pos, icon_pos)), (border, ORIGIN)))
    return canvas

class CharacterIcon(RenderObject, SelectableGuiObject):
    def __init__(self, pos:tuple[int, int], filename:str) -> None:
        DEFAULT_SPRITE = get_sprite(filename, False)
        ACTIVE_SPRITE = get_sprite(filename, True)
        super().__init__(pos, sprite=DEFAULT_SPRITE, default_sprite=DEFAULT_SPRITE, active_sprite=ACTIVE_SPRITE)
    
    def render(self, context:Surface) -> None:
        self.change_sprite(self.get_current_sprite())
        context.blit(self.current_sprite, self.get_center())