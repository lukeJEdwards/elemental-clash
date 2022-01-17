from typing import Optional

from systems.gameObjects import Selectable

from utils.constants import ORIGIN, characterType
from utils.functions import load_image, load_images
from utils.paths import assetsDirs

__all__ = ["CharacterIcon"]


def load_icon(type: characterType, is_active: Optional[bool] = False):
    border_size = (256, 256)
    icon_size = (212, 212)
    border = (
        load_image(f"{assetsDirs.UI}\\player-border-active.png", border_size)
        if is_active
        else load_image(f"{assetsDirs.UI}\\player-border.png", border_size)
    )
    background, icon = load_images(
        [f"{assetsDirs.UI}\\player-border-background.png", f"{assetsDirs.ICONS}\\{type.value}.png"],
        (border_size, icon_size),
    )
    background.blits(blit_sequence=((icon, (22, 22)), (border, ORIGIN)))
    return background


class CharacterIcon(Selectable):
    def __init__(self, pos: tuple[int, int], character_type: characterType, callback: callable, *args) -> None:
        DEFAULT_SPRITE = load_icon(character_type)
        ACTIVE_SPRITE = load_icon(character_type, True)
        super().__init__(pos, DEFAULT_SPRITE, ACTIVE_SPRITE, callback, *args)
        self.character_type = character_type
