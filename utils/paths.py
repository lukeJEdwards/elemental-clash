import os

__all__ = ["CWD", "path_exists", "SETTINGS_DIR", "assetsDirs"]


def relitive_path(*paths: list[str]) -> str:
    return os.path.join(CWD, *paths)


def path_exists(path: str) -> bool:
    return os.path.isfile(path)


CWD: str = os.getcwd()
SETTINGS_DIR: str = os.path.join("settings.json")
CHARACTER_FILES = os.path.join("data", "characters")
ASSETS = os.path.join("assets")


class assetsDirs:
    BACKGROUNDS: str = relitive_path(ASSETS, "backgrounds")
    FONTS: str = relitive_path(ASSETS, "fonts")
    ICONS: str = relitive_path(ASSETS, "icons")
    SPRITES: str = relitive_path(ASSETS, "sprites")
    TILES: str = relitive_path(ASSETS, "tiles")
    UI: str = relitive_path(ASSETS, "ui")
