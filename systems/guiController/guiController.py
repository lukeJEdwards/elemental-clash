from gui import GuiNavObject

__all__ = ["GuiController"]

class GuiController:
    def __init__(self) -> None:
        self.grid:list[list[GuiNavObject]] = []
        self.current_index_x:int = -1
        self.current_index_y:int = -1
        self.current_selected:GuiNavObject = None       
        
    def next(self) -> None: (self.current_index_x + 1) % len(self.grid[self.current_index_x])
    def prev(self) -> None: (self.current_index_x - 1) % len(self.grid[self.current_index_x])
    def down(self) -> None: (self.current_index_y - 1) % len(self.grid)
    def up(self) -> None: (self.current_index_y + 1) % len(self.grid)
    
    def add(self, obj:GuiNavObject, x:int, y:int) -> None:
        if isinstance(self.grid[x], list): self.grid[x][y] = obj
        else: self.grid[x] = [obj] 
            
    def get_current_selected(self) -> None:
        if self.current_selected:
            self.current_selected.deactivate()
            self.current_selected = self.grid[self.current_index_x][self.current_index_y]
            self.current_selected.activate()
        
    def update(self, actions:dict, dt:float) -> None: 
        if actions['UP']: self.up()
        elif actions['DOWN']: self.down()
        elif actions['LEFT']: self.prev()
        elif actions['RIGHT']: self.next()
        self.get_current_selected()
        
        for i in range(len(self.grid)):
            if isinstance(self.grid[i], list):
                for j in range(len(self.grid[i])):
                    self.grid[i][j].update(dt)
            else:
                self.grid[i].update(dt)
        
    def render(self, context) -> None:
        for i in range(len(self.grid)):
            if isinstance(self.grid[i], list):
                for j in range(len(self.grid[i])):
                    self.grid[i][j].render(context)
            else:
                self.grid[i].render(context)