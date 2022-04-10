from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterable


from components.base import Size
from components.objects import RenderObject
from utils.constants import BACKGROUND, SCREEN



@dataclass
class Screen(ABC):
    size:Size
    tag: SCREEN

    @property
    @abstractmethod
    def background(self) -> BACKGROUND:
        pass

    @property
    @abstractmethod
    def switch_screen(self) -> SCREEN:
        pass

    @abstractmethod
    def load_pool(self) -> Iterable[RenderObject]:
        pass