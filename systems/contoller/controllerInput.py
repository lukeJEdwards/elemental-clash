from typing import Optional
from pygame.constants import KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP, JOYAXISMOTION, JOYBUTTONDOWN, JOYBUTTONUP, JOYHATMOTION
from pygame.event import Event

from utils import Serializable, ControllerHat, inputType

__all__ = ['BaseInput', 'KeyboardInput', 'ButtonInput', 'AxisInput', 'HatInput', 'ControllerNavInput']

class BaseInput:
    def __init__(self, input_type:int, **kwargs:dict) -> None:
        super().__init__(**kwargs)
        self.type = input_type
        self._value:int|bool = False
    
class KeyboardInput(BaseInput, Serializable):
    def __init__(self, key, type=inputType.KEYBOARD):
        super().__init__(input_type=type)
        self.key:int = key
    
    def input_handler(self, event:Event) -> None:
        if event.type == KEYDOWN:
            if self.key == event.key:self._value = True
        if event.type == KEYUP:
            if self.key == event.key:self._value = False
        
    
class ButtonInput(BaseInput, Serializable):
    def __init__(self, button, count=1, type=inputType.BUTTON) -> None:
        super().__init__(input_type=type)
        self.button:int = button
        self.count:int = count
        
    def input_handler(self, event:Event) -> None:
        event_types = [MOUSEBUTTONDOWN, JOYBUTTONDOWN]
        if event.type in event_types:
            if event.button == self.button: self._value = True
            
        event_types = [MOUSEBUTTONUP, JOYBUTTONUP]
        if event.type in event_types:
            if event.button == self.button: self._value = False
                
                    
class AxisInput(BaseInput, Serializable):
    def __init__(self, axis, is_toggle:Optional[bool]=False, type=inputType.AXIS) -> None:
        super().__init__(input_type=type)
        self.axis:int = axis
        self.is_toggle:bool = is_toggle
        
    def input_handler(self, event:Event) -> float:
        deadzone = 0.3
        if event.type == JOYAXISMOTION:
            if event.axis == self.axis:
                if self.is_toggle:
                    if  event.value > deadzone - 1:self._value = 1
                    else: self._value = 0
                else:
                    if abs(event.value) > deadzone: self._value = event.value
                    else: self._value = 0
                    
                    
class HatInput(BaseInput, Serializable):
    def __init__(self, button, type=inputType.HAT) -> None:
        super().__init__(input_type=type)
        self.button = button
        
    def input_handler(self, event:Event) -> None:
        if event.type == JOYHATMOTION:
            if event.value == self.button: self._value = True
            if event.value == ControllerHat.HAT_NONE: self._value = False
                         
                         
class ControllerNavInput(BaseInput, Serializable):
    def __init__(self, axis, hat, type=inputType.NAV) -> None:
        super().__init__(input_type=type)
        self.axis = axis
        self.hat = hat
        
    def input_handler(self, event:Event) -> None:
        if event.type == JOYHATMOTION:
            if event.value == self.hat: self._value = True
            if event.value == ControllerHat.HAT_NONE: self._value = False
        if event.type == JOYAXISMOTION:
            deadzone = 0.3
            if event.axis == self.axis:
                    if  abs(event.value) > deadzone: self._value = True
                    else: self._value = False
            