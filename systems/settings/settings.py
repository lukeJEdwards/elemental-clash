from os import path

from utils import settingsEnum, json_file_handler, settingsDirs
from systems.settings.defaultSettings import AUDIO_SETTINGS, VIDEO_SETTINGS, KEY_MAPPING

__all__ = ['Settings']

class Settings:
    """Settings class.
    
    Contains all settings for the game; includes video, audio settings and the key mappings.
    
    Attributes:\n
        video_settings (dict): Settings for all the renderer and screens.
        audio_settings (dict): Settings for all sounds.
        key_mapping (dict): All the mappings for the keys and controlers.
    
    """
    def __init__(self) -> None:
        self.video_settings:dict = self.load_setting(settingsDirs.VIDEO, VIDEO_SETTINGS)
        self.audio_settings:dict = self.load_setting(settingsDirs.AUDIO, AUDIO_SETTINGS)
        self.key_mapping:dict = self.load_setting(settingsDirs.KEY_MAPPING, KEY_MAPPING)
        
    def load_setting(self, file_path:str, default_values:dict) -> dict:
        """Loads setting from file.

        Args:
            file_path (str): Path to the settings file.
            default_values (dict): the default values for the settings if not found in the file.

        Returns:
            dict: The settings from the file.
        """
        if path.exists(file_path):
            return json_file_handler(file_path)
        else:   
            return json_file_handler(file_path, default_values)
        
    def save_setting(self, enum:settingsEnum) -> dict:
        """Save the settings to a file.

        Args:
            enum (settingsEnum): Which settings to save.

        Returns:
            dict: The saved settings.
        """
        match enum:
            case settingsEnum.VIDEO:
                return json_file_handler(settingsDirs.VIDEO, self.video_settings)
            case settingsEnum.AUDIO:
                return json_file_handler(settingsDirs.AUDIO, self.audio_settings)
            case settingsEnum.KEY_MAPPING:
                return json_file_handler(settingsDirs.KEY_MAPPING, self.key_mapping)
        
    