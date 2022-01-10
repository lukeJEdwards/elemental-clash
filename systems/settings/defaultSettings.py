
__all__ = ['DEFAULT_VIDEO_SETTINGS', 'DEFAULT_KEY_MAPPING']

from utils import ControllerButton, ControllerHat, ControllerAxis
from systems.input import BaseInput, ButtonInput, HatInput, AxisInput, NavInput


DEFAULT_VIDEO_SETTINGS:dict[str, bool|int|tuple[int, int]] = {
    "FULLSCREEN":False,
    "FPS_TARGET":60,
    "SIZE":(1280, 720)
}

DEFAULT_KEY_MAPPING:dict[str, BaseInput] = {
    "ATK_1": ButtonInput(ControllerButton.X),
    "ATK_2": ButtonInput(ControllerButton.X, 2),
    "ATK_3": ButtonInput(ControllerButton.Y),
    "ATK_SP": HatInput(ControllerHat.HAT_RIGHT),
    "DEFEND": AxisInput(ControllerAxis.L_TRIGGER, True),
    "HEAL": HatInput(ControllerHat.HAT_UP),
    "JUMP": ButtonInput(ControllerButton.A),
    "LEFT": AxisInput(ControllerAxis.L_STICK_X),
    "RIGHT": AxisInput(ControllerAxis.L_STICK_X),
    "ROLL": ButtonInput(ControllerButton.B),
    "RUN": AxisInput(ControllerAxis.R_TRIGGER, True),
    "UP": NavInput(ControllerAxis.L_STICK_Y, ControllerHat.HAT_UP),
    "DOWN": NavInput(ControllerAxis.L_STICK_Y, ControllerHat.HAT_DOWN),
    "RIGHT": NavInput(ControllerAxis.L_STICK_X, ControllerHat.HAT_RIGHT),
    "LEFT": NavInput(ControllerAxis.L_STICK_X, ControllerHat.HAT_LEFT)
}