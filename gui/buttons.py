from pygame import Surface
from pygame.event import Event
from systems.gameObjects import Selctable

from utils.functions import load_image, render_text, scale_image_2x
from utils.paths import assetsDirs
from utils.fonts import FONT_NORMAL_L
from utils.constants import WHITE


class MenuButton(Selctable):
    def __init__(self, pos: tuple[int, int], text: str, callback: callable, *args):
        DEFAULT_SPRITE = load_image(f"{assetsDirs.UI}\\menu-button.png", (366, 76))
        ACTIVE_SPRITE = load_image(f"{assetsDirs.UI}\\menu-button-active.png", (366, 76))
        super().__init__(list(pos), DEFAULT_SPRITE, ACTIVE_SPRITE, callback, *args)

        self.text: str = text
        self.last_updated: float = 0
        self.o_pos: tuple[int, int] = pos
        self.dist: int = -1

    def update(self, dt: float) -> None:
        active = super().update()

        MAX_DIST = 3
        self.last_updated += dt

        if not active and self.pos != self.o_pos:
            self.pos.update(self.o_pos)

        if active and self.last_updated > 0.1:
            self.last_updated = 0

            if self.o_pos[1] + MAX_DIST == self.pos.y or self.o_pos[1] - MAX_DIST == self.pos.y:
                self.dist *= -1

            self.pos.y += self.dist
            self.rect.move_ip(0, self.dist)

    def render(self, context: Surface) -> None:
        render_text(self.current_sprite, FONT_NORMAL_L, self.text, WHITE, (self.width // 2, self.height // 2))
        super().render(context)
