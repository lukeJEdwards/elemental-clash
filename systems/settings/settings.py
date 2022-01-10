
__all__ = ['save_settings', 'KEY_MAPPING', 'VIDEO_SETTINGS']

from utils import inputType, settingsDirs, path_exists, read_json, json_dump
from systems.input import BaseInput, ButtonInput, HatInput, AxisInput, NavInput
from systems.settings.defaultSettings import DEFAULT_KEY_MAPPING, DEFAULT_VIDEO_SETTINGS


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