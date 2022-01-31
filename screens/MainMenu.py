from typing import Iterable
from _thread import start_new_thread

from components.Objects import RenderObject

from gui.buttons import MainMenuButton
from gui.container import GuiContainer
from gui.notification import Notification
from gui.textInput import TextInput

from screens.CharacterSelection import CharacterSelectionScreen
from server import SERVER, CLIENT

from systems.screen import Screen
from systems.settings import SETTINGS
from systems.stateMachine import GAME_STATE, SCREEN_STATE

from utils.constants import MENU_BACKGROUND, notificationType

__all__ = ["MainMenuScreen"]


def start_sever():
    if not SETTINGS["NAME"]:
        SCREEN_STATE._notification_pool.append(Notification("Please enter a name", notificationType.ALERT))
    else:
        GAME_STATE._server_running = True
        start_new_thread(SERVER.run_server, ())

        failed_connection = CLIENT.connect()
        SETTINGS["IP"] = SERVER.SERVER
        if failed_connection:
            SCREEN_STATE._notification_pool.append(Notification("Connection failed", notificationType.ERROR))
        else:
            SCREEN_STATE.change_state(CharacterSelectionScreen(SETTINGS["SIZE"]))


def connect_to_sever():
    if not SETTINGS["IP"] or not SETTINGS["NAME"]:
        SCREEN_STATE._notification_pool.append(Notification("Please enter a name or IP", notificationType.ALERT))
    else:
        failed_connection = CLIENT.connect(SETTINGS["IP"])
        if failed_connection:
            SCREEN_STATE._notification_pool.append(Notification("Connection failed", notificationType.ERROR))
        else:
            SCREEN_STATE.change_state(CharacterSelectionScreen(SETTINGS["SIZE"]))
            SCREEN_STATE._notification_pool.append(Notification("Connection successful", notificationType.SUCCESS))


class MainMenuScreen(Screen):
    def __init__(self, size: tuple[int, int]):
        super().__init__(size, MENU_BACKGROUND)

    def fill_pool(self) -> Iterable | RenderObject:
        return [
            GuiContainer(
                (312, 242),
                60,
                (MainMenuButton, "START SERVER", start_sever),
                (MainMenuButton, "CONNECT", connect_to_sever),
                (MainMenuButton, "EXIT", exit),
            ),
            GuiContainer(
                (797, 341),
                60,
                (TextInput, "ENTER NAME", "NAME"),
                (TextInput, "ENTER IP", "IP"),
            ),
        ]
