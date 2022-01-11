__all__ = ["CWD", "path_exists", "settingsDirs", "assetsDirs"]

import os


def relitive_path(*paths: list[str]) -> str:
    return os.path.join(CWD, *paths)


def path_exists(path: str) -> bool:
    return os.path.isfile(path)


CWD: str = os.getcwd()
SETTINGS_FILES = os.path.join("data", "settings")
CHARACTER_FILES = os.path.join("data", "characters")
ASSETS = os.path.join("assets")


class settingsDirs:
    VIDEO: str = relitive_path(SETTINGS_FILES, "video_settings.json")
    AUDIO: str = relitive_path(SETTINGS_FILES, "audio_settings.json")
    KEY_MAPPING: str = relitive_path(SETTINGS_FILES, "key_mapping.json")


class uiDirs:
    BARS: str = relitive_path(ASSETS, "ui", "bars")
    BORDERS: str = relitive_path(ASSETS, "ui", "borders")
    BUTTONS: str = relitive_path(ASSETS, "ui", "buttons")
    PLAYER_INPUTS: str = relitive_path(ASSETS, "ui", "player-inputs")


class assetsDirs:
    BACKGROUNDS: str = relitive_path(ASSETS, "backgrounds")
    FONTS: str = relitive_path(ASSETS, "fonts")
    ICONS: str = relitive_path(ASSETS, "icons")
    SPRITES: str = relitive_path(ASSETS, "sprites")
    TILES: str = relitive_path(ASSETS, "tiles")
    UI: uiDirs = uiDirs
