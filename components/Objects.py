from __future__ import annotations
from typing import Optional
from uuid import uuid4
from os import listdir

from pygame import MOUSEBUTTONDOWN, Rect, Surface, Vector2, mouse
from pygame.event import Event

from utils.constants import characterType, characterState
from utils.functions import load_images
from utils.paths import assetsDirs


def get_center(pos: tuple[int, int], size: tuple[int, int]) -> tuple[int, int]:
    return pos[0] - size[0] // 2, pos[1] - size[1] // 2


class RenderObject:
    def __init__(self, pos: tuple[int, int], sprite: Surface, **kwargs) -> None:
        self.id = uuid4()
        self.currrent_sprite: Surface = sprite
        self.size: tuple[int, int] = sprite.get_size()
        self.pos: Vector2 = Vector2(get_center(pos, self.size)) if kwargs.get("center", False) else Vector2(pos)

    def render(self, context: Surface) -> None:
        context.blit(self.currrent_sprite, self.pos)

    def __str__(self) -> str:
        return f"pos:{self.pos}\nsize:{self.size}\n"

class GuiObject(RenderObject):
    def __init__(self, pos: tuple[int, int], sprite: Surface, **kwargs):
        super().__init__(pos, sprite, **kwargs)

    def update(self, dt: float) -> None:
        pass

    def capture_events(self, event: Event) -> None:
        pass

    def __str__(self) -> str:
        return super().__str__()


class GuiInteractable(GuiObject):
    def __init__(self, pos: tuple[int, int], sprite: Surface, active_sprite: Surface, **kwargs):
        super().__init__(pos=pos, sprite=sprite, **kwargs)

        self.rect: Rect = Rect(self.pos, self.size)
        self.default_sprite: Surface = sprite
        self.active_sprite: Surface = active_sprite
        self.orginal_pos: tuple[int, int] = pos
        self.clicked: bool = False

    def is_clicked(self, event: Event) -> bool:
        return event.type == MOUSEBUTTONDOWN and self.is_mouse_hovering()

    def is_mouse_hovering(self) -> bool:
        return self.rect.collidepoint(mouse.get_pos())

    def move_ip(self, x: int, y: int) -> None:
        self.pos.update(self.pos.x + x, self.pos.y + y)
        self.rect.move_ip(x, y)

    def update(self, dt: Optional[float] = 0) -> None:
        self.currrent_sprite = self.active_sprite if self.is_mouse_hovering() else self.default_sprite

    def __str__(self) -> str:
        return super().__str__() + f"{self.rect}\n"

class CharacterObject(RenderObject):
    def __init__(self, character_type:characterType, **kwargs) -> None:
        super().__init__(**kwargs)

        self.rect = Rect(self.size, self.pos)

        self.character_type:characterType = character_type
        self.sprites:dict[characterState, tuple[Surface, ...]] = self.load_moves()

        self.last_updated:float = 0
        self.current_index:int = 0
        self.current_state:characterState = characterState.IDLE
        self.current_sprite:Surface = self.ge_current_state()[0]

    def load_sprites(self, dirname:str) -> tuple[Surface, ...]:
        return load_images(listdir(dirname))

    def load_moves(self) -> dict[characterState, tuple[Surface, ...]]:
        dirs = listdir(f'{assetsDirs.CHARACTER_FILES}\\{self.character_type.value}')
        return {characterState(dir):self.get_sprites(dir) for dir in dirs}

    def get_current_state(self) -> tuple[Surface, ...]:
        return self.sprites[self.currrent_state]

    def change_state(self, state:characterState) -> None:
        self.currrent_state = state
        self.current_index = 0

    def next(self) -> None:
        self.current_index = (self.current_index + 1) % len(self.get_current_state())

    def capture_events(self, event:Event) -> None:
        pass

    def update(self, dt:float) -> None:
        self.last_updated += dt

        if self.last_updated > 0.1:
            self.last_updated =0
            self.next()
