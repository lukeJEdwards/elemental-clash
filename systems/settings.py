
__all__ = ['save_settings', 'KEY_MAPPING', 'VIDEO_SETTINGS']

from utils import inputType, settingsDirs, path_exists, read_json, json_dump, ControllerButton, ControllerHat, ControllerAxis
from systems.input import BaseInput, ButtonInput, HatInput, AxisInput, NavInput

DEFAULT_VIDEO_SETTINGS: dict[str, bool | int | tuple[int, int]] = {
    "FULLSCREEN": False,
    "FPS_TARGET": 60,
    "SIZE": (1280, 720),
}

DEFAULT_KEY_MAPPING: dict[str, BaseInput] = {
    "ATK_1": ButtonInput(ControllerButton.X),
    "ATK_2": ButtonInput(ControllerButton.X, 2),
    "ATK_3": ButtonInput(ControllerButton.Y),
    "ATK_SP": HatInput(ControllerHat.HAT_RIGHT),
    "DEFEND": AxisInput(ControllerAxis.L_TRIGGER, True),
    "HEAL": HatInput(ControllerHat.HAT_UP),
    "JUMP": ButtonInput(ControllerButton.A),
    "MOVE_LEFT": AxisInput(ControllerAxis.L_STICK_X),
    "MOVE_RIGHT": AxisInput(ControllerAxis.L_STICK_X),
    "ROLL": ButtonInput(ControllerButton.B),
    "RUN": AxisInput(ControllerAxis.R_TRIGGER, True),
    "UP": NavInput(ControllerAxis.L_STICK_Y, ControllerHat.HAT_UP),
    "DOWN": NavInput(ControllerAxis.L_STICK_Y, ControllerHat.HAT_DOWN),
    "RIGHT": NavInput(ControllerAxis.L_STICK_X, ControllerHat.HAT_RIGHT),
    "LEFT": NavInput(ControllerAxis.L_STICK_X, ControllerHat.HAT_LEFT),
}


def load_settings(path:str, default_setting:dict): return read_json(path) if path_exists(path) else save_settings(path, default_setting)
def save_settings(path:str, setting_obj:dict): return json_dump(path, setting_obj)

def to_input_object(obj:dict) -> BaseInput:
    match inputType(obj['input_type']):
        case inputType.BUTTON: return ButtonInput(**obj)
        case inputType.HAT: return HatInput(**obj)
        case inputType.AXIS: return AxisInput(**obj)
        case inputType.NAV: return NavInput(**obj)

KEY_MAPPING = {key: to_input_object(value) for key, value in load_settings(settingsDirs.KEY_MAPPING, DEFAULT_KEY_MAPPING).items()}
VIDEO_SETTINGS = load_settings(settingsDirs.VIDEO, DEFAULT_VIDEO_SETTINGS)