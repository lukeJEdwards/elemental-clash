from typing import Optional
from os import getcwd, path
from pygame import Surface, image, transform

from utils.constants import SIZE

CWD:str = getcwd() 
"""the current working directory"""

def relitive_path(*paths:list[str]) -> str: 
    return path.join(CWD, *paths)

def scale_image(img:Surface, scale:tuple|int) -> Surface:
    """scales the image by scale argument.

    Args:
        img (Surface): The image to be scaled.
        scale (tuple): [description]

    Returns:
        Surface: The scaled image.
    """
    if scale == 2:
        return scale_image_2x(img)
    else:
        return transform.scale(img, scale)
    
def scale_image_2x(img:Surface) -> Surface:
    """Scales the image by 2x.

    Args:
        img (Surface): The image to be scaled.

    Returns:
        Surface: The scaled image.
    """
    return transform.scale2x(img)

def load_image(filename:str, scale:Optional[tuple|int] = None) -> Surface:
    """loads an image from a file.

    Args:
        filename (str): The name of the file to be loaded.
        scale (Optional[tuple, optional): When loading the image you can choise to scale it stright away. Defaults to None.

    Returns:
        Surface: [description]
    """
    img = image.load(relitive_path(filename)).convert_alpha()
    if scale:
        img = scale_image(img, scale)
    return img

def load_background(filename:str) -> Surface:
    """Loads a background image.

    Args:
        filename (str): The name of the file to be loaded.

    Returns:
        Surface: The loaded background image.
    """
    return load_image(f'assets\\backgrounds\\{filename}', SIZE)
        