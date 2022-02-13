from typing import Type
from pygame.event import Event
from components.base import Size

from components.objects import GuiInteractable, Screen
from components.objectPools import objectPool

from server.player import Player
from systems.settings import SETTINGS

from utils.constants import characterType
from utils.functions import apply_method


class gameState:
    def __init__(self):
        self.screen_stack: list[Screen] = []
        self.obj_pool: objectPool = objectPool()
        self.notification_pool: list[GuiInteractable] = []

        self.server_running: bool = False
        self.connected: bool = False

        self.server_ip: str = ""

        self.player: Player = Player()
        self.opponent: Player = Player()

    @property
    def player_character(self) -> characterType:
        return self.player.character

    @player_character.setter
    def player_character(self, character: characterType):
        self.player.character = character

    @property
    def player_name(self) -> str:
        return self.player.name

    @player_name.setter
    def player_name(self, name: str) -> None:
        self.player.name = name

    @property
    def player_ready(self) -> bool:
        return self.player.ready

    @player_ready.setter
    def player_ready(self, ready: bool):
        self.player.ready = ready

    @property
    def opponent_name(self) -> str:
        return self.opponent.name

    @property
    def opponent_character(self) -> characterType:
        return self.opponent.character

    @property
    def opponent_ready(self) -> bool:
        return self.opponent.ready

    @property
    def game_ready(self) -> bool:
        return self.player_ready and self.opponent_ready

    def run_server(self):
        self.server_running = True

    def stop_server(self):
        self.server_running = False

    def get_top(self) -> Screen:
        return self.screen_stack[-1]

    def back(self) -> None:
        self.screen_stack.pop()
        self.obj_pool.update(self.get_top().fill_pool())

    def change_state(self, screen_class: Type[Screen]) -> None:
        new_screen: Screen = screen_class(Size(*SETTINGS["SIZE"]))
        self.screen_stack.append(new_screen)
        self.obj_pool.reset(new_screen.load_pool())

    def update(self, dt: float) -> None:
        apply_method(self.notification_pool, "update", dt)
        for __id in self.obj_pool.update_pool:
            self.obj_pool[__id].update(dt)

    def capture_events(self, event: Event) -> None:
        apply_method(self.notification_pool, "capture_events", event)
        for __id in self.obj_pool.event_pool:
            self.obj_pool[__id].capture_events(event)


GAME_STATE: gameState = gameState()
