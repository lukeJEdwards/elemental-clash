from pygame import Surface
from pygame.event import Event
from components.base import Point, textObject

from components.objects import GuiInteractable
from systems.settings import SETTINGS
from systems.stateMachine import GAME_STATE

from utils.constants import Colour, notificationType
from utils.fonts import FONT_LIGHT_S
from utils.functions import load_image
from utils.paths import assetsDirs


def create_notification(msg: str, type: notificationType):
    notification = load_image(f"{assetsDirs.UI}\\{type.value}.png", (244, 76))
    txt_obj = textObject(msg, FONT_LIGHT_S, Colour.WHITE)
    notification.blit(*txt_obj.render(notification.get_width() // 2, notification.get_height() // 2))
    return notification


class Notification(GuiInteractable):
    def __init__(self, msg: str, type: notificationType) -> None:
        SPRITE = create_notification(msg, type)
        super().__init__(Point(SETTINGS["SIZE"][0] // 2, 50), SPRITE, SPRITE, center=True)

        self.type = type
        self.msg = msg

        self.toggle: bool = True
        self.timer: float = 1.5
        self.last_updated: float = 0
        self.alpha: int = 0

    def update(self, dt: float) -> None:
        super().update()
        self.last_updated += dt
        self.timer -= dt

        if self.timer <= 0:
            self.toggle = False

        if self.last_updated > 0.01:
            self.last_updated = 0
            self.alpha = self.alpha + 10 if self.toggle else self.alpha - 10

        if self.alpha <= 0 and not self.toggle:
            GAME_STATE.notification_pool.pop()

    def capture_events(self, event: Event) -> None:
        super().capture_events(event)

        if self.clicked:
            GAME_STATE.notification_pool.pop()

    def render(self, context: Surface) -> None:
        self.currrent_sprite.set_alpha(self.alpha)
        return super().render(context)

    def __repr__(self) -> str:
        return f"Notification({super().__repr__()[16:-1]}, msg={self.msg}, type={self.type})"
