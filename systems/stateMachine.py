from components.objectPools import objectPool
from systems.screen import Screen

from utils.functions import apply_method


class gameState:
    def __init__(self) -> None:
        self._started_server: bool = False
        self._connected: bool = False


class screenStateMachine:
    def __init__(self):
        self._current_state = None
        self._current_pool = objectPool()
        self._notification_pool = objectPool()

        self._previous_state: Screen = None
        self._previous_pool = objectPool()

        self.update: callable = lambda dt: self.__apply_method("update", dt)
        self.capture_events: callable = lambda event: self.__apply_method("capture_events", event)

    def __apply_method(self, method: str, *args):
        if self._current_state.render_previous:
            apply_method(self._previous_pool, method, *args)
        apply_method(self._current_pool, method, *args)
        apply_method(self._notification_pool, method, *args)

    def get_state(self) -> Screen:
        return self._current_state

    def get_previous(self) -> Screen:
        return self._previous_state

    def change_state(self, state: Screen) -> None:
        self._previous_state = self._current_state
        self._previous_pool.clear()
        self._previous_pool.update(self._current_pool)

        self._current_pool.clear()
        self._current_state = state
        self._current_state.fill_pool()


SCREEN_STATE: screenStateMachine = screenStateMachine()
GAME_STATE: gameState = gameState()
