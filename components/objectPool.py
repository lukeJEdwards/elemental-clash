from __future__ import annotations
from dataclasses import dataclass, field
from typing import SupportsIndex

from components.objects import RenderObject

from utils.constants import TAG

@dataclass
class ObjectPool:

    objects: dict[str, RenderObject] = field(default_factory=dict)
    render_order: dict[TAG, list[str]] = field(default_factory= lambda: {tag: [] for tag in TAG})
    __iter: int = -1

    def __getitem__(self, __i: SupportsIndex) -> RenderObject:
        return self.objects[__i]

    def __iter__(self) -> ObjectPool:
        return self

    def __next__(self) -> RenderObject:
        self.__iter += 1
        if self.__iter < len(self.objects):
            return self.objects.values()[self.__iter]
        self.__iter = -1
        raise StopIteration

    def set_objs(self, objects: list[RenderObject]) -> None:
        self.objects = {}
        self.render_order = {tag: [] for tag in TAG}

        for __obj in objects:
            self.objects[__obj.id] = __obj
            self.render_order[__obj.tag].append(__obj.id)