from typing import Optional
from uuid import uuid4

from systems.gameObjects.gameObject import RenderObject, GameObject, Animatable


__all__ = ['ObjectPool', 'GameObjectPool', 'AnimatablePool']

class ObjectPool:
    """Object pool for holding objects.

    Args:
        category (Optional[str], optional): Category of the object for the renderer to categorise it. Defaults to None.
    """
    def __init__(self, category:Optional[str]=None):
        self.id:str = uuid4().hex
        self.category:str = category
        self.pool:dict[str:RenderObject] = {}
        
    def __getitem__(self, id:str) -> RenderObject:
        """return the item from the pool stored under the given id.

        Args:
            id (str): The id of the object trying to be retrived.

        Returns:
            RenderObject: The object stored under the given id.
        """
        return self.pool[id]
    
    def __setitem__(self, id:str, obj:RenderObject) -> None:
        """Adds object to the pool under the given id.

        Args:
            id (str): Key of the object in the pool.
            obj (RenderObject): Object being stored.
        """
        assert isinstance(obj, RenderObject)
        self.pool[id] = obj
        
    def values(self) -> list[RenderObject]:
        """Return list all objects in the pool.

        Returns:
            list[RenderObject]: A list of objects in the pool.
        """
        return self.pool.values()

    
    def clear(self):
        """Removes all objects from the pool."""
        self.pool.clear()


class GameObjectPool(ObjectPool):
    """Object pool for holding game objects.

    Args:
        category (Optional[str], optional): Category of the object for the renderer to categorise it. Defaults to None.
    """
    def __init__(self, category:Optional[str]=None) -> None:
        super().__init__(category)
        
    def __getitem__(self, id:str) -> GameObject:...
    def __setitem__(self, id:str, obj:GameObject) -> None:...
    def values(self) -> list[GameObject]:...
        
    def has_collided(self, game_object:GameObject) -> Optional[GameObject]:
        """To see if a collision has occurred
        
        Check to see if the game object has collided with the any object in the
        pool. If so, returns the first object it has collided with.

        Returns:
            Optional[GameObject]: If found the game object that has collide with the game object passed in.
        """
        for obj in self.pool.values():
            assert isinstance(obj, GameObject)
            if obj.has_collided(game_object.rect):
                return obj
            
            
class AnimatablePool(GameObjectPool):
    """Object pool for holding game objects that have animation.

    Args:
        category (Optional[str], optional): Category of the object for the renderer to categorise it. Defaults to None.
    """
    def __init__(self, category:Optional[str]=None) -> None:
        super().__init__(category)  
        
    def __getitem__(self, id:str) -> Animatable:...
    def __setitem__(self, id:str, obj:Animatable) -> None:...
    def values(self) -> list[Animatable]:...
    
    def update(self, dt:float) -> None:
        """Updates all objects in the pool.

        Args:
            dt (float): Delta time in seconds.
        """
        for obj in self.pool.values():
            assert isinstance(obj, Animatable)
            obj.update(dt) 
        
            
            
            
            