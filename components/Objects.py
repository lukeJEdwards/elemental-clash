from __future__ import annotations
from dataclasses import dataclass, field
from typing import Iterable, Optional


from uuid import UUID, uuid4

from pygame import Rect, Surface, mouse
from pygame.constants import MOUSEBUTTONDOWN
from pygame.event import Event

from components.base import Dimension, Point, Size, Location

from utils.constants import BACKGROUND, Colour
from utils.fonts import FONT_NORMAL_L
from utils.functions import get_center


class Screen(Dimension):
    def __init__(self, size: Size) -> None:
        super().__init__(size=size)

    @property
    def background(self) -> BACKGROUND:
        pass

    def load_pool(self) -> Iterable[RenderObject]:
        pass


@dataclass
class Title(Location):
    pos: Point
    text: str
    colour: Colour
    id: UUID = field(default_factory=uuid4)
    alpha: int = 255

    def render(self, context: Surface) -> None:
        surf = FONT_NORMAL_L.render(self.text, True, self.colour.value)
        surf.set_alpha(self.alpha)
        rect = surf.get_rect()
        rect.center = (self.x, self.y + 4)
        context.blit(surf, rect)


class RenderObject(Location, Dimension):
    def __init__(self, pos: Point, sprite: Surface, **kwargs) -> None:
        super().__init__(pos=pos, size=Size(*sprite.get_size()))
        self.id: UUID = uuid4()
        self.currrent_sprite: Surface = sprite

        if kwargs.get("center", False):
            self.pos.update(*get_center(pos, self.size))

    def move_ip(self, x: int, y: int) -> None:
        self.pos.move_ip(x, y)

    def render(self, context: Surface) -> None:
        context.blit(self.currrent_sprite, self.pos.toTuple())

    def __repr__(self) -> str:
        return f"RenderObject(id={self.id}, pos={repr(self.pos)}, size={repr(self.size)})"


class GuiObject(RenderObject):
    def __init__(self, pos: Point, sprite: Surface, **kwargs) -> None:
        super().__init__(pos, sprite, **kwargs)

    def update(self, dt: float) -> None:
        pass


class GuiInteractable(GuiObject):
    def __init__(self, pos: Point, sprite: Surface, active_sprite: Surface, **kwargs) -> None:
        super().__init__(pos=pos, sprite=sprite, **kwargs)

        self.rect: Rect = Rect(self.pos.toTuple(), self.size.toTuple())

        self.default_sprite: Surface = sprite
        self.active_sprite: Surface = active_sprite

        self.clicked: bool = False

    @property
    def hovering(self) -> bool:
        return self.rect.collidepoint(mouse.get_pos())

    @property
    def active(self) -> bool:
        return self.hovering

    def move_ip(self, x: int, y: int) -> None:
        super().move_ip(x, y)
        self.rect.move_ip(x, y)

    def update(self, dt: Optional[float] = 0) -> None:
        self.currrent_sprite = self.active_sprite if self.active else self.default_sprite

    def capture_events(self, event: Event) -> None:
        self.clicked = event.type == MOUSEBUTTONDOWN and self.hovering

    def __repr__(self) -> str:
        return f"GuiInteractable({super().__repr__()[13:-1]}, rect={repr(self.rect)})"
