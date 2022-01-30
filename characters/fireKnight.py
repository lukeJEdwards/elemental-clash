from components.Objects import CharacterObject
from utils.constants import characterType

class FireKnight(CharacterObject):
    def __init__(self, pos:tuple[int, int]):
        super().__init__(pos=pos, character_type=characterType.FIRE)

