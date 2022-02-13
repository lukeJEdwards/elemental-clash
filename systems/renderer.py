from pygame import Surface

from systems.stateMachine import GAME_STATE

from utils.constants import ORIGIN
from utils.functions import apply_method


class Renderer:
    def __init__(self, window: Surface) -> None:
        self.window: Surface = window

    def render(self) -> None:
        current_screen = GAME_STATE.get_top()

        self.window.blit(current_screen.background.value, ORIGIN)
        apply_method(GAME_STATE.obj_pool, "render", self.window)
        apply_method(GAME_STATE.notification_pool, "render", self.window)
