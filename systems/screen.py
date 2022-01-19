from typing import Optional
from pygame import Surface

from utils.constants import ORIGIN


class Screen:
    def __init__(
        self,
        size: tuple[int, int],
        background: Surface,
        pos: Optional[tuple[int, int]] = ORIGIN,
        render_previous: Optional[bool] = False,
    ) -> None:
        self.size: tuple[int, int] = size
        self.pos = pos
        self.width: int = size[0]
        self.height: int = size[1]
        self.render_previous: bool = render_previous
        self.background: Surface = background
        self.last_updated = 0

    def update(self, dt: float) -> None:
        self.last_updated += dt

    def render(self):
        return self.background
