from os import path

from utils import settingsType, json_file_handler, settingsDirs
from systems.settings.defaultSettings import AUDIO_SETTINGS, VIDEO_SETTINGS, KEY_MAPPING


__all__ = ['Settings']

class Settings:
    def __init__(self) -> None:
        self.video_settings:dict = self.load_setting(settingsDirs.VIDEO, VIDEO_SETTINGS)
        self.audio_settings:dict = self.load_setting(settingsDirs.AUDIO, AUDIO_SETTINGS)
        self.key_mapping:dict = self.load_setting(settingsDirs.KEY_MAPPING, KEY_MAPPING)
        
    def load_setting(self, file_path:str, default_values:dict) -> dict:
        if path.exists(file_path): return json_file_handler(file_path)
        else: return json_file_handler(file_path, default_values)
        
    def save_setting(self, enum:settingsType) -> dict:
        match enum:
            case settingsType.VIDEO: return json_file_handler(settingsDirs.VIDEO, self.video_settings)
            case settingsType.AUDIO: return json_file_handler(settingsDirs.AUDIO, self.audio_settings)
            case settingsType.KEY_MAPPING: return json_file_handler(settingsDirs.KEY_MAPPING, self.key_mapping)

    