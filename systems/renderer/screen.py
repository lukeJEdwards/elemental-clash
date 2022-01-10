from pygame import Surface

from gui.guiObject import GuiNavObject
from systems.gameObjects import ObjectPool
from systems.guiController import GuiController
from utils import ORIGIN

__all__ = ['Screen', 'GuiScreen']

class Screen:
    def __init__(self, size:tuple[int, int], background:Surface) -> None:
        self.width:int = size[0]
        self.height:int = size[1]
        self.size:tuple = size
        self.overlay:bool = False
        self.canvas:Surface = Surface(size)
        self.background:Surface = background
        
    def render(self) -> Surface:
        if self.background: self.canvas.blit(self.background, ORIGIN)
        return self.canvas
    
class GuiScreen(Screen):
    def __init__(self, size:tuple[int, int], background:Surface) -> None:
        super().__init__(size, background)
        self.controller = GuiController()
        
    def set_grid(self, grid:list[list[GuiNavObject]]):self.controller.grid = grid
    
    def update(self, actions:dict, dt:float) -> None: 
        self.controller.update(actions, dt)
        
    def render(self) -> Surface:
        super().render()
        self.controller.render(self.canvas)
        return self.canvas
    
class GameScreen(Screen):
    def __init__(self, size:tuple[int,int], background:Surface) -> None:
        super().__init__(size, background)
        self.object_pool = ObjectPool()
        
    def update(self, dt:float) -> None: 
        for obj in self.object_pool.values(): obj.update(dt)
        
    def render(self) -> Surface:
        super().render()
        for obj in self.object_pool.values(): obj.render(self.canvas)
        return self.canvas
        
        
        
        