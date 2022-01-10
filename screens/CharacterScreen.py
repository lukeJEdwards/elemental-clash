
__all__ = ['CharacterScreen']

from utils import load_background
from systems.renderer import GuiScreen
from systems.gui import CharacterIcon

class CharacterScreen(GuiScreen):
    def __init__(self, size: tuple[int, int]) -> None:
        super().__init__(size, background=load_background('menu-background.png', size))
        self.set_grid([
            [CharacterIcon((self.width//4, self.height//4), 'fire_knight'),
            CharacterIcon((self.width//4 * 3, self.height//4), 'ground_monk')],
            [CharacterIcon((self.width//4, self.height//4 * 3), 'water_priestess'),
            CharacterIcon((self.width//4 * 3, self.height//4* 3), 'wind_hashashin')]
        ])