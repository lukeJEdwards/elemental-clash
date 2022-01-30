from pygame import Surface
from pygame.event import Event

from components.Objects import GuiInteractable
from systems.settings import SETTINGS
from systems.stateMachine import SCREEN_STATE

from utils.constants import WHITE, notificationType
from utils.fonts import FONT_LIGHT_S
from utils.functions import load_image, render_text
from utils.paths import assetsDirs


class Notification(GuiInteractable):
    def __init__(self, message: str, type: notificationType) -> None:
        SPRITE = load_image(f"{assetsDirs.UI}\\{type.value}.png", (244, 76))
        POS = (SETTINGS["SIZE"][0] // 2, 50)
        super().__init__(POS, SPRITE, SPRITE, center=True)

        self.message: str = message
        self.type: notificationType = type

        self.toggle: bool = True
        self.timer: float = 1
        self.last_updated: float = 0
        self.alpha: int = 0

    def capture_events(self, event: Event) -> None:
        if self.is_clicked(event):
            SCREEN_STATE._notification_pool.pop()

    def update(self, dt: float) -> None:
        self.last_updated += dt
        self.timer -= dt

        if self.timer <= 0:
            self.toggle = False

        if self.last_updated > 0.01:
            self.last_updated = 0
            self.alpha = self.alpha + 10 if self.toggle else self.alpha - 10

        if self.alpha <= 0 and not self.toggle:
            SCREEN_STATE._notification_pool.pop()

    def render(self, context: Surface) -> None:
        render_text(FONT_LIGHT_S, self.message, WHITE, (self.size[0] // 2, self.size[1] // 2), self.currrent_sprite)
        self.currrent_sprite.set_alpha(self.alpha)
        return super().render(context)
