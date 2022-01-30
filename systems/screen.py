from typing import Optional
from pygame import Surface
from components.objectPools import objectPool
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
        self.width: int = size[0]
        self.height: int = size[1]
        self.background: Surface = background
        self.pos: tuple[int, int] = pos
        self.render_previous: bool = render_previous
        self.canvas: Surface = Surface(size)

    def render(self) -> Surface:
        self.canvas.blit(self.background, ORIGIN)
        return self.canvas
