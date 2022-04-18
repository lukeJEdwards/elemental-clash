from typing import Iterable
from sys import exit


from components.base import Point, Size
from components.Objects import RenderObject, Screen, Title

from gui.buttons import MainMenuButton
from gui.notification import Notification
from gui.textInput import TextInput

from screens.CharacterSelection import CharacterSelectionScreen
from systems.stateMachine import GAME_STATE

from utils.constants import BACKGROUND, Colour, notificationType


class MainMenuScreen(Screen):
    def __init__(self, size: Size) -> None:
        super().__init__(size)
        self.player_1 = TextInput(Point(730, 344), "PLAYER 1")
        self.player_2 = TextInput(Point(730, 452), "PLAYER 2")

    @property
    def background(self) -> BACKGROUND:
        return BACKGROUND.MENU_BACKGROUND

    def load_pool(self) -> Iterable | RenderObject:
        return [
            Title(Point(self.width / 2, 100), "ELEMENTAL CLASH", Colour.TITLE),
            MainMenuButton(Point(244, 325), "PLAY", self.play),
            MainMenuButton(Point(244, 443), "EXIT", exit),
            self.player_1,
            self.player_2,
        ]

    def play(self) -> None:
        if len(self.player_1.text) < 1 or len(self.player_2.text) < 1:
            GAME_STATE.notification_pool.append(Notification("Please enter name for both players.", notificationType.ALERT))
            return
        GAME_STATE.players[0].name = self.player_1.text
        GAME_STATE.players[1].name = self.player_2.text
        GAME_STATE.change_state(CharacterSelectionScreen)
