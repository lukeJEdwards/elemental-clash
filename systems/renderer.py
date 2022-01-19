from pygame import Surface

from systems.settings import SETTINGS
from systems.stateMachine import screenStateMachine


class Renderer:
    def __init__(self, window: Surface, screenState: screenStateMachine) -> None:
        self._window: Surface = window
        self._screenState: screenStateMachine = screenState
        self._size: tuple[int, int] = SETTINGS["SIZE"]

    def render(self) -> None:
        current_screen = self._screenState.get_state()
        if current_screen.render_previous:
            previous_screen = self._screenState.get_previous()
            self._window.blit(previous_screen.render(), previous_screen.pos)
        self._window.blit(current_screen.render(), current_screen.pos)
