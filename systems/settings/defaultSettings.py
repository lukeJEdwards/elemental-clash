from pygame.constants import K_RCTRL, K_RSHIFT, K_SPACE, K_a, K_d, K_e, K_h, K_q, K_x

"""All the deafult settings.

All the default settings for the game are defined in the constants below. Custom settings will override those blow and
will be save in the same file.

"""

__all__ = ['AUDIO_SETTINGS','VIDEO_SETTINGS','KEY_MAPPING']

AUDIO_SETTINGS:dict[str:int] = {
    "MASTER": 50,
    "MUSIC": 100,
    "SFX": 100,
}
VIDEO_SETTINGS:dict[str:bool|dict[str:int]] = {
    "FULLSCREEN":False,
    "SIZE":{
        "WIDTH":1280,
        "HEIGHT":720,
    }
}
KEY_MAPPING:dict[str: bool|int] = {
    "LEFT":K_a,
    "RIGHT":K_d,
    "JUMP":K_SPACE,
    "RUN":K_RSHIFT,
    "ROLL":K_RCTRL,
    "DEFEND":False, #mouse right click
    "ATK_1":False, #mouse left click
    "ATK_2":K_q,
    "ATK_3":K_e,
    "ATK_SP":K_x,
    "HEAL":K_h
}