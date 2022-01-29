from pygame.constants import K_LCTRL, K_LSHIFT, K_SPACE, K_a, K_d, K_e, K_x

from systems.contoller import KeyboardInput, ButtonInput, AxisInput, HatInput, ControllerNavInput
from utils import ControllerButton, ControllerAxis, ControllerHat
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
VIDEO_SETTINGS:dict[str:bool|int|dict[str:int]] = {
    "FULLSCREEN":False,
    "FPS_TARGET":60,
    "SIZE":(1280, 720)
}
KEY_MAPPING:dict[str: dict] = {
    'KEYBOARD':{
        'ATK_1':ButtonInput(1).serialize(),
        'ATK_2':ButtonInput(1, 2).serialize(),
        'ATK_3':ButtonInput(1, 3).serialize(),
        'ATK_SP':KeyboardInput(K_x).serialize(),
        'DEFEND':ButtonInput(3).serialize(),
        'HEAL':KeyboardInput(K_e).serialize(),
        'JUMP':KeyboardInput(K_SPACE).serialize(),
        'LEFT':KeyboardInput(K_a).serialize(),
        'RIGHT': KeyboardInput(K_d).serialize(),
        'ROLL':KeyboardInput(K_LCTRL).serialize(),
        'RUN':KeyboardInput(K_LSHIFT).serialize()
        },
    'CONTROLLER':{
        "ATK_1": ButtonInput(ControllerButton.X).serialize(),
        "ATK_2": ButtonInput(ControllerButton.X, 2).serialize(),
        "ATK_3": ButtonInput(ControllerButton.Y).serialize(),
        "ATK_SP": HatInput(ControllerHat.HAT_RIGHT).serialize(),
        "DEFEND": AxisInput(ControllerAxis.L_TRIGGER, True).serialize(),
        "HEAL": HatInput(ControllerHat.HAT_UP).serialize(),
        "JUMP": ButtonInput(ControllerButton.A).serialize(),
        "LEFT": AxisInput(ControllerAxis.L_STICK_X).serialize(),
        "RIGHT": AxisInput(ControllerAxis.L_STICK_X).serialize(),
        "ROLL": ButtonInput(ControllerButton.B).serialize(),
        "RUN": AxisInput(ControllerAxis.R_TRIGGER, True).serialize(),
        "UP": ControllerNavInput(ControllerAxis.L_STICK_Y, ControllerHat.HAT_UP).serialize(),
        "DOWN": ControllerNavInput(ControllerAxis.L_STICK_Y, ControllerHat.HAT_DOWN).serialize(),
        "RIGHT": ControllerNavInput(ControllerAxis.L_STICK_X, ControllerHat.HAT_RIGHT).serialize(),
        "LEFT": ControllerNavInput(ControllerAxis.L_STICK_X, ControllerHat.HAT_LEFT).serialize()
        }
}