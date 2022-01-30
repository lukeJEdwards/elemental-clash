from typing import Optional

from pygame import Surface

from components.Objects import GuiInteractable

from utils.constants import ORIGIN, characterType
from utils.functions import load_image
from utils.paths import assetsDirs


def icon(character_type: characterType, active: Optional[bool] = False) -> Surface:
    background = load_image(f"{assetsDirs.UI}\\player-border-background.png", (128, 128))
    icon = load_image(f"{assetsDirs.ICONS}\\{character_type.value}.png", (106, 106))
    border = load_image(f'{assetsDirs.UI}\\player-{"border-active" if active else "border"}.png', (128, 128))
    background.blit(icon, (11, 11))
    background.blit(border, ORIGIN)
    return background


class CharacterIcon(GuiInteractable):
    def __init__(self, pos: tuple[int, int], character_type: characterType, **kwargs):
        super().__init__(pos, icon(character_type), icon(character_type, True), **kwargs)
