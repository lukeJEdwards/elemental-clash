import sys
from pygame import init, display, event
from pygame.time import Clock
from pygame.constants import QUIT

from systems.settings import SETTINGS

init()
window = display.set_mode(SETTINGS["SIZE"])

from systems.stateMachine import screenStateMachine
from systems.renderer import Renderer

from utils.constants import WHITE
from utils.functions import get_dt, render_text
from utils.fonts import FONT_LIGHT_M


if __name__ == "__main__":
    screen_state = screenStateMachine()
    renderer = Renderer(window, screen_state)
    clock = Clock()

    dt, previous_time = 0, 0

    running = True

    while running:

        clock.tick(SETTINGS["FPS_TARGET"])
        dt, previous_time = get_dt(previous_time)

        for e in event.get():
            if e.type == QUIT:
                sys.exit()
            screen_state.capture_events(e)

        screen_state.update(dt)

        renderer.render()
        render_text(FONT_LIGHT_M, "{:.2}".format(str(clock.get_fps())), WHITE, (50, 50), window)
        display.flip()
