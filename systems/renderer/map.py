"""
TODO:
    - Have a list of collidables tiles
    - render list for the tiles
    - way to load map from file
    - to update map to different file
"""

from pygame import Surface

__all__ = ['TileMap']

class TileMap:
    def __init__(self, filename):
        self.filename = filename
        
    def render(self, context:Surface) -> None:
        pass