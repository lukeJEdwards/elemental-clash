
__all__ = ['TitleScreen']

from sys import exit

from utils import load_background
from systems.renderer import GuiScreen
from systems.gui import MenuButton

class TitleScreen(GuiScreen):
    def __init__(self, size:tuple[int,int]):
        super().__init__(size, background=load_background('menu-background.png', size))
        margin = 150
        self.set_grid([
            [MenuButton([size[0]//2, size[1]//2 - margin], 'PLAY', exit)],
            [MenuButton([size[0]//2, size[1]//2], 'SETTINGS', exit)],
            [MenuButton([size[0]//2, size[1]//2 + margin], 'EXIT', exit)]
        ])        