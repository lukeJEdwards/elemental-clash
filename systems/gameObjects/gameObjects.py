from __future__ import annotations
from typing import Optional


__all__ = ['RenderObject', 'GameObject', 'SelectableGuiObject', 'Animatiable']

from pygame import Rect, Surface
from pygame.math import Vector2


class RenderObject:
    def __init__(self, pos:list[int, int], sprite:Surface, **kwargs) -> None:
        super().__init__(**kwargs)
        self.pos:list[int, int] = pos
        self.current_sprite:Surface = sprite
        self.size:tuple[int, int] = self.current_sprite.get_size()
        self.width:int = self.size[0]
        self.height:int = self.size[1]
        
    def get_center(self) -> tuple[int, int]: return (self.pos[0] - self.width//2, self.pos[1] - self.height//2)
        
    def change_sprite(self, sprite:Surface) -> None: self.current_sprite = sprite
        
    def render(self, context:Surface) -> None: context.blit(self.current_sprite, self.pos)
    
class SelectableGuiObject:
    def __init__(self, default_sprite:Surface, active_sprite:Surface, **kwargs):
        super().__init__(**kwargs)
        self.default_sprite:Surface = default_sprite
        self.active_sprite:Surface = active_sprite
        self.is_active = False
        
    def activate(self) -> None: self.is_active = True
    def deactivate(self) -> None: self.is_active = False
    
    def get_current_sprite(self) -> Surface: return self.active_sprite if self.is_active else self.default_sprite
    
    def update(self, dt:Optional[float]=None) -> None: pass
    
class GameObject(RenderObject):
    def __init__(self, pos:list[int, int], sprite:Surface) -> None:
        super().__init__(pos, sprite)
        self.x:int = pos[0]
        self.y:int = pos[1]
        self.rect:Rect = self.current_sprite.get_rect()
        
    def has_colllided(self, obj:GameObject|Vector2|list[int, int]) -> bool:
        if isinstance(obj, GameObject): return self.rect.colliderect(obj.rect)
        elif isinstance(obj, Vector2): return self.rect.collidepoint(obj.x, obj.y)
        elif isinstance(obj, tuple): return self.rect.collidepoint(obj)
        return False
    
    def update(self, dt:float) -> None: pass
    
class Animatiable(RenderObject):
    def __init__(self, pos:list[int, int], sprites:list[Surface]) -> None:
        super().__init__(pos, sprites[0])
        self.sprite_list:list[Surface] = sprites
        self.current_index:int = 0
        self.last_updated:float = 0
        
    def update(self, dt:float) -> None: 
        self.last_updated += dt
        self.current_sprite = self.sprite_list[self.current_index]
    
    def next(self) -> None: (self.current_index + 1) % len(self.sprite_list)
    def prev(self) -> None: (self.current_index - 1) % len(self.sprite_list)
    def reset(self) -> None: self.last_updated = 0
        