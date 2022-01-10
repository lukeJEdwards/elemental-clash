
__all__ = ['get_dt', 'scale_image_2x', 'scale_image', 'load_image', 'load_images', 'load_background']

import time
from typing import Optional
from pygame import Surface, image, transform

from utils.paths import assetsDirs

# get delta time (change in time from last time being called)
def get_dt(previous_time:float) -> tuple[float, float]:
    now:float = time.time()
    return (0, now) if previous_time < 0 else (now - previous_time, now)

# scale pygame surface by 2x
def scale_image_2x(img:Surface) -> Surface: return transform.scale2x(img)

# scale pygame surface by the scale passed in
def scale_image(img:Surface, scale:tuple[int, int]) -> Surface: return transform.scale(img, scale)

# load image in and if scale passed then scales image
def load_image(filename:str, scale:Optional[tuple[int, int]] = None) -> Surface:
    img:Surface = image.load(filename).convert_alpha()
    return scale_image(img, scale) if scale else img

# loads mutiple images at once
def load_images(filenames:list[str]|tuple[str], scales:Optional[tuple[tuple[int, int], ...]] = None) -> tuple[Surface, ...]:
    if scales == None:
        scales = tuple([None for x in range(len(filenames))])
    return tuple(map(lambda filename, scale: load_image(filename, scale), filenames, scales))

# loads background image from background directory
def load_background(filename:str, *args) -> Surface: return load_image(f'{assetsDirs.BACKGROUNDS}\\{filename}', *args)

