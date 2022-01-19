from enum import IntEnum

from screens import MainMenuScreen, SettingsScreen, CharacterSelectionScreen, GameScreen
from systems.screen import Screen
from systems.settings import SETTINGS
from utils.constants import screenState


class stateMachine:
    def __init__(self):
        self._current_state = None
        self._previous_state = None

    def change_state(self, state: IntEnum):
        self._currentState = state

    def get_state(self) -> IntEnum:
        return self._currentState


class screenStateMachine(stateMachine):
    def __init__(self):
        super().__init__()
        self.change_state(screenState.MAIN_MENU)

        self.update: callable = lambda dt: self.apply_method("update", dt)
        self.capture_events: callable = lambda event: self.apply_method("capture", event)

    def get_state(self) -> Screen:
        return self._current_state

    def get_previous(self) -> Screen:
        return self._previous_state

    def change_state(self, state: IntEnum) -> None:
        self._previous_state = self._current_state

        if state == screenState.MAIN_MENU:
            self._current_state = MainMenuScreen(SETTINGS["SIZE"])
        elif state == screenState.SETTINGS:
            self._current_state = SettingsScreen(SETTINGS["SIZE"])
        elif state == screenState.CHARACTER_SELECTION:
            self._current_state = CharacterSelectionScreen(SETTINGS["SIZE"])
        elif state == screenState.GAME:
            self._current_state = GameScreen(SETTINGS["SIZE"])
        else:
            self._current_state = None

    def apply_method(self, method: str, *args) -> None:
        if self._current_state.render_previous:
            getattr(self._previous_state, method)(*args)
        getattr(self._current_state, method)(*args)
