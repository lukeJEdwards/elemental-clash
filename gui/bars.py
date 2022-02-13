from components.base import Point
from components.objects import GuiObject

from utils.constants import BARS


class HealthBar(GuiObject):
    def __init__(self, pos: Point, health: int) -> None:
        super().__init__(pos, BARS.HEALTH.value)
        self.health: int = health


class EnergyBar(GuiObject):
    def __init__(self, pos: Point, energy: int) -> None:
        super().__init__(pos, BARS.ENERGY.value)
        self.energy: int = energy
