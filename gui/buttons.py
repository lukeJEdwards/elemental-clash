from pygame import Surface

from systems.gameObjects import Selectable

from utils.functions import load_image, render_text
from utils.paths import assetsDirs
from utils.fonts import FONT_NORMAL_L
from utils.constants import WHITE

__all__ = ["MenuButton"]


class MenuButton(Selectable):
    def __init__(self, pos: tuple[int, int], text: str, callback: callable, *args):
        DEFAULT_SPRITE = load_image(f"{assetsDirs.UI}\\menu-button.png", (366, 76))
        ACTIVE_SPRITE = load_image(f"{assetsDirs.UI}\\menu-button-active.png", (366, 76))
        super().__init__(list(pos), DEFAULT_SPRITE, ACTIVE_SPRITE, callback, *args)

        self.text: str = text
        self.last_updated: float = 0
        self.o_pos: tuple[int, int] = pos
        self.dist: int = -1

    def __str__(self):
        return super().__str__()

    def update(self, dt: float) -> None:
        active = super().update()

        MAX_DIST = 3
        self.last_updated += dt

        if not active and self.pos.y != self.o_pos[1]:
            self.move_ip(0, self.o_pos[1] - self.pos.y)

        if active and self.last_updated > 0.1:
            self.last_updated = 0

            if self.o_pos[1] + MAX_DIST == self.pos.y or self.o_pos[1] - MAX_DIST == self.pos.y:
                self.dist *= -1

            self.move_ip(0, self.dist)

    def render(self, context: Surface) -> None:
        render_text(FONT_NORMAL_L, self.text, WHITE, (self.width // 2, self.height // 2), self.current_sprite)
        super().render(context)
