from pygame import Surface

from systems.settings import SETTINGS
from systems.stateMachine import SCREEN_STATE
from utils.functions import apply_method


class Renderer:
    def __init__(self, window: Surface) -> None:
        self._window: Surface = window
        self._size: tuple[int, int] = SETTINGS["SIZE"]

    def render(self) -> None:
        current_screen = SCREEN_STATE.get_state()
        if current_screen.render_previous:
            previous_screen = SCREEN_STATE.get_previous()
            self._window.blit(previous_screen.render(), previous_screen.pos)

            apply_method(SCREEN_STATE._previous_pool, "render", self._window)

        self._window.blit(current_screen.render(), current_screen.pos)
        apply_method(SCREEN_STATE._current_pool, "render", self._window)
