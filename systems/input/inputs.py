from typing import Optional

__all__ = ["BaseInput", "ButtonInput", "HatInput", "AxisInput", "NavInput"]

from pygame.event import Event
from pygame.constants import JOYBUTTONDOWN, JOYBUTTONUP, JOYHATMOTION, JOYAXISMOTION

from utils import Serializable, inputType


class BaseInput:
    def __init__(self, input_type: int, **kwargs: dict):
        super().__init__(**kwargs)
        self.input_type = input_type
        self._value: float | bool = False

    def input_handler(self, event: Event) -> float | bool:
        return self._value


class ButtonInput(Serializable, BaseInput):
    def __init__(self, button: int, count: Optional[int] = 1, input_type: Optional[int] = inputType.BUTTON):
        super().__init__(input_type=input_type)
        self.button = button
        self.count = count
        self._counter = 0
        self._last_updated: float = 0

    def input_handler(self, event: Event, dt: float) -> tuple[bool, int]:
        MAX_TIME = 0.25
        self._last_updated += dt

        if self._last_updated >= MAX_TIME:
            self._last_updated = 0
            self._counter = 0

        if event.type == JOYBUTTONDOWN and event.button == self.button:
            if self._counter != self.count:
                self._counter += 1
            self._value = True if self.count == self._counter else False

        if event.type == JOYBUTTONUP and event.button == self.button:
            self._value = False

        return super().input_handler(event)


class HatInput(Serializable, BaseInput):
    def __init__(self, hat: tuple[int, int], input_type: Optional[int] = inputType.HAT):
        super().__init__(input_type=input_type)
        self.hat = hat

    def input_handler(self, event: Event) -> float | bool:
        if event.type == JOYHATMOTION:
            self._value = True if event.value == self.hat else False
        return super().input_handler(event)


class AxisInput(Serializable, BaseInput):
    def __init__(self, axis: int, is_trigger: Optional[bool] = False, input_type: Optional[int] = inputType.AXIS):
        super().__init__(input_type=input_type)
        self.axis = axis
        self.is_trigger = is_trigger

    def input_handler(self, event: Event) -> float | bool:
        DEADZONE = 0.3
        if event.type == JOYAXISMOTION and event.axis == self.axis:
            self._value = 1 if self.is_trigger else event.value if abs(event.value) > DEADZONE else 0
        return super().input_handler(event)


class NavInput(Serializable, BaseInput):
    def __init__(self, axis: int, hat: tuple[int, int], input_type: Optional[int] = inputType.NAV):
        super().__init__(input_type=input_type)
        self.axis = axis
        self.hat = hat

    def input_handler(self, event: Event) -> float | bool:
        DEADZONE = 0.3
        if event.type == JOYAXISMOTION and event.axis == self.axis:
            self._value = True if abs(event.value) > DEADZONE else False
        if event.type == JOYHATMOTION:
            self._value = True if event.value == self.hat else False
        return super().input_handler(event)
