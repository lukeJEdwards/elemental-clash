
__all__ = ['ORIGIN', 'BLACK', 'WHITE', 'inputType','ControllerButton', 'ControllerAxis', 'ControllerHat']

from enum import IntEnum

ORIGIN:tuple[int, int] = (0, 0)
BLACK:tuple[int, int, int] = (0, 0, 0)
WHITE:tuple[int, int, int] = (255, 255, 255)

class inputType(IntEnum):
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
    
class ControllerAxis(IntEnum):
    L_STICK_X = 0
    L_STICK_Y = 1
    R_STICK_X = 2
    R_STICK_Y = 3
    L_TRIGGER = 4
    R_TRIGGER = 5
    
class ControllerHat:
    HAT_UP = (0, 1)
    HAT_DOWN = (0, -1)
    HAT_RIGHT = (1, 0)
    HAT_LEFT = (-1, 0)
    HAT_NONE = (0, 0)
    