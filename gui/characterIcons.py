from pygame import SRCALPHA, Surface
from pygame.event import Event
from components.base import Point, textObject

from components.Objects import GuiInteractable, GuiObject
from systems.stateMachine import GAME_STATE

from utils.constants import ORIGIN, characterType, Colour
from utils.fonts import FONT_NORMAL_M
from utils.functions import load_image, scale_image
from utils.paths import assetsDirs


background: str = load_image(f"{assetsDirs.UI}\\player-border-background.png")

border: Surface = load_image(f"{assetsDirs.UI}\\player-border.png")
border_active: Surface = load_image(f"{assetsDirs.UI}\\player-border-active.png")

icons: dict[characterType, Surface] = {
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
    canvas.blit(scale_image(border_active if active else border, size), ORIGIN)
    return canvas


class CharacterIcon(GuiInteractable):
    def __init__(self, pos: Point, character_type: characterType, **kwargs):        
        DEFAULT_SPRITE = make_icon(character_type, False)
        ACTIVE_SPRITE = make_icon(character_type, True)

        super().__init__(pos, DEFAULT_SPRITE, ACTIVE_SPRITE, **kwargs)

        self.character_type = character_type
        self.player_selecting:int = 0
        self.txt_obj = textObject(self.player_selecting+1, FONT_NORMAL_M, Colour.WHITE)

    def update(self, dt: float) -> None:
        super().update()

    def capture_events(self, event: Event) -> None:
        super().capture_events(event)

        if self.clicked:
            GAME_STATE.players[1 if GAME_STATE.player_selection else 0].character = self.character_type
            GAME_STATE.player_selection = not GAME_STATE.player_selection

    def render(self, context: Surface) -> None:
        super().render(context)

        self.txt_obj.text = ""
        if self.character_type == GAME_STATE.players[0].character:
            self.txt_obj.text += "1 "
        if self.character_type == GAME_STATE.players[1].character:
            self.txt_obj.text += "2"
        context.blit(*self.txt_obj.render(self.x, self.y - 20))
            

    def __repr__(self) -> str:
        return f"CharacterIcon({super().__repr__()[16:-1]})"


class ChosenCharacterIcon(GuiObject):
    def __init__(self, pos: Point, player_index: int, size:tuple[int, int] = (78, 78), **kwargs):
        super().__init__(pos, Surface(size, SRCALPHA), **kwargs)

        self.character: characterType = characterType.NONE
        self.background: Surface = scale_image(background, (78, 78))
        self.border: Surface = scale_image(border, (78, 78))
        self.border_active: Surface = scale_image(border_active, (78, 78))
        self.player_index: bool = player_index


    def update(self, dt: float) -> None:
        self.character = GAME_STATE.players[self.player_index].character

    def render(self, context: Surface) -> None:
        self.currrent_sprite.fill((0, 0, 0, 0))
        self.currrent_sprite.blit(self.background, ORIGIN)
        self.currrent_sprite.blit(icons[self.character], (5, 6))
        self.currrent_sprite.blit(self.border_active, ORIGIN)
        super().render(context)

    def __repr__(self) -> str:
        return f"ChosenCharacterIcon({super().__repr__()[13:-1]})"
