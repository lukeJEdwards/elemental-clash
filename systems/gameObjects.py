from __future__ import annotations
from typing import Optional

from pygame import Rect, Surface, Vector2, mouse
from uuid import UUID, uuid4
from pygame.constants import MOUSEBUTTONUP

from pygame.event import Event

__all__ = ["GameObject"]


class GameObject:
    def __init__(self, pos: tuple[int, int], sprite: Surface, **kwargs) -> None:
        super().__init__(**kwargs)
        self.id: UUID = uuid4()
        self.pos: Vector2 = Vector2(pos)
        self.current_sprite: Surface = sprite
        self.size: tuple[int, int] = self.current_sprite.get_size()
        self.width: int = self.size[0]
        self.height: int = self.size[1]
        self.rect = Rect(self.get_center(), self.size)

    def get_center(self) -> tuple[int, int]:
        return (self.pos[0] - self.width // 2, self.pos[1] - self.height // 2)

    def capture_events(self, event: Event) -> None:
        pass

    def update(self, dt: Optional[float] = 0) -> None:
        pass

    def render(self, context: Surface) -> None:
        context.blit(self.current_sprite, self.get_center())


class Selctable(GameObject):
    def __init__(
        self, pos: tuple[int, int], default_sprite: Surface, active_sprite: Surface, callback: callable, *args, **kwargs
    ) -> None:
        super().__init__(pos, default_sprite, **kwargs)
        self.default_sprite: Surface = default_sprite
        self.active_sprite: Surface = active_sprite
        self.callback: callable = callback
        self.args: tuple = args

    def click_handler(self, event: Event) -> None:
        if self.is_active() and event.type == MOUSEBUTTONUP:
            if self.args:
                self.callback(*self.args)
            else:
                self.callback()

    def is_active(self) -> bool:
        return True if self.rect.collidepoint(mouse.get_pos()) else False

    def capture_events(self, event: Event) -> None:
        self.click_handler(event)

    def update(self, dt: Optional[float] = 0) -> None:
        active = self.is_active()
        self.current_sprite = self.active_sprite if active else self.default_sprite
        return active
