from characters.character import Character
from utils.constants import characterType


class FireKnight(Character):
    def __init__(self, pos: tuple[int, int]):
        super().__init__(pos=pos, character_type=characterType.FIRE)
