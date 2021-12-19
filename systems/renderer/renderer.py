from pygame import Surface
from systems.renderer.screen import Screen
from utils import ORIGIN

__all__ = ['Renderer']

class Renderer:
    """Renderer for the game.
    
    The class is responsible for the order of rendering. This is done by rendering each object in the object pool from 
    the top object in the sack, being background, game objects and then the GUI objects. The consents above are used 
    for this purpose.
    
    Args:\n
        display (Surface): The surface the method pygame.display.set_mode() returns.
    
    Attributes:\n
        display (Surface): Is the main surface for the rendering.
        render_stack (list[Screen]): A stack for the order of screens that need to be rendered.
        
    """
    def __init__(self, display:Surface, inital_screen:Screen) -> None:
        self.display:Surface = display
        self.render_stack:list[Screen] = []
        self.render_stack.append(inital_screen)
        
    
    def push_screen(self, screen:Screen) -> None:
        """push a screen into the stack.

        Args:
            screen (Screen): The screen that needs to be pushed onto the stack.
        """
        assert isinstance(screen, Screen)
        self.render_stack.append(screen)
        
    def get_top(self) -> Screen:
        """Returns the top screen in the stack.

        Returns:
            Screen: The top screen in the stack.
        """
        return self.render_stack[-1]
    
    def get_prevoius_screen(self) -> Screen:
        """Returns the previous screen if needed.

        Returns:
            Screen: [description]
        """
        return self.render_stack[-2]
    
    def render(self) -> None:
        """Renders the screen.
        
        Renders the current screen, if necessary the previous screen as well. That is determined by the overlay 
        attribute in the screen object.
        """
        self.display.fill((255, 255, 255))
        top_screen = self.get_top()
        top_screen_render = top_screen.render()
        if top_screen.overlay:
            previous_screen = self.get_prevoius_screen().render()
            self.display.blit(previous_screen, ORIGIN)
        self.display.blit(top_screen_render, ORIGIN)
    
        
        
        
        
        
        