import sys
from pygame import init, display, event
from pygame.time import Clock
from pygame.constants import QUIT

from systems.settings import SETTINGS

init()
window = display.set_mode(SETTINGS["SIZE"])


from utils.constants import WHITE, characterType
from utils.functions import get_dt, render_text
from utils.fonts import FONT_LIGHT_M

from systems.stateMachine import SCREEN_STATE
from systems.renderer import Renderer
from screens import MainMenuScreen


if __name__ == "__main__":
    renderer = Renderer(window)
    clock = Clock()

    dt, previous_time = 0, 0

    running = True

    SCREEN_STATE.change_state(MainMenuScreen(SETTINGS["SIZE"]))

    while running:

        clock.tick(SETTINGS["FPS_TARGET"])
        dt, previous_time = get_dt(previous_time)

        for e in event.get():
            if e.type == QUIT:
                sys.exit()
            SCREEN_STATE.capture_events(e)

        SCREEN_STATE.update(dt)

        renderer.render()
        render_text(FONT_LIGHT_M, "{:.2}".format(str(clock.get_fps())), WHITE, (50, 50), window)
        display.flip()
