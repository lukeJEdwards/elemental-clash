from typing import Iterable
from components.Objects import RenderObject, Screen
from components.base import Size, staticPoint
from components.gameObjects import winMsg
from systems.stateMachine import GAME_STATE
from utils.constants import BACKGROUND


class WinScreen(Screen):
    def __init__(self, size: Size):
        super().__init__(size)

    @property
    def background(self) -> BACKGROUND:
        return BACKGROUND.WIN

    @property
    def get_winner(self) -> str:
        return GAME_STATE.players[0].name if GAME_STATE.players[0].hit_count == 5 else GAME_STATE.players[1].name

    def load_pool(self) -> Iterable[RenderObject]:
        return [
            winMsg(staticPoint(640, 360), f'{self.get_winner} IS THE WINNER!')
        ]