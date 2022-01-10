
__all__ = ['ControllerDisconnectScreen']

from pygame import Surface

from utils import load_image, assetsDirs, BLACK
from systems.renderer import Screen

class ControllerDisconnectScreen(Screen):
    def __init__(self, size: tuple[int, int]) -> None:
        super().__init__(size, True)
        self.icon = load_image(f'{assetsDirs.UI.PLAYER_INPUTS}\\XOne.png')
        
    def render(self) -> Surface:
        self.canvas.fill((255, 255, 255, 120))
        self.canvas.blit(self.icon, (self.width//2, self.height//2))
        return super().render()