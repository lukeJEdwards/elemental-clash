from enum import IntEnum

__all__ = [ 'ORIGIN', 'actionEnum', 'settingsEnum']


ORIGIN:tuple = (0, 0)

class actionEnum(IntEnum):
    LEFT = 0
    RIGHT = 1
    JUMP = 2
    RUN = 3
    ROLL = 4
    DEFEND = 5 
    ATK_1 = 6 
    ATK_2 = 7
    ATK_3 = 8
    ATK_SP = 9
    HEAL = 10
    
class settingsEnum(IntEnum):
    VIDEO = 0
    AUDIO = 1
    KEY_MAPPING = 2
