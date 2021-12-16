from pygame import Surface
from systems.gameObjects import ObjectPool
from utils import ORIGIN

GAME_OBJECTS:str = 'gameobject'
GUI_LAYER:str = 'gui'

class Screen:
    """The base class for all screen objects.

    Args:\n
        width (int): The width of the screen.
        height (int): The height of the screen.
        background (Surface): The background of the screen.
        
    Attributes:\n
        width (int): The width of the screen.
        height (int): The height of the screen.
        size (tuple): The size of the screen.
        overlay (bool): Whether the previous screen should be rendered underneath.
        canvas (Surface): The surface that all objects will be rendered to.
        background (Surface): The background of the screen.
        object_pool (ObjectPool): The object pool that contains all objects.
    """
    def __init__(self, size:tuple[int, int], background:Surface) -> None:
        self.width:int = size[0]
        self.height:int = size[1]
        self.size:tuple = size
        self.overlay:bool = False
        self.canvas:Surface = Surface(self.size)
        self.background:Surface = background
        self.object_pool:ObjectPool = ObjectPool()
        
    def update(self, dt:float, actions:dict) -> None:
        """Updates all objects in object pool.

        Args:
            dt (float): Delta time in seconds.
            actions (dict): Action dictionary.
        """
        for obj in self.object_pool:
            obj.update(dt)
            
    def render(self) -> Surface:
        """Render all objects in object pool to the canvas.

        Returns:
            Surface: The canvas after being rendered.
        """
        self.canvas.blit(self.background, ORIGIN)
        for obj in self.object_pool.values():
            obj.render(self.canvas)
        return self.canvas
        
        
        