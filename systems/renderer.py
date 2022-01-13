from __future__ import annotations
from typing import Optional

from sys import exit
from pygame import Surface
from pygame.constants import SRCALPHA
from pygame.event import Event

from gui.buttons import MenuButton
from gui.characterIcon import CharacterIcon
from systems.settings import VIDEO_SETTINGS
from systems.objectPool import ObjectPool
from utils.constants import BLACK, ORIGIN, MENU_BACKGROUND, characterType
from utils.functions import load_background

__all__ = ["Renderer", "Screen"]


class Renderer:
    def __init__(self, display: Surface) -> None:
        self.display = display
        self.render_stack: list[Screen] = [MainMenu(VIDEO_SETTINGS["SIZE"], self)]

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

    def capture_events(self, event: Event) -> None:
        self.apply_method("capture_events", event)

    def update(self, dt: float) -> None:
        self.apply_method("update", dt)

    def render(self) -> None:
        self.display.fill(BLACK)
        top_screen = self.get_top_screen()
        if top_screen.render_prev_screen:
            prev_screen = self.get_previous_screen()
            self.display.blit(prev_screen.render(), ORIGIN)
        self.display.blit(top_screen.render(), ORIGIN)


class Screen:
    def push(renderer: Renderer) -> None:
        pass

    def __init__(self, size: tuple[int, int], renderer: Renderer, render_prev_screen: Optional[bool] = False) -> None:
        self.size = size
        self.width: int = size[0]
        self.height: int = size[1]
        self.renderer = renderer
        self.render_prev_screen: bool = render_prev_screen
        self.background: Surface | list = []
        self.object_pool: ObjectPool | list = []
        self.canvas: Surface = Surface(size, SRCALPHA)

    def init_pool(self, *args) -> None:
        self.object_pool = ObjectPool(*args)

    def set_background(self, background: Surface) -> None:
        self.background = background

    def capture_events(self, event: Event) -> None:
        for obj in self.object_pool:
            obj.capture_events(event)

    def update(self, dt: float) -> None:
        for obj in self.object_pool:
            obj.update(dt)

    def render(self) -> Surface:
        if self.background:
            self.canvas.blit(self.background, ORIGIN)
        for obj in self.object_pool:
            obj.render(self.canvas)
        return self.canvas


class MainMenu(Screen):
    def __init__(self, size: tuple[int, int], renderer: Renderer):
        super().__init__(size, renderer)
        self.set_background(MENU_BACKGROUND)

        MARGIN = 100
        self.init_pool(
            MenuButton(
                (self.width // 2, self.height // 2 - MARGIN),
                "PLAY",
                clicked,
                self.renderer,
            ),
            MenuButton(
                (self.width // 2, self.height // 2),
                "SETTINGS",
                clicked,
                self.renderer,
            ),
            MenuButton((self.width // 2, self.height // 2 + MARGIN), "QUIT", exit),
        )


def clicked(*args):
    print("clicked")
