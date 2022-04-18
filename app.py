import sys
from pygame import init, display, event
from pygame.time import Clock
from pygame.constants import QUIT

from systems.settings import SETTINGS

init()
window = display.set_mode(SETTINGS["SIZE"])

from components.base import textObject

from screens.MainMenu import MainMenuScreen
from screens.winScreen import WinScreen

from systems.stateMachine import GAME_STATE
from systems.renderer import Renderer

from utils.constants import Colour, characterState
from utils.functions import get_dt
from utils.fonts import FONT_LIGHT_M


def check_left_collision(player_index, other_player):
    return (GAME_STATE.players[player_index].collision_box.left > GAME_STATE.players[other_player].collision_box.centerx + 10 or
        GAME_STATE.players[player_index].collision_box.left < GAME_STATE.players[other_player].collision_box.centerx - 10) and GAME_STATE.players[player_index].state == characterState.AKT and GAME_STATE.players[other_player].state != characterState.DEFEND

def check_right_collision(player_index, other_player):
    return (GAME_STATE.players[player_index].collision_box.right > GAME_STATE.players[other_player].collision_box.centerx + 10 or
        GAME_STATE.players[player_index].collision_box.right < GAME_STATE.players[other_player].collision_box.centerx - 10) and GAME_STATE.players[player_index].state == characterState.AKT and GAME_STATE.players[other_player].state != characterState.DEFEND



def main():
    # renders the screen
    renderer = Renderer(window)

    # keeps the game running at 60fps as best as possible
    clock = Clock()
    fps_counter = textObject("{:.2}".format(str(clock.get_fps())), FONT_LIGHT_M, Colour.WHITE)

    # if game can't run at 60fps helps with keeping consistant physics
    dt, previous_time = 0, 0
    
    atk_timers = [0, 0]
    atk_calldown = 0.1

    running = True

    GAME_STATE.change_state(MainMenuScreen)

    while running:

        # set fps at 60
        clock.tick(SETTINGS["FPS_TARGET"])
        # finds new delta time for game 
        dt, previous_time = get_dt(previous_time)
        fps_counter.update("{:.2}".format(str(clock.get_fps())))

        for e in event.get():
            if e.type == QUIT:
                sys.exit()
            # send event to objects on screen
            GAME_STATE.capture_events(e)

        # updates objects on the screen
        GAME_STATE.update(dt)

        if GAME_STATE.game_start:

            atk_timers[0] += dt
            atk_timers[1] += dt

            print(atk_timers)

            if check_left_collision(0, 1) and atk_timers[0] > atk_calldown:
                GAME_STATE.players[0].hit_count += 1
                atk_timers[0] = 0
            elif check_left_collision(1, 0) and atk_timers[1] > atk_calldown:
                GAME_STATE.players[1].hit_count += 1
                atk_timers[1] = 0
            elif check_left_collision(0, 1) and atk_timers[0] > atk_calldown:
                GAME_STATE.players[0].hit_count += 1
                atk_timers[0] = 0
            elif check_left_collision(1, 0) and atk_timers[1] > atk_calldown:
                GAME_STATE.players[1].hit_count += 1
                atk_timers[1] = 0


            if GAME_STATE.players[0].state == characterState.AKT:
                atk_timers[0] = 0
            
            if GAME_STATE.players[1].state == characterState.AKT:
                atk_timers[1] = 0

            if any(map(lambda player: player.hit_count == 5, GAME_STATE.players)):
                GAME_STATE.change_state(WinScreen)

        # renders the objects on screen
        renderer.render()
        window.blit(*fps_counter.render(50, 50))
        display.flip()


if __name__ == "__main__":
    main()
