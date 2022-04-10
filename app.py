import sys
from pygame import init, display, event
from pygame.time import Clock
from pygame.constants import QUIT

from systems.settings import SETTINGS

init()
window = display.set_mode(SETTINGS["SIZE"].to_tuple())

from screens.mainMenu import MainMenu
from systems.gameState import GAMESTATE
from utils.functions import get_dt


def main():
    clock = Clock()
    dt, previous_time = 0, 0
    running = True

    while running:
        clock.tick(SETTINGS["FPS_TARGET"])
        dt, previous_time = get_dt(previous_time)

        for e in event.get():
            if e.type == QUIT:
                sys.exit()
            GAMESTATE.capture_event(e)

        GAMESTATE.update(dt)



        GAMESTATE.render(window)
        display.flip()

        running = GAMESTATE.check_state()


if __name__ == "__main__":
    main()
