from __future__ import annotations
from typing import Iterator, Iterable
from uuid import UUID

from components.Objects import RenderObject


class objectPool:
    def __init__(self, __iterable: Iterable[RenderObject] = []):
        self._pool: dict[UUID, RenderObject] = {obj.id: obj for obj in __iterable}
        self._keys: list[UUID] = list(self._pool.keys())
        self._len: int = len(self._pool)
        self._iter: int = -1

    def append(self, __obj: RenderObject | Iterable[RenderObject]) -> None:
        if isinstance(__obj, RenderObject):
            self.__setitem__(__obj.id, __obj)
        elif isinstance(__obj, Iterable):
            for obj in __obj:
                self.append(obj)

    def clear(self) -> None:
        self._pool.clear()
        self._keys.clear()

    def update(self, __pool: objectPool) -> None:
        self._pool = __pool._pool.copy()
        self._keys = __pool._keys.copy()

    def __str__(self):
        _str: str = ""
        for __obj in self._pool.values():
            _str += __obj.__str__()
        return _str

    def __len__(self) -> int:
        return self._len

    def __iter__(self) -> Iterator[objectPool]:
        return self

    def __getitem__(self, __k: UUID) -> RenderObject:
        return self._pool[__k]

    def __setitem__(self, __k: UUID, __obj: RenderObject) -> None:
        self._pool[__k] = __obj
        self._keys.append(__k)
        self._len += 1

    def __next__(self) -> RenderObject:
        self._iter += 1
        if self._iter < self._len:
            return self._pool[self._keys[self._iter]]
        self._iter = -1
        raise StopIteration
