from dataclasses import dataclass, field
from uuid import uuid4

from pygame import Rect, Surface, mouse
from pygame.constants import MOUSEBUTTONDOWN
from pygame.event import Event

from components.base import Size, Vec2
from utils.constants import TAG


@dataclass
class RenderObject:
    tag: TAG
    pos: Vec2
    size: Size
    current_sprite: Surface
    id:str = field(default_factory=lambda: uuid4().hex)

    def render(self, context:Surface) -> None:
        context.blit(self.current_sprite, self.pos.to_tuple())

@dataclass
class AnimationObject:
    sprites:list[Surface]
    current_index:int = 0

    @property
    def current_sprite(self) -> Surface:
        return self.sprites[self.current_index]

    def get_react(self) -> Rect:
        return self.current_sprite.get_rect()

    def next_sprite(self) -> None:
        self.current_index += 1

@dataclass
class UpdateObject(RenderObject):
     
    def move_ip(self, x:float, y:float):
        self.pos.x += x
        self.pos.y += y

    def update(self, dt:float):
        pass

class EventObject(UpdateObject):
    def __init__(self, tag: TAG, pos: Vec2, size: Size, current_sprite: Surface):
        super().__init__(tag, pos, size, current_sprite)

        self.rect: Rect = self.current_sprite.get_rect()


    def move_ip(self, x:float, y:float) -> None:
        super().move_ip(x, y)
        self.rect.move_ip(x, y)

    def collision(self, location:Rect|Vec2) -> bool:
        return self.rect.colliderect(location) if isinstance(location, Rect) else self.rect.collidepoint(location)

    def capture_event(self, event:Event) -> None:
        pass

@dataclass
class GUIInteractable(EventObject):

    @property
    def hovering(self) -> bool:
        return self.rect.collidepoint(mouse.get_pos())

    @property
    def clicked(self, event:Event) -> bool:
        return self.hovering and event.type == MOUSEBUTTONDOWN