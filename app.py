from pygame import init, Surface, display, event
from pygame.constants import MOUSEBUTTONDOWN, QUIT
from sys import exit

from systems.settings import Settings

init()
settings = Settings()
SIZE = (settings.video_settings['SIZE']['WIDTH'], settings.video_settings['SIZE']['HEIGHT'])
window:Surface = display.set_mode(SIZE)

from systems.renderer import Renderer
from screens import TitleScreen


def setup() -> tuple[Renderer, TitleScreen]:
    title_screen = TitleScreen(SIZE)
    renderer:Renderer = Renderer(window, title_screen)
    return renderer, title_screen


if __name__ == '__main__':
    renderer, title_screen = setup()
    running = True
    
    while running:
        for e in event.get():
            if e.type == QUIT: exit()
            if e.type == MOUSEBUTTONDOWN:
                print(e)
            
        renderer.render()
        display.flip()
            
    