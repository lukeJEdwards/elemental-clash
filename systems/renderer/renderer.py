from pygame import Surface
from systems.renderer.screen import Screen
from utils import ORIGIN

__all__ = ['Renderer']

class Renderer:
    def __init__(self, display:Surface, inital_screen:Screen) -> None:
        self.display:Surface = display
        self.render_stack:list[Screen] = []
        self.render_stack.append(inital_screen)
        
    
    def push_screen(self, screen:Screen) -> None: 
        assert isinstance(screen, Screen)
        self.render_stack.append(screen)
        
    def get_top(self) -> Screen: return self.render_stack[-1]
    
    def get_prevoius_screen(self) -> Screen: return self.render_stack[-2]
    
    def render(self) -> None:
        self.display.fill((255, 255, 255))
        top_screen = self.get_top()
        top_screen_render = top_screen.render()
        if top_screen.overlay:
            previous_screen = self.get_prevoius_screen().render()
            self.display.blit(previous_screen, ORIGIN)
        self.display.blit(top_screen_render, ORIGIN)
    
        
        
        
        
        
        