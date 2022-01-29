from typing import Optional
from json import load, dump
from pygame import Surface, image, transform

from utils.paths import assetsDirs

__all__ = ['scale_image', 'scale_image_2x', 'load_image', 'load_background', 'json_file_handler']

def scale_image(img:Surface, scale:tuple|int) -> Surface:
    if scale == 2: return scale_image_2x(img)
    else: return transform.scale(img, scale)
    
def scale_image_2x(img:Surface) -> Surface: return transform.scale2x(img)

def load_image(filename:str, scale:Optional[tuple|int] = None) -> Surface:
    img = image.load(filename).convert_alpha()
    if scale: img = scale_image(img, scale)
    return img

def load_background(filename:str, size:tuple) -> Surface: return load_image(f'{assetsDirs.BACKGROUNDS}\\{filename}', size)


def pererve_tuple(obj):
    if '__tuple__' in obj:
        return tuple(obj['obj'])
    else:
        return obj

def json_file_handler(path:str, data:Optional[dict]=None) -> dict:
    try:
        with open(path, 'w' if data else 'r') as file:
            if data:
                dump(data, file, sort_keys=True, ensure_ascii=False, indent=2)
            else: data = load(file, object_hook=pererve_tuple)
        file.close()
        return data
    except: print('json file not found:', path)
        