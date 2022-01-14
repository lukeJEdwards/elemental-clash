import sys
from pygame import init, Surface, display, event, joystick
from pygame.time import Clock
from pygame.constants import QUIT, FULLSCREEN

from systems.settings import SETTINGS

init()
joystick.init()
window: Surface = (
    display.set_mode(SETTINGS["SIZE"], FULLSCREEN) if SETTINGS["FULLSCREEN"] else display.set_mode(SETTINGS["SIZE"])
)

from utils.functions import get_dt, render_text
from utils.fonts import FONT_NORMAL_M
from utils.constants import WHITE
from systems.renderer import Renderer

if __name__ == "__main__":
    renderer, clock = Renderer(window), Clock()

    running = True
    previous_time, dt = 0, 0

    while running:

        clock.tick(SETTINGS["FPS_TARGET"])
        dt, previous_time = get_dt(previous_time)
        joysticks = [joystick.Joystick(x) for x in range(joystick.get_count())]

        for e in event.get():
            if e.type == QUIT:
                sys.exit()
            renderer.capture_events(e)

        renderer.update(dt)
        renderer.render()

        render_text(window, FONT_NORMAL_M, "{:.2}".format(str(clock.get_fps())), WHITE, (50, 50))
        display.flip()
