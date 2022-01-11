import sys
from pygame import init, Surface, display, event, joystick
from pygame.time import Clock
from pygame.constants import QUIT, FULLSCREEN

from systems.settings import VIDEO_SETTINGS, KEY_MAPPING

init()
joystick.init()
window: Surface = (
    display.set_mode(VIDEO_SETTINGS["SIZE"], FULLSCREEN)
    if VIDEO_SETTINGS["FULLSCREEN"]
    else display.set_mode(VIDEO_SETTINGS["SIZE"])
)

from utils import get_dt, render_text, FONT_NORMAL_M, WHITE
from systems.renderer import Renderer
from systems.input import Controller

if __name__ == "__main__":
    controller = Controller(KEY_MAPPING)
    renderer, clock = Renderer(window, controller), Clock()

    running = True
    previous_time, dt = 0, 0

    while running:

        clock.tick(VIDEO_SETTINGS["FPS_TARGET"])
        dt, previous_time = get_dt(previous_time)
        joysticks = [joystick.Joystick(x) for x in range(joystick.get_count())]

        for e in event.get():
            if e.type == QUIT:
                sys.exit()
            controller.update(e, dt)

        renderer.update(dt)
        renderer.render()
        render_text(window, FONT_NORMAL_M, "{:.2}".format(str(clock.get_fps())), WHITE, (50, 50))
        display.flip()
