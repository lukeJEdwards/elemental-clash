
__all__ = ['Screen', 'GuiScreen']

from typing import Optional
from pygame import Surface

from utils import ORIGIN
from systems.input import GuiController
from systems.gameObjects import SelectableGuiObject



class Screen:
    def __init__(self, size:tuple[int, int], render_prev_screen:bool=False, background:Optional[Surface] = None) -> None:
        self.size = size
        self.width:int = size[0]
        self.height:int = size[1]
        self.render_prev_screen:bool = render_prev_screen
        self.background:Surface = background
        self.canvas:Surface = Surface(size)
        
    def render(self) -> Surface:
        if self.background:
            self.canvas.blit(self.background, ORIGIN)
        return self.canvas
    
    
class GuiScreen(Screen):
    def __init__(self, size:tuple[int, int], render_prev_screen:bool=False, background:Optional[Surface] = None) -> None:
        super().__init__(size, render_prev_screen, background)
        self.controller = GuiController()
        
    def set_grid(self, grid:list[list[SelectableGuiObject]]) -> None: self.controller.grid = grid
    
    def update(self, dt:float) -> None:
        self.controller.update(dt)
        
    def render(self) -> None:
        self.render_background()
        self.controller.render(self.canvas)
        return self.canvas