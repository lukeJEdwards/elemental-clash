from __future__ import annotations
from typing import Iterable, NamedTuple, SupportsIndex

from dataclasses import dataclass, field
from uuid import UUID, uuid4


from pygame import Rect, Surface
from pygame.font import Font

from utils.constants import Colour
from utils.fonts import FONT_NORMAL_L


@dataclass
class iterator:
    """
        Class to add iteration to an object
    """
    iter: Iterable
    __iter: int = -1

    def __getitem__(self, __i: SupportsIndex) -> int:
        return self.iter[__i]

    def __setitem__(self, __i: SupportsIndex, value: int) -> None:
        self.iter[__i] = value

    def __iter__(self) -> Point:
        return self

    def __next__(self) -> int:
        self.__iter += 1
        if self.__iter < len(self.iter):
            return self.iter[self.__iter]
        self.__iter = -1
        raise StopIteration


class staticPoint(NamedTuple):
    """
        makes using tuple nice as index [0] and [1] are now named
        to X and Y respectively
    """
    x: int
    y: int


class Point(iterator):
    """
        Point of screen
    """
    def __init__(self, x=0, y=0):
        super().__init__([x, y])

    @property
    def x(self) -> float:
        return self.iter[0]

    @x.setter
    def x(self, value: float):
        self.iter[0] = value

    @property
    def y(self) -> float:
        return self.iter[1]

    @y.setter
    def y(self, value: float):
        self.iter[1] = value

    def move_ip(self, __x: float, __y: float) -> None:
        self.x += __x
        self.y += __y

    def update(self, __x: float, __y: float) -> None:
        self.x, self.y = __x, __y

    def toTuple(self) -> tuple[float, float]:
        return (self.x, self.y)


class Size(iterator):
    """
        Used for sizes
    """
    def __init__(self, width: float, height: float) -> None:
        super().__init__([width, height])

    @property
    def width(self) -> float:
        return self.iter[0]

    @width.setter
    def width(self, value: float) -> None:
        self.size[0] = value

    @property
    def height(self) -> float:
        return self.iter[1]

    @height.setter
    def height(self, value: float) -> None:
        self.iter[1] = value

    def update(self, __width: float, __height: float) -> None:
        self.width += __width
        self.height += __height

    def toTuple(self) -> tuple[float, float]:
        return (self.width, self.height)


class Location:
    """
        Adds properties that point to the loaction
    """
    def __init__(self, pos: Point, **kwargs) -> None:
        super().__init__(**kwargs)
        self.pos: Point = pos

    @property
    def x(self) -> int:
        return self.pos.x

    @property
    def y(self) -> int:
        return self.pos.y

    def __repr__(self) -> str:
        return f"Location(pos={repr(self.pos)})"


class Dimension:
    """
        Adds properties that point to the size
    """
    def __init__(self, size: Size, **kwargs) -> None:
        super().__init__(**kwargs)
        self.size = size

    @property
    def width(self) -> int:
        return self.size.width

    @property
    def height(self) -> int:
        return self.size.height

    def __repr__(self) -> str:
        return f"Dimension(size={repr(self.size)})"


@dataclass
class textObject:
    """
        For rendering any text in screen
    """
    text: str
    font: Font
    colour: Colour
    alpha: int = 255
    id:UUID = uuid4()

    def update(self, text: str) -> None:
        self.text = text

    def render(self, x: int, y: int) -> tuple[Surface, Rect]:
        surf = self.font.render(self.text, True, self.colour.value)
        surf.set_alpha(self.alpha)
        rect = surf.get_rect()
        rect.center = (x, y + 4)
        return (surf, rect)
