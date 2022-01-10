
__all__ = ['GuiController']

from systems.gameObjects import SelectableGuiObject

class GuiController:
    def __init__(self) -> None:
        self.grid:list[list[SelectableGuiObject]] = []
        self.current_index_x:int = -1
        self.current_index_y:int = -1
        
    def next(self) -> None: self.current_index_x = (self.current_index_x + 1) % len(self.grid[self.current_index_x])
    def prev(self) -> None: self.current_index_x = (self.current_index_x - 1) % len(self.grid[self.current_index_x])
    def up(self) -> None: self.current_index_y = (self.current_index_y + 1) % len(self.grid)
    def down(self) -> None: self.current_index_y = (self.current_index_y - 1) % len(self.grid)
    
    def check_x_bounds(self) -> None:
        if self.current_index_x > len(self.grid[self.current_index_y]): 
            self.current_index_x = len(self.grid[self.current_index_y])
            
    def update(self, dt:float) -> None: 
        self.check_x_bounds()
        for list in self.grid:
            for object in list:
                object.update(dt)
    
    def render(self, context):
        for list in self.grid:
            for object in list:
                object.render(context)