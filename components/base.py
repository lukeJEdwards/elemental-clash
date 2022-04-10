from __future__ import annotations
from re import T
from typing import Iterable, SupportsIndex, overload

from dataclasses import dataclass


@dataclass
class iterator:
    __iterable: Iterable[T]
    __iter: int = -1

    def __getitem__(self, __i: SupportsIndex) -> int:
        return self.__iterable[__i]

    def __setitem__(self, __i: SupportsIndex, value: int) -> None:
        self.__iterable[__i] = value

    def __iter__(self) -> T:
        return self

    def __next__(self) -> int:
        self.__iter += 1
        if self.__iter < len(self.__iterable):
            return self.__iterable[self.__iter]
        self.__iter = -1
        raise StopIteration

    def to_tuple(self) -> tuple[T, ...]:
        return tuple(self.__iterable)

class Size(iterator):

    @overload
    def __init__(self, width: int, height: int) -> None:...
    @overload
    def __init__(self, size: tuple[int, int]):...

    def __init__(self, *args) -> None:
        super().__init__(tuple(args))


    @property
    def width(self) -> int:
        return self[0]

    @property
    def height(self) -> int:
        return self[1]


class Vec2(iterator):

    @overload
    def __init__(self, pos: Iterable) -> None:...
    @overload
    def __init__(self, x:float, y: float) -> None:...

    def __init__(self, *args) -> None:
        super().__init__(list(args))

    @property
    def x(self) -> float:
        return self[0]

    @x.setter
    def x(self, _x:float) -> None:
        self[0] = _x

    @property
    def y(self) -> float:
        return self[1]

    @y.setter
    def x(self, _y:float) -> None:
        self[1] = _y

    


# class staticPoint(NamedTuple):
#     x: int
#     y: int


# class Point(iterator):
#     def __init__(self, x=0, y=0):
#         super().__init__([x, y])

#     @property
#     def x(self) -> int:
#         return self.iter[0]

#     @x.setter
#     def x(self, value: int):
#         self.iter[0] = value

#     @property
#     def y(self) -> int:
#         return self.iter[1]

#     @y.setter
#     def y(self, value: int):
#         self.iter[1] = value

#     def move_ip(self, __x: int, __y: int) -> None:
#         self.x += __x
#         self.y += __y

#     def update(self, __x: int, __y: int) -> None:
#         self.x, self.y = __x, __y

#     def toTuple(self) -> tuple[float, float]:
#         return (self.x, self.y)