from __future__ import annotations
from uuid import UUID

from pygame import Surface
from systems.gameObjects import GameObject

__all__ = ["ObjectPool"]


class ObjectPool:
    def __init__(self, *args: GameObject) -> None:
        self.object_pool: dict[UUID, GameObject] = {obj.id: obj for obj in args}
        self.keys = list(self.object_pool.keys())
        self.iter = -1

    def __getitem__(self, id: str) -> GameObject:
        return self.object_pool[id]

    def __setitem__(self, id: str, obj: GameObject) -> None:
        self.object_pool[id] = obj
        self.keys = list(self.object_pool.keys())

    def __iter__(self) -> ObjectPool:
        return self

    def __next__(self) -> GameObject:
        self.iter += 1
        if self.iter < len(self.keys):
            return self.object_pool[self.keys[self.iter]]
        self.iter = -1
        raise StopIteration
