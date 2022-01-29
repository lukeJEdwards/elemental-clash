from __future__ import annotations
from re import T
from typing import Iterable

from components.objects import GuiInteractable, GuiObject
from utils.functions import apply_method


class GuiContainer:
    def __init__(self, pos: tuple[int, int], margin: int = 0, *args, **kwargs):
        super().__init__()

        self.pos: tuple[int, int] = pos
        self._margin: int = margin
        self._horizontal: bool = kwargs.get("horizontal", False)
        self._center: bool = kwargs.get("center", False)
        self._right_align: bool = kwargs.get("right_align", False)

        self._container: list[GuiObject] = []
        self._len: int = 0
        self._iter: int = -1

        self.update: callable = lambda dt: apply_method(self._container, "update", dt)
        self.capture_events: callable = lambda event: apply_method(self._container, "capture_events", event)

        for __obj in args:
            self.append(*__obj)

    def get_size(self):
        prev = self._container[-1]
        return (self.pos[0] - prev.pos[0]) + prev.size[0] + self._margin

    def append(self, __obj_class: T | Iterable[T], *args) -> None:
        if isinstance(__obj_class, Iterable):
            self._container.extend(list(map(lambda obj: self.append(obj), __obj_class)))
        else:
            __obj: GuiObject = __obj_class(self.pos, *args, center=self._center)

            if self._len > 0:
                prev = self._container[-1]
                if self._horizontal:
                    __obj.pos.x += (prev.pos[0] - self.pos[0]) + prev.size[0] + self._margin
                else:
                    __obj.pos.y += (prev.pos[1] - self.pos[1]) + prev.size[1] + self._margin

            if self._right_align:
                __obj.pos.x -= __obj.size[0] // 2

            try:
                getattr(__obj, "rect")
                assert isinstance(__obj, GuiInteractable)
                __obj.rect.move_ip(__obj.pos.x - __obj.rect.x, __obj.pos.y - __obj.rect.y)
                __obj.orginal_pos = (int(__obj.pos.x), int(__obj.pos.y))
            except AttributeError:
                pass

            self._container.append(__obj)
            self._len += 1

    def __str__(self) -> str:
        _str: str = ""
        for __obj in self._container:
            _str += __obj.__str__()
        return _str

    def __len__(self):
        return self._len

    def __iter__(self) -> GuiContainer:
        return self

    def __next__(self) -> GuiObject:
        self._iter += 1
        if self._iter < self._len:
            return self._container[self._iter]
        self._iter = -1
        raise StopIteration
