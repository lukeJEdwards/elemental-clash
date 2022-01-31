from gui.buttons import BackButton, ReadyButton
from gui.characterIcons import CharacterIcon, ChosenCharacterIcon
from gui.container import GuiContainer
from gui.textInput import TextInput
from server import SERVER, CLIENT

from systems.screen import Screen
from systems.stateMachine import GAME_STATE, SCREEN_STATE

from utils.constants import MENU_BACKGROUND, characterType

__all__ = ["CharacterSelectionScreen"]


def exit_server():
    CLIENT.disconnect()

    if GAME_STATE._server_running:
        GAME_STATE._server_running = False


class CharacterSelectionScreen(Screen):
    def __init__(self, size: tuple[int, int]):
        super().__init__(size, MENU_BACKGROUND)

    def fill_pool(self) -> None:
        SCREEN_STATE._current_pool.append(
            [
                GuiContainer(
                    (165, 194),
                    100,
                    (CharacterIcon, characterType.FIRE),
                    (CharacterIcon, characterType.EARTH),
                    horizontal=True,
                ),
                GuiContainer(
                    (165, 397),
                    100,
                    (CharacterIcon, characterType.WATER),
                    (CharacterIcon, characterType.AIR),
                    horizontal=True,
                ),
                GuiContainer(
                    (704, 226),
                    15,
                    (TextInput, "", GAME_STATE._player_data["1"]["name"], True),
                    (ChosenCharacterIcon, "1"),
                    horizontal=True,
                ),
                GuiContainer(
                    (704, 429),
                    15,
                    (TextInput, "", GAME_STATE._player_data["2"]["name"], True),
                    (ChosenCharacterIcon, "2"),
                    horizontal=True,
                ),
                ReadyButton((724, 585)),
                BackButton((20, 20), exit_server),
            ]
        )
