__all__ = ["Controller", "GuiController"]

from pygame.constants import JOYDEVICEADDED, JOYDEVICEREMOVED
from pygame.event import Event

from utils import inputType
from systems.input import BaseInput, ButtonInput
from systems.gameObjects import SelectableGuiObject


class Controller:
    def __init__(self, key_mapping: dict[str, BaseInput]) -> None:
        self.key_mapping: dict[str, BaseInput] = {
            key: value for key, value in key_mapping.items() if value.input_type != inputType.BUTTON
        }
        self.button_mapping: dict[str, ButtonInput] = {
            key: value for key, value in key_mapping.items() if value.input_type == inputType.BUTTON
        }
        self.actions: dict[str, bool | float] = {
            key: 0 if value.input_type == inputType.AXIS else False for key, value in key_mapping.items()
        }
        self.controller_connected: bool = False

    def controller_state(self, event: Event) -> None:
        if event.type == JOYDEVICEADDED:
            self.controller_connected = True
        if event.type == JOYDEVICEREMOVED:
            self.controller_connected = False

    def button_update(self, event: Event, dt: float) -> None:
        for key, value in self.button_mapping.items():
            self.actions[key] = value.input_handler(event, dt)

    def key_update(self, event: Event) -> None:
        for key, value in self.key_mapping.items():
            self.actions[key] = value.input_handler(event)

    def update(self, event: Event, dt: float) -> None:
        self.controller_state(event)
        self.button_update(event, dt)
        self.key_update(event)


class GuiController:
    def __init__(self) -> None:
        self.grid: list[list[SelectableGuiObject]] = []
        self.current_index_x: int = 0
        self.current_index_y: int = 0
        self.last_updated = 0

    def wait(self) -> bool:
        return self.last_updated > 0.2

    def next(self) -> None:
        self.current_index_x = (self.current_index_x + 1) % len(self.grid[self.current_index_x])

    def prev(self) -> None:
        self.current_index_x = (self.current_index_x - 1) % len(self.grid[self.current_index_x])

    def up(self) -> None:
        if self.wait():
            self.last_updated = 0
            self.grid[self.current_index_y][self.current_index_x].deactivate()
            self.current_index_y = (self.current_index_y - 1) % len(self.grid)
            self.grid[self.current_index_y][self.current_index_x].activate()

    def down(self) -> None:
        if self.wait():
            self.last_updated = 0
            self.grid[self.current_index_y][self.current_index_x].deactivate()
            self.current_index_y = (self.current_index_y + 1) % len(self.grid)
            self.grid[self.current_index_y][self.current_index_x].activate()

    def clicked(self) -> None:
        if self.wait():
            self.last_updated = 0
            self.grid[self.current_index_y][self.current_index_x].clicked()

    def check_x_bounds(self) -> None:
        if self.current_index_x > len(self.grid[self.current_index_y]):
            self.current_index_x = len(self.grid[self.current_index_y])

    def update(self, dt: float) -> None:
        self.last_updated += dt
        self.check_x_bounds()
        for list in self.grid:
            for object in list:
                object.update(dt)

    def render(self, context):
        for list in self.grid:
            for object in list:
                object.render(context)
