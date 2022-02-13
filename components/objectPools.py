from __future__ import annotations
from typing import Iterator, Iterable
from uuid import UUID

from components.objects import RenderObject


class objectPool:
    def __init__(self) -> None:
        self.pool: dict[UUID, RenderObject] = {}
        self.keys: list[UUID] = []
        self.update_pool: list[UUID] = []
        self.event_pool: list[UUID] = []

        self._len: int = len(self.pool)
        self._iter: int = -1

    def _clear(self) -> None:
        self.pool.clear()
        self.keys.clear()
        self.update_pool.clear()
        self.event_pool.clear()
        self._len = 0

    def reset(self, __iter: Iterable[RenderObject]) -> None:
        self._clear()
        for __obj in __iter:
            self._len += 1
            self.pool[__obj.id] = __obj
            self._sort_obj(__obj)

    def _sort_obj(self, __obj: RenderObject) -> None:
        self.keys.append(__obj.id)
        if "update" in dir(__obj):
            self.update_pool.append(__obj.id)

        if "capture_events" in dir(__obj):
            self.event_pool.append(__obj.id)

    def __str__(self) -> str:
        _str: str = ""
        for __obj in self.pool.values():
            _str += __obj.__str__()
        return _str

    def __len__(self) -> int:
        return self._len

    def __iter__(self) -> Iterator[objectPool]:
        return self

    def __getitem__(self, __k: UUID) -> RenderObject:
        return self.pool[__k]

    def __next__(self) -> RenderObject:
        self._iter += 1
        if self._iter < self._len:
            return self.pool[self.keys[self._iter]]
        self._iter = -1
        raise StopIteration
