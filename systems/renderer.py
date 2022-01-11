from __future__ import annotations
from typing import Optional

__all__ = ["Renderer", "render_text", "Screen", "GuiScreen"]

from pygame import Surface
from pygame.constants import SRCALPHA

from utils import ORIGIN, load_background
from systems.settings import VIDEO_SETTINGS
from systems.input import Controller, GuiController
from systems.gameObjects import SelectableGuiObject
from systems.gui import MenuButton, CharacterIcon


def load_screen(renderer: Renderer, controller: Controller, size: tuple[int, int], screen_class: Screen) -> None:
    renderer.append(screen_class(size, controller, renderer))


class Renderer:
    def __init__(self, display: Surface, controller: Controller) -> None:
        self.display = display
        self.render_stack: list[Screen] = []
        self.render_stack.append(TitleScreen(VIDEO_SETTINGS["SIZE"], controller, self))

    def append(self, screen: Screen) -> None:
        self.render_stack.append(screen)

    def pop(self, index: Optional[int] = None) -> Screen:
        return self.render_stack.pop(index) if index else self.render_stack.pop()

    def get_top_screen(self) -> Screen:
        return self.render_stack[-1]

    def get_previous_screen(self) -> Screen:
        return self.render_stack[-2]

    def update(self, dt: float) -> None:
        top_screen = self.get_top_screen()
        if top_screen.render_prev_screen:
            prev_screen = self.get_previous_screen()
            prev_screen.update(dt)
        top_screen.update(dt)

    def render(self) -> None:
        self.display.fill((255, 255, 255))
        top_screen = self.get_top_screen()
        if top_screen.render_prev_screen:
            prev_screen = self.get_previous_screen()
            self.display.blit(prev_screen.render(), ORIGIN)
        self.display.blit(top_screen.render(), ORIGIN)


class Screen:
    def __init__(
        self,
        size: tuple[int, int],
        renderer: Renderer,
        controller: Controller,
        render_prev_screen: bool = False,
        background: Optional[Surface] = None,
    ) -> None:
        self.size = size
        self.width: int = size[0]
        self.height: int = size[1]
        self.render_prev_screen: bool = render_prev_screen
        self.background: Surface = background
        self.renderer: Renderer = renderer
        self.controller = controller
        self.canvas: Surface = Surface(size, SRCALPHA)

    def update(self, dt: float) -> None:
        pass

    def render(self) -> Surface:
        if self.background:
            self.canvas.blit(self.background, ORIGIN)
        return self.canvas


class GuiScreen(Screen):
    def __init__(
        self,
        size: tuple[int, int],
        renderer: Renderer,
        controller: Controller,
        render_prev_screen: bool = False,
        background: Optional[Surface] = None,
    ) -> None:
        super().__init__(size, renderer, controller, render_prev_screen, background)
        self.guiController = GuiController()

    def set_grid(self, grid: list[list[SelectableGuiObject]]) -> None:
        self.guiController.grid = grid
        self.guiController.grid[0][0].activate()

    def update(self, dt: float) -> None:
        if self.controller.actions["JUMP"]:
            self.guiController.clicked()
        if self.controller.actions["UP"]:
            self.guiController.up()
        if self.controller.actions["DOWN"]:
            self.guiController.down()
        self.guiController.update(dt)

    def render(self) -> Surface:
        self.guiController.render(super().render())
        return self.canvas


class TitleScreen(GuiScreen):
    def __init__(self, size: tuple[int, int], controller: Controller, renderer: Renderer) -> None:
        super().__init__(size, renderer, controller, background=load_background("menu-background.png", size))
        margin = 150
        self.set_grid(
            [
                [
                    MenuButton(
                        [size[0] // 2, size[1] // 2 - margin],
                        "PLAY",
                        load_screen,
                        [self.renderer, self.controller, self.size, CharacterScreen],
                    )
                ],
                [MenuButton([size[0] // 2, size[1] // 2], "SETTINGS", exit)],
                [MenuButton([size[0] // 2, size[1] // 2 + margin], "EXIT", exit)],
            ]
        )


def dummy():
    pass


class CharacterScreen(GuiScreen):
    def __init__(self, size: tuple[int, int], controller: Controller, renderer: Renderer) -> None:
        super().__init__(size, renderer, controller, background=load_background("menu-background.png", size))
        self.set_grid(
            [
                [
                    CharacterIcon((self.width // 4, self.height // 4), "fire_knight", dummy),
                    CharacterIcon((self.width // 4 * 3, self.height // 4), "ground_monk", dummy),
                ],
                [
                    CharacterIcon((self.width // 4, self.height // 4 * 3), "water_priestess", dummy),
                    CharacterIcon((self.width // 4 * 3, self.height // 4 * 3), "wind_hashashin", dummy),
                ],
            ]
        )
