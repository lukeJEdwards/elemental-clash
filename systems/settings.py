__all__ = ["save_settings", "KEY_MAPPING", "VIDEO_SETTINGS"]

from utils.paths import settingsDirs, path_exists
from utils.serializable import read_json, json_dump

DEFAULT_VIDEO_SETTINGS: dict[str, bool | int | tuple[int, int]] = {
    "FULLSCREEN": False,
    "FPS_TARGET": 60,
    "SIZE": (1280, 720),
}


def load_settings(path: str, default_setting: dict):
    return read_json(path) if path_exists(path) else save_settings(path, default_setting)


def save_settings(path: str, setting_obj: dict):
    return json_dump(path, setting_obj)


VIDEO_SETTINGS = load_settings(settingsDirs.VIDEO, DEFAULT_VIDEO_SETTINGS)
