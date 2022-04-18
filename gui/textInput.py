from uuid import UUID
from pygame import K_BACKSPACE, K_RETURN, KEYDOWN, MOUSEBUTTONDOWN, Surface
from pygame.event import Event

from components.base import Point, textObject
from components.Objects import GuiInteractable, GuiObject
from systems.stateMachine import GAME_STATE

from utils.constants import Colour
from utils.fonts import FONT_LIGHT_M
from utils.functions import load_image
from utils.paths import assetsDirs


class TextInput(GuiInteractable):
    def __init__(self, pos: Point, filler_text: str = "", **kwargs):
        DEFAULT_SPRITE = load_image(f"{assetsDirs.UI}\\text-input.png", (306, 48))
        ACTIVE_SPRITE = load_image(f"{assetsDirs.UI}\\text-input-active.png", (306, 48))
        super().__init__(pos=pos, sprite=DEFAULT_SPRITE, active_sprite=ACTIVE_SPRITE, **kwargs)

        self.filler_text: str = filler_text
        self.text_obj: textObject = textObject(filler_text, FONT_LIGHT_M, Colour.WHITE, 127)
        self.text: str = ""
        self.toggle: bool = False

    @property
    def active(self) -> bool:
        return self.toggle

    def update(self, dt: float = 0) -> None:
        super().update()

        if len(self.text) > 0:
            self.text_obj.update(self.text)
            self.text_obj.alpha = 255
        else:
            self.text_obj.update(self.filler_text)
            self.text_obj.alpha = 127

    def capture_events(self, event: Event) -> None:
        if event.type == MOUSEBUTTONDOWN:
            self.toggle = self.hovering

        if self.active and event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == K_RETURN:
                self.toggle = False
            else:
                self.text += event.unicode

    def render(self, context: Surface) -> None:
        super().render(context)
        txt_surf, rect = self.text_obj.render(self.x + self.width / 2, self.y + self.height / 2)
        context.blit(txt_surf, rect)

    def __repr__(self) -> str:
        return f"TextInput({super().__repr__()[16:-1]})"


class PlayerLable(GuiObject):
    def __init__(self, pos: Point, player_index: int, **kwargs) -> None:
        super().__init__(pos, load_image(f"{assetsDirs.UI}\\text-input-active.png", (306, 48)), **kwargs)
        self.player_index = player_index

        text: textObject = textObject(self.name, FONT_LIGHT_M, Colour.WHITE)
        self.currrent_sprite.blit(*text.render(self.width // 2, self.height // 2))

    @property
    def name(self) -> str:
        return GAME_STATE.players[self.player_index].name

    def __repr__(self) -> str:
        return f"PlayerLable({super().__repr__()[13:-1]})"
