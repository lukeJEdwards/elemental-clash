from typing import Optional
from pygame import SRCALPHA, Surface
from pygame.event import Event

from components.Objects import GuiInteractable, GuiObject
from systems.stateMachine import GAME_STATE

from utils.constants import ORIGIN, characterType
from utils.functions import load_image, scale_image
from utils.paths import assetsDirs


background = load_image(f"{assetsDirs.UI}\\player-border-background.png")
border = lambda active: load_image(f'{assetsDirs.UI}\\player-{"border-active" if active else "border"}.png')

icons = {
    characterType.FIRE: load_image(f"{assetsDirs.ICONS}\\{characterType.FIRE.value}.png"),
    characterType.EARTH: load_image(f"{assetsDirs.ICONS}\\{characterType.EARTH.value}.png"),
    characterType.WATER: load_image(f"{assetsDirs.ICONS}\\{characterType.WATER.value}.png"),
    characterType.AIR: load_image(f"{assetsDirs.ICONS}\\{characterType.AIR.value}.png"),
    characterType.NONE: Surface((64, 64), SRCALPHA),
}


def make_icon(character_type: characterType, active: bool):
    size = (128, 128)
    canvas = Surface(size, SRCALPHA)
    canvas.blit(scale_image(background, size), ORIGIN)
    canvas.blit(scale_image(icons[character_type], (106, 106)), (11, 11))
    canvas.blit(scale_image(border(active), size), ORIGIN)
    return canvas


class CharacterIcon(GuiInteractable):
    def __init__(self, pos: tuple[int, int], character_type: characterType, **kwargs):
        DEFAULT_SPRITE = make_icon(character_type, False)
        ACTIVE_SPRITE = make_icon(character_type, True)

        super().__init__(pos, DEFAULT_SPRITE, ACTIVE_SPRITE, **kwargs)

        self.character_type = character_type

    def capture_events(self, event: Event) -> None:
        if self.is_clicked(event) and not GAME_STATE._player_data["1"]["ready"]:
            GAME_STATE._player_data["1"]["character"] = self.character_type

    def update(self, dt: Optional[float] = 0) -> None:
        super().update()
        if GAME_STATE._player_data["1"]["ready"]:
            self.currrent_sprite = self.default_sprite

        if GAME_STATE._player_data["1"]["character"] == self.character_type:
            self.currrent_sprite = self.active_sprite


class ChosenCharacterIcon(GuiObject):
    def __init__(self, pos: tuple[int, int], player: str, **kwargs):
        self.canvas: Surface = Surface((78, 78), SRCALPHA)
        super().__init__(pos, self.canvas, **kwargs)

        self.icon: Surface = icons[characterType.NONE]
        self.background = scale_image(background, self.size)
        self.player = player

    def change_icon(self, character_type: characterType) -> None:
        self.icon = icons[character_type]

    def update(self, dt: float) -> None:
        if GAME_STATE._player_data[self.player]["character"] != characterType.NONE:
            self.change_icon(GAME_STATE._player_data[self.player]["character"])

    def render(self, context: Surface) -> None:
        self.canvas.fill((0, 0, 0, 0))
        self.canvas.blit(self.background, ORIGIN)
        self.canvas.blit(self.icon, (5, 6))
        self.canvas.blit(scale_image(border(GAME_STATE._player_data[self.player]["ready"]), self.size), ORIGIN)
        context.blit(self.canvas, (self.pos.x, self.pos.y - self.size[0] // 4))
