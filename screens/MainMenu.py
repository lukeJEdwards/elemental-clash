from typing import Iterable
from sys import exit
from _thread import start_new_thread


from components.base import Point, Size
from components.objects import RenderObject, Screen, Title

from gui.buttons import MainMenuButton
from gui.notification import Notification
from gui.textInput import TextInput

from screens.CharacterSelection import CharacterSelectionScreen
from server.client import CLIENT
from server.server import IP, SERVER
from systems.stateMachine import GAME_STATE

from utils.constants import BACKGROUND, Colour, notificationType


class MainMenuScreen(Screen):
    def __init__(self, size: Size) -> None:
        super().__init__(size)
        self.name = TextInput(Point(730, 344), "ENTER NAME")
        self.ip = TextInput(Point(730, 452), "ENTER IP")

    @property
    def background(self) -> BACKGROUND:
        return BACKGROUND.MENU_BACKGROUND

    def load_pool(self) -> Iterable | RenderObject:
        return [
            Title(Point(self.width / 2, 100), "ELEMENTAL CLASH", Colour.TITLE),
            MainMenuButton(Point(244, 245), "CONNECT", self.connect_to_server),
            MainMenuButton(Point(244, 381), "START SERVER", self.start_local_server),
            MainMenuButton(Point(244, 517), "EXIT", exit),
            self.name,
            self.ip,
        ]

    def connect(self, ip: str) -> None:
        players = CLIENT.connect(ip)
        if players:
            GAME_STATE.connected = True
            GAME_STATE.server_ip = ip
            GAME_STATE.player_name = self.name.text
            GAME_STATE.change_state(CharacterSelectionScreen)
        else:
            GAME_STATE.notification_pool.append(Notification("Could not connect!", notificationType.ERROR))

    def connect_to_server(self) -> None:
        if self.name.text and self.ip.text:
            GAME_STATE.index = 1
            self.connect(self.ip.text)
        else:
            GAME_STATE.notification_pool.append(Notification("No IP address or Name", notificationType.ALERT))

    def start_local_server(self) -> None:
        if self.name.text:
            GAME_STATE.index = 0
            GAME_STATE.run_server()
            start_new_thread(SERVER.run, ())
            self.connect(IP)
        else:
            GAME_STATE.notification_pool.append(Notification("please fill in your name", notificationType.ALERT))
