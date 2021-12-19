from __future__ import annotations

from uuid import uuid4
from pygame import Rect, Surface
from pygame.math import Vector2


__all__ = ['RenderObject', 'GameObject', 'Animatable', 'MoveableObject']

class RenderObject:
    """RenderObject class is for anthing that will be rendered to the screen.
    
    This class is the base class for all objects that will be rendered to the screen, this includes game objects, gui 
    objects, etc. This class can not be updated so only use for static assets that won't need to be updated. These
    Objects will be not have collision as well.
    
    Args:\n
        pos (tuple): Position of the object.
        image (Surface): Image to rendered.
        category (str): Category of the object for the renderer to categorise it.
        
    Attributes:\n
        id (str): A unique identifier for the object meant for quicker removal.
        category (str): Category of the object for the renderer to categorise it.
        pos (math.Vector2 ): Position of the object
        image (Surface): Image to be rendered.
        
    """
    def __init__(self, pos:tuple, image:Surface, category:str) -> None:
        self.id:str = uuid4().hex
        self.category:str = category
        self.pos:Vector2 = Vector2(pos)
        self.image:Surface = image
        
    def render(self, context:Surface) -> None: 
        """Method to render the object

        Args:
            context (Surface): The surface to render the image to.
        """
        context.blit(self.image, self.pos)
        
class GameObject(RenderObject):
    """GameObject class is for anything that will be classed as a game object.
    
    This class is the base class for all objects that will be classed as a game object. All game objects will inherit 
    from this class. Unlike it's parent class, RenderObject, this class will be able to detect collision with other 
    objects.
    
    Inherit:\n 
        RenderObject
        
    Args:\n
        pos (tuple): position of the object.
        image (Surface): Image to rendered.
        
    Attributes:\n
        size (tuple): Size of the object
        width (int): Width of the object.
        height (int): Height of the object.
        rect (Rect): Collisiton box of the object.
        
    """
    def __init__(self, pos:tuple, image:Surface, category:str) -> None:
        super().__init__(pos, image, category)
        
        self.size:tuple = self.image.get_size()
        self.width:int = self.size[0]
        self.height:int = self.size[1]
        self.rect:Rect = Rect(self.pos, self.size)
        
    def has_collided(self, game_object:GameObject) -> bool: 
        """check to see if there has been a collision.
        
        checks to see if the collision box of the current object is intersecting with
        the other object's collision box.

        Args:
            game_object (GameObject): the game object being checked is in the collision box.

        Returns:
            bool: If the objects are colliding then returns True.
        """
        return self.rect.colliderect(game_object.rect)     
        
        
class Animatable(GameObject):
    """The class for all animatable objects.

    This class is a base class for all animatable objects.
    
    Inherit:\n 
        RenderObject
        GameObject
        
    Args:\n
        pos (tuple): position of the object.
        image (List[Surface]): List of images for animation.
        category (str): Category of the object for the renderer to categorise it.
        
    Attributes:\n
        image (List[Surface]): List of images for animation.
        current_index (int): Current index of image in the list of images.
        current_image (Surface): Current image of the object.
        last_updated (float): Last time the object was updated.
        
    """
    def __init__(self, pos:tuple, images:list[Surface], category:str) -> None:
        super().__init__(pos, images[0], category)
        
        self.images:list[Surface] = images
        self.current_index:int = 0
        self.current_image:Surface = self.images[self.current_index]
        self.last_updated:float = 0
        
    def reset(self) -> None:
        """Resets the last_updated to zero """
        self.last_updated = 0
        
    def next(self) -> None:
        """increment the current index by one."""
        self.current_index = (self.current_index + 1) % len(self.images)
        
    def animation(self, dt:float) -> None:
        """The base method to make sure the last_updated is calculated.

        Args:
            dt (float): Delta time in seconds.
        """
        self.last_updated += dt
        
    def update(self, dt:float) -> None:
        """base method to make sure the the animation is called.

        Args:
            dt (float): Delta time in seconds.
        """
        self.animation(dt)
        
        
class MoveableObject(Animatable):
    """The class for all animatable objects.

    This class is a base class for all animatable objects.
    
    Inherit:\n
        RenderObject
        GameObject
        Animatable
        
    Args:\n
        pos (tuple): position of the object.
        image (List[Surface]): List of images for animation.
        category (str): Category of the object for the renderer to categorise it.
        
    Attributes:\n
        image (List[Surface]): List of images for animation.
        current_index (int): Current index of image in the list of images.
        current_image (Surface): Current image of the object.
        last_updated (float): Last time the object was updated.
        
    """
    
    def __init__(self, pos:tuple, images:list[Surface], category:str) -> None:
        super().__init__(pos, images, category)
        self.is_jumping:bool = False
        self.on_ground:bool = False
        self.moving_left:bool = False
        self.gravity:float = .25
        self.friction:float = .12
        self.velocity:Vector2 = Vector2(0, 0)
        self.acceleration:Vector2 = Vector2(0, self.gravity)
        
    def update(self, dt:float) -> None:
        """base method to make sure all base updates are called.

        Args:
            dt (float): Delta time in seconds.
        """
        super().update(dt)
        self.horizontal_movement(dt)
        self.vertical_movement(dt)
        
    def horizontal_movement(self, dt: float) -> None:
        """Horizontal movement.
        
        controls the horizontal movement of the object.

        Args:
            dt (float): Delta time in seconds.
        """
        self.acceleration.x = 0
        if self.moving_left:
            self.acceleration.x -= 3
        else:
            self.acceleration.x += 3
        self.acceleration.x += self.velocity.x * self.friction
        self.velocity.x += self.acceleration.x * dt
        self.limit_velocity(4)
        self.pos.x += self.velocity * dt + (self.acceleration.x * .5) * dt**2
        self.rect.x = self.pos.x
        
    def vertical_movement(self, dt: float) -> None:
        """Vertical movement..
        
        controls the vertical movement of the object.

        Args:
            dt (float): Delta time in seconds.
        """
        self.velocity.y += self.acceleration.y * dt
        if self.velocity.y > 7:self.velocity.y = 7
        self.pos.y += self.acceleration.y * dt + (self.acceleration.y * .5) * dt**2
        if self.pos.y > 128:
            self.on_ground = True
            self.velocity.y = 0
            self.pos.y -= 128
        self.rect.bottom = self.pos.y
        
        
    def limit_velocity(self, max_vel: int) -> None:
        """limits the objects velocity.

        Args:
            max_vel (int): Max velocity it can move.
        """
        min(-max_vel, max(self.velocity.x, max_vel))
        if abs(self.velocity.x) < 0.1: self.velocity = 0
        
    def jump(self):
        """makes the object jump."""
        if self.on_ground:
            self.is_jumping = True
            self.velocity.y -= 8
            self.on_ground = False
        
        
