from enum import Enum, IntEnum

__all__ = [ 'ORIGIN', 'settingsType', 'inputType', 'ControllerHat', 'ControllerButton', 'ControllerAxis']


ORIGIN:tuple = (0, 0)
    
class settingsType(IntEnum):
    VIDEO = 0
    AUDIO = 1
    KEY_MAPPING = 2
    
class inputType(IntEnum):
    KEYBOARD = 0
    BUTTON = 1
    AXIS = 2
    HAT = 3
    NAV = 4
    
class ControllerButton(IntEnum):
    A = 0
    B = 1
    X = 2
    Y = 3
    LB = 4
    RB = 5
    MENU = 6
    START = 7
    L_STICK = 8
    R_STICK = 9
    
class ControllerHat:
    HAT_UP = (0, 1)
    HAT_DOWN = (0, -1)
    HAT_RIGHT = (1, 0)
    HAT_LEFT = (-1, 0)
    HAT_NONE = (0, 0)
    
class ControllerAxis(IntEnum):
    L_STICK_X = 0
    L_STICK_Y = 1
    R_STICK_X = 2
    R_STICK_Y = 3
    L_TRIGGER = 4
    R_TRIGGER = 5
