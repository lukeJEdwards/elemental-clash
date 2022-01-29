from components.objectPools import objectPool
from systems.screen import Screen

from utils.functions import apply_method


class stateMachine:
    def __init__(self):
        self._current_state: Screen = None
        self._previous_state: Screen = None
        self._previous_pool = objectPool()
        self._current_pool = objectPool()

    def change_state(self, state: Screen):
        self._currentState = state

    def get_state(self) -> Screen:
        return self._currentState


class screenStateMachine(stateMachine):
    def __init__(self):
        super().__init__()

        self.update: callable = lambda dt: self.__apply_method("update", dt)
        self.capture_events: callable = lambda event: self.__apply_method("capture_events", event)

    def __apply_method(self, method: str, *args):
        if self._current_state.render_previous:
            apply_method(self._previous_pool, method, *args)
        apply_method(self._current_pool, method, *args)

    def get_state(self) -> Screen:
        return self._current_state

    def get_previous(self) -> Screen:
        return self._previous_state

    def change_state(self, state: Screen) -> None:
        self._previous_state = self._current_state
        self._previous_pool.clear()
        self._previous_pool.update(self._current_pool)

        self._current_state = state


SCREEN_STATE: screenStateMachine = screenStateMachine()
