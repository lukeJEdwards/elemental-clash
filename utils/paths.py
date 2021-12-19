from os import getcwd, path

__all__ = ['CWD', 'settingsDirs', 'characterDirs', 'assetsDirs', 'relitive_path']

def relitive_path(*paths:list[str]) -> str: 
    """create relative path to this directory.

    Returns:
        str: The path.
    """
    return path.join(CWD, *paths)

CWD:str = getcwd()
SETTINGS_FILES = relitive_path('data', 'settings')
CHARACTER_FILES = relitive_path('data', 'characters')
ASSETS = relitive_path('assets')


class settingsDirs:
    VIDEO:str = path.join(SETTINGS_FILES, 'video_settings.json')
    AUDIO:str = path.join(SETTINGS_FILES, 'audio_settings.json')
    KEY_MAPPING:str = path.join(SETTINGS_FILES, 'key_mapping.json')

class characterDirs:
    pass

class assetsDirs:
    FONTS:str = path.join(ASSETS, 'fonts')
    BACKGROUNDS:str = path.join(ASSETS, 'backgrounds')
    UI:str = path.join(ASSETS, 'ui')
    TILES:str = path.join(ASSETS, 'tiles')
    SPRITES:str = path.join(ASSETS, 'sprites')
    ICONS:str = path.join(ASSETS, 'icons')
    
