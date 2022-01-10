from typing import Optional
from pygame import Surface, mouse

from systems.gameObjects import RenderObject


__all__ = ['GuiNavObject']

class GuiNavObject(RenderObject):
    def __init__(self, pos:tuple, default_image:Surface, active_image:Surface, **kwargs) -> None:
        super().__init__(pos, default_image, **kwargs)
        self.default_image = default_image
        self.active_image = active_image
        self.current_image = default_image
        self.last_upadate = 0
        self.is_active = False
        
    def activate(self):self.is_active = True
    def deactivate(self):self.is_active = False
    def reset(self): self.last_upadate = 0   
        
    def if_active(self):
        if self.is_active: self.current_image = self.active_image
        else: self.current_image = self.default_image
        
    def mouse_hover(self): return self.rect.collidepoint(mouse.get_pos())
    def update(self, dt:Optional[float]=None) -> None: self.if_active()
        