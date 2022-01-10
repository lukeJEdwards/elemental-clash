from pygame import init, Surface, display, event, joystick
from pygame.time import Clock
from pygame.constants import QUIT
from sys import exit

from systems.settings import Settings

init()
settings = Settings()
window:Surface = display.set_mode(settings.video_settings['SIZE'])

from systems.contoller import ControllerEvents
from systems.renderer import Renderer
from screens import TitleScreen
from utils.functions import get_dt


def setup() -> tuple[Clock, Renderer, TitleScreen]:
    joystick.init()
    title_screen:TitleScreen = TitleScreen(settings.video_settings['SIZE'])
    renderer:Renderer = Renderer(window, title_screen)
    return Clock(), renderer, title_screen


if __name__ == '__main__':
    control_input = ControllerEvents(settings.key_mapping)
    clock, renderer, title_screen = setup()
    prev_time = 0
    running = True
    
    while running:
        clock.tick(settings.video_settings['FPS_TARGET'])
        joysticks = [joystick.Joystick(x) for x in range(joystick.get_count())]
        for e in event.get():
            if e.type == QUIT: exit()
            
            control_input.update(e)
            
        dt, prev_time = get_dt(prev_time)
        title_screen.update(control_input.actions, dt)
        renderer.render()
        display.flip()
            
    