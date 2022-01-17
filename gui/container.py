from __future__ import annotations
from uuid import uuid4


from systems.gameObjects import Selectable

__all__ = ["GuiContainer"]


class GuiContainer:
    def __init__(self, pos: tuple[int, int], margin: int = 0, *args, **kwargs) -> None:
        self.id = uuid4()
        self.container: list[Selectable] = []
        self.pos: tuple[int, int] = pos
        self.right_align: bool = kwargs.get("right_align", False)
        self.vertical: bool = kwargs.get("horizontal", True)
        self.margin: int = margin

        for obj in args:
            self.append(*obj)

        for obj in self.container:
            print(obj)
        self.capture_events: callable = lambda event: self.apply_method("capture_events", event)
        self.update: callable = lambda dt: self.apply_method("update", dt)
        self.render: callable = lambda context: self.apply_method("render", context)

    def apply_method(self, method, *args):
        for obj in self.container:
            getattr(obj, method)(*args)

    def find_biggest(self) -> int:
        if len(self.container) > 1:
            biggest = 0
            for obj in self.container:
                if obj.width > biggest:
                    biggest = obj.width
            return biggest
        else:
            return 0

    def append(self, __object: Selectable, *args) -> None:
        obj: Selectable = __object(*args)

        if len(self.container) > 0:
            if self.vertical:
                prev = self.container[-1]
                diff = prev.pos.y + prev.height + self.margin - obj.pos.y
                obj.move_ip(0, diff)
            else:
                prev = self.container[-1]
                diff = prev.pos.x + prev.width + self.margin - obj.pos.x
                obj.move_ip(diff, 0)

        if self.right_align:
            biggest = self.find_biggest()
            for obj in self.container:
                if obj.width < biggest:
                    obj.move_ip(biggest - obj.width, 0)
        self.container.append(obj)
