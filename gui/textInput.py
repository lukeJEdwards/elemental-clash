from typing import Optional
from pygame import K_BACKSPACE, K_RETURN, KEYDOWN, MOUSEBUTTONDOWN, Surface
from pygame.event import Event

from components.Objects import GuiInteractable

from systems.settings import SETTINGS

from utils.constants import WHITE
from utils.fonts import FONT_LIGHT_M
from utils.functions import load_images, render_text
from utils.paths import assetsDirs


class TextInput(GuiInteractable):
    def __init__(
        self,
        pos: tuple[int, int],
        filler_text: Optional[str] = "",
        default_txt: Optional[str] = "",
        disabled: Optional[bool] = False,
        **kwargs,
    ):
        DEFAULT_SPRITE, ACTIVE_SPRITE = load_images(
            [f"{assetsDirs.UI}\\text-input.png", f"{assetsDirs.UI}\\text-input-active.png"],
            ((306, 48), (306, 48)),
        )
        super().__init__(pos=pos, sprite=DEFAULT_SPRITE, active_sprite=ACTIVE_SPRITE, **kwargs)

        self._filler_text: str = filler_text
        self._default_txt: str = default_txt
        self._text: str = default_txt
        self.disabled: bool = disabled
        self.active = False

    def update(self, dt: float) -> None:
        self.currrent_sprite = self.active_sprite if self.active or self.disabled else self.default_sprite

    def capture_events(self, event: Event) -> None:
        if event.type == MOUSEBUTTONDOWN:
            self.active = self.is_mouse_hovering()

        if self.active and event.type == KEYDOWN and not self.disabled:
            if event.key == K_BACKSPACE:
                self._text = self._text[:-1]
            elif event.key == K_RETURN:
                self.active = False
            else:
                self._text += event.unicode
            SETTINGS[self._default_txt] = self._text

    def render(self, context: Surface) -> None:
        super().render(context)

        txt_surf = render_text(FONT_LIGHT_M, self._text if len(self._text) > 0 else self._filler_text, WHITE)
        if len(self._text) < 1:
            txt_surf.set_alpha(100)
        pos = (
            self.pos.x + self.size[0] // 2 - txt_surf.get_width() // 2,
            self.pos.y + self.size[1] // 2 - txt_surf.get_height() // 2 + 3,
        )
        context.blit(txt_surf, pos)
