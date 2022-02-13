from os import listdir
from os.path import isfile, join

from pygame import K_a, K_d, Surface, key

from components.base import Location, Point, Size
from utils.constants import characterType, characterState
from utils.functions import load_image
from utils.paths import assetsDirs


def load_sprites_arrays(character_type: characterType) -> dict[list]:
    path = f"{assetsDirs.CHARACTER_FILES}\\{character_type}\\idle"
    return {characterState.IDLE: [load_image(f) for f in listdir(path) if isfile(join(path, f))]}


class Character(Location):
    def __init__(self, pos: Point, character_type: characterType) -> None:
        self.character_type: characterType = character_type
        self.current_index: int = 0
        self.state: characterState = characterState.IDLE
        self.sprite_dict: dict[list] = load_sprites_arrays(character_type)
        super().__init__(pos, Size(*self.current_sprite.get_size()))

        self.speed: int = 0
        self.last_updated: int = 0

    @property
    def current_sprite_array(self) -> list[Surface]:
        return self.sprite_dict[self.state]

    @property
    def current_sprite(self) -> Surface:
        return self.current_sprite_array[self.current_index]

    def update(self, dt: float) -> None:
        self.last_updated += dt

        if self.last_updated > 0.1:
            self.current_index = (self.current_index + 1) % len(self.current_sprite_array)

    def key_inputs(self) -> None:
        keys = key.get_pressed()
        self.speed = 0
        if keys[K_d]:
            self.speed += 10
        if keys[K_a]:
            self.speed -= 10

        self.pos.x += self.speed

    def render(self, context: Surface) -> None:
        context.blit(self.current_sprite, self.pos)
