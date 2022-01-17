from utils.paths import SETTINGS_DIR, path_exists
from utils.serializable import read_json, json_dump

__all__ = ["save_settings", "SETTINGS"]


DEFAULT_SETTINGS: dict = {
    "NAME:": "",
    "FULLSCREEN": False,
    "FPS_TARGET": 60,
    "SIZE": (1280, 720),
}


def load_settings(path: str, default_setting: dict):
    return read_json(path) if path_exists(path) else save_settings(path, default_setting)


def save_settings(path: str, setting_obj: dict):
    return json_dump(path, setting_obj)


SETTINGS = load_settings(SETTINGS_DIR, DEFAULT_SETTINGS)
