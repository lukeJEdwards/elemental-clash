from pygame import Surface
from pygame.event import Event

from components.Objects import GuiInteractable

from utils.constants import WHITE
from utils.fonts import FONT_NORMAL_L
from utils.paths import assetsDirs
from utils.functions import load_images, render_text


class MainMenuButton(GuiInteractable):
    def __init__(
        self, pos: tuple[int, int], text: str, call_back: callable = lambda: print("clicked"), **kwargs
    ) -> None:
        DEFAULT_SPRITE, ACTIVE_SPRITE = load_images(
            [f"{assetsDirs.UI}\\menu-button.png", f"{assetsDirs.UI}\\menu-button-active.png"],
            ((336, 76), (336, 76)),
        )
        super().__init__(pos=pos, sprite=DEFAULT_SPRITE, active_sprite=ACTIVE_SPRITE, **kwargs)

        self.call_back = call_back
        self.text: str = text
        self.last_updated: int = 0
        self.direction: int = -1

    def capture_events(self, event: Event) -> None:
        self.is_clicked(event)

    def update(self, dt: float) -> None:
        super().update()

        MAX = 2
        self.last_updated += dt
        active = self.is_mouse_hovering()

        if not active and self.pos.y != self.orginal_pos[1]:
            self.move_ip(0, self.orginal_pos[1] - self.pos.y)

        if active and self.last_updated > 0.1:
            self.last_updated = 0

            if self.pos.y not in range(self.orginal_pos[1] - MAX, self.orginal_pos[1] + MAX):
                self.direction *= -1

            self.move_ip(0, self.direction)

    def is_clicked(self, event: Event) -> bool:
        is_clicked = super().is_clicked(event)
        if is_clicked:
            self.call_back()

    def render(self, context: Surface) -> None:
        render_text(FONT_NORMAL_L, self.text, WHITE, (self.size[0] // 2, self.size[1] // 2), self.currrent_sprite)
        super().render(context)

    def __str__(self) -> str:
        return super().__str__()
