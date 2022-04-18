from pygame import Surface

from components.Objects import RenderObject
from components.base import Point, staticPoint, textObject

from systems.stateMachine import GAME_STATE

from utils.constants import BACKGROUND, Colour
from utils.fonts import FONT_NORMAL_L, FONT_NORMAL_XXL

class floorObject(RenderObject):
    def __init__(self, pos: Point) -> None:
        super().__init__(pos, BACKGROUND.GAME_FLOOR.value)

class ScoreObject(RenderObject):

    def __init__(self, pos:staticPoint, player_index: int):
        super().__init__(pos, Surface((100, 100)))

        self.player_index = player_index
        self.txt_obj = textObject(str(self.score), FONT_NORMAL_L, Colour.WHITE)

    @property
    def score(self) -> int:
        return GAME_STATE.players[self.player_index].hit_count

    def update(self, dt:float) -> None:
        self.txt_obj.update(str(self.score))

    def render(self, context:Surface) -> None:
        context.blit(*self.txt_obj.render(*self.pos))

class winMsg(RenderObject):
    def __init__(self,pos:staticPoint, winner:str, **kwargs) -> None:
        super().__init__(pos, Surface((100, 100)), **kwargs)
        self.txt_obj = textObject(winner, FONT_NORMAL_XXL, Colour.WHITE)

    def render(self, context:Surface) -> None:
        context.blit(*self.txt_obj.render(*self.pos))

