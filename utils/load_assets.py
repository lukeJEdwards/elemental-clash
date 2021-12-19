from typing import Optional
from json import load, dump
from pygame import Surface, image, transform

from utils.paths import relitive_path, assetsDirs

__all__ = ['scale_image', 'scale_image_2x', 'load_image', 'load_background', 'json_file_handler']

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
    img = image.load(filename).convert_alpha()
    if scale:
        img = scale_image(img, scale)
    return img

def load_background(filename:str, size:tuple) -> Surface:
    """Loads a background image.

    Args:
        filename (str): The name of the file to be loaded.

    Returns:
        Surface: The loaded background image.
    """
    return load_image(relitive_path(assetsDirs.BACKGROUNDS, 'menu-background.png'), size)


def json_file_handler(path:str, data:Optional[dict]=None) -> dict:
    """Either saves or loads a json file.

    Args:
        path (str): Path to the file.
        data (Optional[dict], optional): The data being saved. Defaults to None.

    Returns:
        dict: The loaded data or data passed in to be saved.
    """
    try:
        with open(path, 'w' if data else 'r') as file:
            if data:
                dump(data, file, sort_keys=True, ensure_ascii=False, indent=2)
            else:
                data = load(file)
        file.close()
        return data
    except:
        print('json file not found:', path)
        