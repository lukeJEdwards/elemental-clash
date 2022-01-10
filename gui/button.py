from typing import Callable, Optional
from pygame import Surface

from gui.guiObject import GuiNavObject
from utils import load_image, assetsDirs

__all__ = ['MenuButton']

class MenuButton(GuiNavObject):
    def __init__(self, pos:tuple[int, int], callback:Callable, text:str) -> None:
        DEFULT_IMAGE:Surface = load_image(f'{assetsDirs.UI.BUTTONS}\\menu-button.png', 2)
        ACTIVE_IMAGE:Surface = load_image(f'{assetsDirs.UI.BUTTONS}\\menu-button-active.png', 2)
        super().__init__(pos, DEFULT_IMAGE, ACTIVE_IMAGE)
        
        self.callback = callback
        self.text = text
        self.direction = True
        self.o_pos = pos
        
    def animation(self, dt:Optional[float]) -> None:
        self.last_upadate += dt
        if self.last_upadate > .035:
            self.reset()
            if self.direction: self.pos.y += 1
            else: self.pos.y -= 1
            
            if self.pos.y == self.o_pos[1] + 5: self.direction = False
            elif self.pos.y == self.o_pos[1] - 5: self.direction = True
                
    
    def update(self, dt:Optional[float]) -> None:
        super().update()
        self.animation(dt)
    
            
        
            

        