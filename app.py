import sys
from pygame import init, display, event
from pygame.time import Clock
from pygame.constants import QUIT

from systems.settings import SETTINGS

init()
window = display.set_mode(SETTINGS["SIZE"])

from components.base import Size, textObject

from screens.MainMenu import MainMenuScreen
from screens.game import GameScreen

from systems.stateMachine import GAME_STATE
from systems.renderer import Renderer

from utils.constants import Colour
from utils.functions import get_dt
from utils.fonts import FONT_LIGHT_M


def main():
    renderer = Renderer(window)

    clock = Clock()
    fps_counter = textObject("{:.2}".format(str(clock.get_fps())), FONT_LIGHT_M, Colour.WHITE)

    dt, previous_time = 0, 0

    running = True

    GAME_STATE.change_state(MainMenuScreen)

    while running:

        clock.tick(SETTINGS["FPS_TARGET"])
        dt, previous_time = get_dt(previous_time)
        fps_counter.update("{:.2}".format(str(clock.get_fps())))

        for e in event.get():
            if e.type == QUIT:
                sys.exit()
            GAME_STATE.capture_events(e)

        GAME_STATE.update(dt)
        if GAME_STATE.game_ready:
            GAME_STATE.change_state(GameScreen)

        renderer.render()
        window.blit(*fps_counter.render(50, 50))
        display.flip()


if __name__ == "__main__":
    main()
