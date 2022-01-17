from __future__ import annotations
from typing import Optional

from pygame import Surface
from pygame.constants import SRCALPHA

from systems.objectPool import ObjectPool

from utils.constants import BLACK, ORIGIN

__all__ = ["Renderer", "Screen"]


class Renderer:
    def __init__(self, display: Surface, inital_screen: Screen) -> None:
        self.display = display

        inital_screen.set_renderer(self)
        self.render_stack: list[Screen] = [inital_screen]

        self.capture_events: callable = lambda event: self.apply_method("capture_events", event)
        self.update: callable = lambda dt: self.apply_method("update", dt)

    def append(self, screen: Screen) -> None:
        self.render_stack.append(screen)

    def pop(self, index: Optional[int] = None) -> Screen:
        return self.render_stack.pop(index) if index else self.render_stack.pop()

    def get_top_screen(self) -> Screen:
        return self.render_stack[-1]

    def get_previous_screen(self) -> Screen:
        return self.render_stack[-2]

    def apply_method(self, method: str, *args) -> None:
        top_screen = self.get_top_screen()
        if top_screen.render_prev_screen:
            prev_screen = self.get_previous_screen()
            getattr(prev_screen, method)(*args)
        getattr(top_screen, method)(*args)

    def render(self) -> None:
        self.display.fill(BLACK)
        top_screen = self.get_top_screen()
        if top_screen.render_prev_screen:
            prev_screen = self.get_previous_screen()
            self.display.blit(prev_screen.render(), ORIGIN)
        self.display.blit(top_screen.render(), ORIGIN)


class Screen:
    def __init__(
        self, size: tuple[int, int], renderer: Optional[Renderer], render_prev_screen: Optional[bool] = False
    ) -> None:
        self.size = size
        self.width: int = size[0]
        self.height: int = size[1]
        self.renderer = renderer
        self.render_prev_screen: bool = render_prev_screen
        self.background: Surface | list = []
        self.object_pool: ObjectPool | list = []
        self.canvas: Surface = Surface(size, SRCALPHA)

        self.capture_events: callable = lambda event: self.apply_method("capture_events", event)
        self.update: callable = lambda dt: self.apply_method("update", dt)

    def init_pool(self, *args) -> None:
        self.object_pool = ObjectPool(*args)

    def set_renderer(self, renderer: Renderer) -> None:
        self.renderer = renderer

    def set_background(self, background: Surface) -> None:
        self.background = background

    def apply_method(self, method: str, *args):
        for obj in self.object_pool:
            getattr(obj, method)(*args)

    def render(self) -> Surface:
        if self.background:
            self.canvas.blit(self.background, ORIGIN)
        self.apply_method("render", self.canvas)

        surf = Surface((366, 76))
        surf.fill((255, 0, 0))

        self.canvas.blit(surf, (457, 458))
        self.canvas.blit(surf, (457, 594))

        return self.canvas
