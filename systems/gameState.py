
from dataclasses import dataclass, field
from hashlib import new

from pygame import Surface
from pygame.event import Event

from components.objectPool import ObjectPool

from screens.screen import Screen
from screens.mainMenu import MainMenu

from systems.settings import SETTINGS

from utils.constants import ORIGIN, SCREEN, TAG


@dataclass
class GameState:

    def __init__(self) -> None:
        self.screen_stack: list[Screen] = [MainMenu(SETTINGS['SIZE'])]
        self.obj_pool: ObjectPool = ObjectPool()

        self.prev_state: SCREEN = None
        self.currrent_state:SCREEN = SCREEN.MENU

        self.obj_pool.set_objs(self.current_screen.load_pool())


    @property
    def current_screen(self) -> Screen:
        return self.screen_stack[self.currrent_state.value]

    def check_state(self) -> bool:
        new_tag = self.current_screen.switch_screen

        if new_tag == SCREEN.CLOSE:
            return False

        if self.currrent_state != new_tag:

            self.prev_state = self.currrent_state
            self.currrent_state = new_tag

            self.obj_pool.set_objs(self.current_screen.load_pool())

        return True

          



    def capture_event(self, event:Event) -> None:
        pass

    def update(self, dt:float) -> None:
        pass

    def render(self, window:Surface) -> None:
        window.blit(self.current_screen.background.value, ORIGIN)
        
        for tag in TAG:
            for id in self.obj_pool.render_order[tag]:
                obj = self.obj_pool[id]
                obj.render(window)
    

GAMESTATE: GameState = GameState()