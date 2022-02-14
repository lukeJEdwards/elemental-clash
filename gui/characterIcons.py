from pygame import SRCALPHA, Surface
from pygame.event import Event
from components.base import Point

from components.objects import GuiInteractable, GuiObject
from server.client import CLIENT
from systems.stateMachine import GAME_STATE

from utils.constants import ORIGIN, characterType
from utils.functions import load_image, scale_image
from utils.paths import assetsDirs


background: str = load_image(f"{assetsDirs.UI}\\player-border-background.png")

border: Surface = load_image(f"{assetsDirs.UI}\\player-border.png")
border_active: Surface = load_image(f"{assetsDirs.UI}\\player-border-active.png")

icons: dict[characterType, Surface] = {
    characterType.FIRE: load_image(characterType.FIRE.value),
    characterType.EARTH: load_image(characterType.EARTH.value),
    characterType.WATER: load_image(characterType.WATER.value),
    characterType.AIR: load_image(characterType.AIR.value),
    characterType.NONE: Surface((64, 64), SRCALPHA),
}


def make_icon(character_type: characterType, active: bool):
    size = (128, 128)
    canvas = Surface(size, SRCALPHA)
    canvas.blit(scale_image(background, size), ORIGIN)
    canvas.blit(scale_image(icons[character_type], (106, 106)), (11, 11))
    canvas.blit(scale_image(border_active if active else border, size), ORIGIN)
    return canvas


class CharacterIcon(GuiInteractable):
    def __init__(self, pos: Point, character_type: characterType, **kwargs):
        DEFAULT_SPRITE = make_icon(character_type, False)
        ACTIVE_SPRITE = make_icon(character_type, True)

        super().__init__(pos, DEFAULT_SPRITE, ACTIVE_SPRITE, **kwargs)

        self.character_type = character_type

    @property
    def active(self) -> bool:
        return GAME_STATE.player_character == self.character_type

    def update(self, dt: float) -> None:
        super().update()

    def capture_events(self, event: Event) -> None:
        super().capture_events(event)

        if self.clicked and self.character_type != GAME_STATE.player_character:
            GAME_STATE.player_character = self.character_type

    def __repr__(self) -> str:
        return f"CharacterIcon({super().__repr__()[16:-1]})"


class ChosenCharacterIcon(GuiObject):
    def __init__(self, pos: Point, opponent: bool, **kwargs):
        super().__init__(pos, Surface((78, 78), SRCALPHA), **kwargs)

        self.character: characterType = characterType.NONE
        self.background: Surface = scale_image(background, (78, 78))
        self.border: Surface = scale_image(border, (78, 78))
        self.border_active: Surface = scale_image(border_active, (78, 78))
        self.opponent: bool = opponent

    @property
    def ready(self) -> bool:
        return GAME_STATE.opponent_ready if self.opponent else GAME_STATE.player_ready

    def update(self, dt: float) -> None:
        if self.opponent:
            self.character = GAME_STATE.opponent_character
        else:
            self.character = GAME_STATE.player_character

    def render(self, context: Surface) -> None:
        self.currrent_sprite.fill((0, 0, 0, 0))
        self.currrent_sprite.blit(self.background, ORIGIN)
        self.currrent_sprite.blit(icons[self.character], (5, 6))
        self.currrent_sprite.blit(self.border_active if self.ready else self.border, ORIGIN)
        super().render(context)

    def __repr__(self) -> str:
        return f"ChosenCharacterIcon({super().__repr__()[13:-1]})"
