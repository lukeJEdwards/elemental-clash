from typing import Optional
from uuid import uuid4

from systems.gameObjects.gameObject import GameObject, Animatable


__all__ = ['ObjectPool', 'AnimatablePool']

class ObjectPool:
    def __init__(self):
        self.id:str = uuid4().hex
        self.pool:dict[str:GameObject] = {}
        
    def __getitem__(self, id:str) -> GameObject: return self.pool[id]
    def __setitem__(self, id:str, obj:GameObject) -> None:
        assert isinstance(obj, GameObject)
        self.pool[id] = obj
        
    def values(self) -> list[GameObject]: return self.pool.values()
    def items(self) -> list[GameObject]: return self.pool.items()
    def keys(self) -> list[GameObject]: return self.pool.keys()
    
    def clear(self): self.pool.clear()
        
    def has_collided(self, game_object:GameObject) -> Optional[GameObject]:
        for obj in self.pool.values():
            assert isinstance(obj, GameObject)
            if obj.has_collided(game_object.rect): return obj
            
            
class AnimatablePool(ObjectPool):
    def __init__(self) -> None:
        super().__init__()  
        
    def __getitem__(self, id:str) -> Animatable:...
    def __setitem__(self, id:str, obj:Animatable) -> None:...
    def values(self) -> list[Animatable]:...
    def items(self) -> list[Animatable]:...
    def keys(self) -> list[Animatable]:...
    
    def update(self, dt:float) -> None:
        for obj in self.pool.values():
            assert isinstance(obj, Animatable)
            obj.update(dt) 
        
            
            
            
            