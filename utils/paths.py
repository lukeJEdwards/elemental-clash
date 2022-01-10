from os import getcwd, path

__all__ = ['CWD', 'settingsDirs', 'characterDirs', 'assetsDirs']

def relitive_path(*paths:list[str]) -> str:  return path.join(CWD, *paths)

CWD:str = getcwd()
SETTINGS_FILES = path.join('data', 'settings')
CHARACTER_FILES = path.join('data', 'characters')
ASSETS = path.join('assets')


class settingsDirs:
    VIDEO:str = relitive_path(SETTINGS_FILES, 'video_settings.json')
    AUDIO:str = relitive_path(SETTINGS_FILES, 'audio_settings.json')
    KEY_MAPPING:str = relitive_path(SETTINGS_FILES, 'key_mapping.json')

class characterDirs:
    pass

class uiDirs:
    BUTTONS:str = relitive_path(ASSETS, 'ui', 'buttons')
    CARDS:str = relitive_path(ASSETS, 'ui', 'cards')
    GUI:str = relitive_path(ASSETS, 'ui', 'gui')
    LEVELS:str = relitive_path(ASSETS, 'ui', 'levels')
    PLAYER_INPUTS:str = relitive_path(ASSETS, 'ui', 'player_inputs')
    SLIDERS:str = relitive_path(ASSETS, 'ui', 'sliders')

class assetsDirs:
    FONTS:str = relitive_path(ASSETS, 'fonts')
    BACKGROUNDS:str = relitive_path(ASSETS, 'backgrounds')
    UI:uiDirs = uiDirs
    TILES:str = relitive_path(ASSETS, 'tiles')
    SPRITES:str = relitive_path(ASSETS, 'sprites')
    ICONS:str = relitive_path(ASSETS, 'icons')
    
