from systems.renderer import Screen
from utils import load_background

__all__ = ['TitleScreen']

class TitleScreen(Screen):    
    def __init__(self, size:tuple[int, int]) -> None:
        BACKGROUND_IMAGE = load_background('menu-background.png', size)
        super().__init__(size, BACKGROUND_IMAGE)