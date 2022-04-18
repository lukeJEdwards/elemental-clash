from typing import Type
from pygame.event import Event

from components.base import Size
from components.Objects import GuiInteractable, Screen
from components.objectPools import objectPool

from systems.player import Player
from systems.settings import SETTINGS

from utils.functions import apply_method


"""
Main state for everything in the game

screen_stack: lsit of all screen been to, this makes going back alot easier
obj_pool: all objects on screen par from notifications
notification_pool: all nofications on screen

players: list of the players and all data they need
player_selection: flag used for the selection screen
"""

class gameState:
    def __init__(self):
        self.screen_stack: list[Screen] = []
        self.obj_pool: objectPool = objectPool()
        self.notification_pool: list[GuiInteractable] = []

        self.players:list[Player] = [Player(name="Player 1"), Player("Player 2")]
        self.player_selection: bool = False
        self.game_start:bool = False

    # top screen and the current screen being rendered
    def get_top(self) -> Screen:
        return self.screen_stack[-1]

    # used for back button
    def back(self) -> None:
        self.screen_stack.pop()
        self.obj_pool.update(self.get_top().fill_pool())

    # used for changing screen
    def change_state(self, screen_class: Type[Screen]) -> None:
        new_screen: Screen = screen_class(Size(*SETTINGS["SIZE"]))
        self.screen_stack.append(new_screen)
        self.obj_pool.reset(new_screen.load_pool())

    # updates all objects
    def update(self, dt: float) -> None:
        apply_method(self.notification_pool, "update", dt)
        for __id in self.obj_pool.update_pool:
            self.obj_pool[__id].update(dt)

    # pass events to all objects
    def capture_events(self, event: Event) -> None:
        apply_method(self.notification_pool, "capture_events", event)
        for __id in self.obj_pool.event_pool:
            self.obj_pool[__id].capture_events(event)


GAME_STATE: gameState = gameState()
