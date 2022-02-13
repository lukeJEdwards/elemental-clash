from typing import Optional, Iterable

import time
from pygame import Surface, image, transform


def get_dt(previous_time: float) -> tuple[float, float]:
    now: float = time.time()
    return (0, now) if previous_time == 0 else (now - previous_time, now)


def scale_image(img: Surface, scale: tuple[int, int]) -> Surface:
    return transform.scale(img, scale)


def load_image(filename: str, scale: Optional[tuple[int, int]] = None) -> Surface:
    img: Surface = image.load(filename).convert_alpha()
    return scale_image(img, scale) if scale else img


def apply_method(__iterator: Iterable, method: str, *args):
    for __obj in __iterator:
        getattr(__obj, method)(*args)


def get_center(pos: tuple[int, int], size: tuple[int, int]) -> tuple[int, int]:
    return pos[0] - size[0] // 2, pos[1] - size[1] // 2
