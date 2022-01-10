from __future__ import annotations
from typing import Optional

from uuid import uuid4
from pygame import Rect, Surface
from pygame.math import Vector2


__all__ = ['RenderObject', 'GameObject', 'Animatable']

class RenderObject:
    def __init__(self, pos:tuple, image:Surface, **kwargs) -> None:
        super().__init__(**kwargs)
        self.pos:Vector2 = Vector2(pos)
        self.image:Surface = image
        self.size:tuple = self.image.get_size()
        self.width:int = self.size[0]
        self.height:int = self.size[1]
        self.rect:Rect = Rect(self.pos, self.size)
        
    def render(self, context:Surface) -> None: context.blit(self.image, self.pos)

class GameObject(RenderObject):
    def __init__(self, pos:tuple, image:Surface, **kwargs) -> None:
        super().__init__(pos=pos, image=image, **kwargs)
        self.id:str = uuid4().hex
        
    def has_collided(self, obj:GameObject|tuple) -> bool:  
        if isinstance(obj, GameObject): return self.rect.colliderect(obj.rect)
        elif isinstance(obj, tuple): return self.rect.collidepoint(obj)
    
    def update(self, dt:Optional[float]=None) -> None: pass
        
    
class Animatable(GameObject):
    def __init__(self, pos:tuple, images:list[Surface], **kwargs) -> None:
        super().__init__(pos, images[0], **kwargs)
        self.images:list[Surface] = images
        self.current_index = 0
        self.current_image = self.images[0]
        self.last_updated:float = 0
        
    def reset(self) -> None: self.last_updated = 0
    def next(self) -> None: self.current_index = (self.current_index + 1) % len(self.images)
    def animation(self, dt:float) -> None: self.last_updated += dt
    def update(self, dt:float) -> None: pass       
        
