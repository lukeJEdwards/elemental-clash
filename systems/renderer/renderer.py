
__all__ = ['Renderer', 'render_text']

from typing import Optional
from pygame import Surface
from pygame.font import Font

from utils import ORIGIN
from systems.renderer.screen import Screen

def render_text(context:Surface, font:Font, text:str, colour:tuple[int, int, int], pos:tuple[int, int]):
    text_surface = font.render(text, True, colour)
    text_rect = text_surface.get_rect()
    text_rect.center = pos
    context.blit(text_surface, text_rect)

class Renderer:
    def __init__(self, display:Surface, inital_screen:Screen) -> None:
        self.display = display
        self.render_stack:list[Screen] = []
        self.render_stack.append(inital_screen)
        
    def append(self, screen:Screen) -> None: self.render_stack.append(screen)
    def pop(self, index:Optional[int]=None) -> Screen: return self.render_stack.pop(index) if index else self.render_stack.pop()
    
    def get_top_screen(self) -> Screen: return self.render_stack[-1]
    def get_previous_screen(self) -> Screen: return self.render_stack[-2]
    
    def render(self) -> None:
        self.display.fill((255, 255, 255))
        top_screen = self.get_top_screen()
        if top_screen.render_prev_screen:
            prev_screen = self.get_previous_screen()
            self.display.blit(prev_screen.render(), ORIGIN)
        self.display.blit(top_screen.render(), ORIGIN)