import time
from typing import Optional, Iterable, overload
from pygame import Surface, image, transform

from components.base import Size, Vec2


def get_dt(previous_time: float) -> tuple[float, float]:
    now: float = time.time()
    return (0, now) if previous_time == 0 else (now - previous_time, now)



@overload
def load_image(filename: str, scale: int) -> Surface:...

@overload
def load_image(filename: str, scale: tuple[int, int]) -> Surface:...

@overload
def load_image(filename: str) -> Surface:...


def load_image(*args) -> Surface:
    img: Surface = image.load(args[0]).convert_alpha()
    
    if args[1]:
        return transform.scale2x(img) if isinstance(args[1], int) else transform.scale(img, args[1])

    return img

def apply_method(__iterator: Iterable, method: str, *args):
    for __obj in __iterator:
        getattr(__obj, method)(*args)


def get_center(pos: Vec2, size: Size) -> tuple[int, int]:
    return pos.x - size.width // 2, pos.y - size.height // 2
