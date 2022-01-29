from sys import exit

from systems.renderer import GuiScreen
from gui import MenuButton
from utils import load_background

__all__ = ['TitleScreen']

class TitleScreen(GuiScreen):    
    def __init__(self, size:tuple[int, int]) -> None:
        BACKGROUND_IMAGE = load_background('menu-background.png', size)
        super().__init__(size, BACKGROUND_IMAGE)
        self.set_grid([
            [MenuButton((100, 100), exit, 'PLAY')]
            [MenuButton((100, 100), exit, 'SETTING')]
            [MenuButton((100, 100), exit, 'EXIT')]
        ])
        