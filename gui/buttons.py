from pygame import Surface
from pygame.event import Event

from components.base import Point, staticPoint, textObject
from components.objects import GuiInteractable
from gui.notification import Notification
from systems.stateMachine import GAME_STATE

from utils.constants import Colour, characterType, notificationType
from utils.fonts import FONT_NORMAL_L
from utils.paths import assetsDirs
from utils.functions import load_image


def make_button_sprite(text: str, active: bool) -> Surface:
    img_end = "-active.png" if active else ".png"
    sprite = load_image(f"{assetsDirs.UI}\\menu-button{img_end}", (336, 76))
    obj = textObject(text, FONT_NORMAL_L, Colour.WHITE)
    sprite.blit(*obj.render(sprite.get_width() // 2, sprite.get_height() // 2))
    return sprite


class MainMenuButton(GuiInteractable):
    def __init__(self, pos: Point, text: str, call_back: callable, **kwargs) -> None:
        DEFAULT_SPRITE = make_button_sprite(text, False)
        ACTIVE_SPRITE = make_button_sprite(text, True)

        super().__init__(pos=pos, sprite=DEFAULT_SPRITE, active_sprite=ACTIVE_SPRITE, **kwargs)

        self.call_back = call_back

        self.orginal_pos: staticPoint = staticPoint(*pos)
        self.last_updated: int = 0
        self.direction: int = -1

    def update(self, dt: float) -> None:
        super().update()

        MAX = 2
        self.last_updated += dt

        if not self.hovering and self.y != self.orginal_pos.y:
            self.pos.update(*self.orginal_pos)

        if self.hovering and self.last_updated > 0.1:
            self.last_updated = 0

            if self.y not in range(self.orginal_pos.y - MAX, self.orginal_pos.y + MAX):
                self.direction *= -1

            self.move_ip(0, self.direction)

    def capture_events(self, event: Event) -> None:
        super().capture_events(event)

        if self.clicked:
            self.call_back()

    def __repr__(self) -> str:
        return f"MainMenuButton({super().__repr__()[16:-1]})"


class ReadyButton(GuiInteractable):
    def __init__(self, pos: Point, **kwargs):
        DEFAULT_SPRITE = make_button_sprite("READY", False)
        ACTIVE_SPRITE = make_button_sprite("READY", True)
        super().__init__(pos, DEFAULT_SPRITE, ACTIVE_SPRITE, **kwargs)

    @property
    def active(self) -> bool:
        return GAME_STATE.player_ready

    def update(self, dt: float) -> None:
        super().update(dt)

    def capture_events(self, event: Event) -> None:
        super().capture_events(event)

        if self.clicked:
            GAME_STATE.player_ready = not GAME_STATE.player_ready

    def __repr__(self) -> str:
        return f"ReadyButton({super().__repr__()[16:-1]})"


# class BackButton(GuiInteractable):
#     def __init__(self, pos: tuple[int, int], call_back: callable, **kwargs) -> None:
#         DEFAULT_SPRITE, ACTIVE_SPRITE = load_images(
#             [f"{assetsDirs.UI}\\back-button.png", f"{assetsDirs.UI}\\back-button-active.png"],
#             ((128, 128), (128, 128)),
#         )
#         super().__init__(pos, DEFAULT_SPRITE, ACTIVE_SPRITE, **kwargs)

#         self.call_back: callable = call_back

#     def capture_events(self, event: Event) -> None:
#         if self.is_clicked(event):
#             self.call_back()
#             SCREEN_STATE.back()
