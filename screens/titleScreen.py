from systems.renderer import Screen
from utils import load_background


class TitleScreen(Screen):
    
    BACKGROUND_IMAGE = load_background('menu-background.png')
    
    def __init__(self, size:tuple[int, int]) -> None:
        super().__init__(size, TitleScreen.BACKGROUND_IMAGE)