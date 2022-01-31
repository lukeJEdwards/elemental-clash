from components.objectPools import objectPool
from systems.screen import Screen
from systems.settings import SETTINGS
from utils.constants import characterType

from utils.functions import apply_method


class gameState:
    def __init__(self) -> None:
        self._server_running: bool = False
        self._connected: bool = False

        self._player_data: dict = {
            "1": {
                "name": SETTINGS["NAME"],
                "character": characterType.NONE,
                "ready": False,
                "health": 100,
            },
            "2": {
                "name": "",
                "character": characterType.NONE,
                "ready": False,
                "health": 100,
            },
        }


class screenStateMachine:
    def __init__(self):
        self._state_stack: list[Screen] = []
        self._current_pool = objectPool()
        self._previous_pool = objectPool()
        self._notification_pool = objectPool()

        self.update: callable = lambda dt: self.__apply_method("update", dt)
        self.capture_events: callable = lambda event: self.__apply_method("capture_events", event)

    def __apply_method(self, method: str, *args):
        if self._state_stack[-1].render_previous:
            apply_method(self._state_stack[-2], method, *args)
        apply_method(self._current_pool, method, *args)
        apply_method(self._notification_pool, method, *args)

    def get_state(self) -> Screen:
        return self._state_stack[-1]

    def get_previous(self) -> Screen:
        return self._state_stack[-2]

    def back(self) -> None:
        self._state_stack.pop()
        self._current_pool.clear()
        self._current_pool.append(self._state_stack[-1].fill_pool())
        if len(self._state_stack) > 1:
            self._previous_pool.update(self._state_stack[-2].fill_pool())

    def change_state(self, state: Screen) -> None:
        self._previous_pool.update(self._current_pool)
        self._state_stack.append(state)
        self._current_pool.clear()
        self._current_pool.append(self._state_stack[-1].fill_pool())


SCREEN_STATE: screenStateMachine = screenStateMachine()
GAME_STATE: gameState = gameState()
