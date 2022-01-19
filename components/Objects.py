from pygame import Surface, Vector2


class renderObject:
    def __init__(self, pos: tuple[int, int], sprite: Surface, **kwargs):
        super().__init__(**kwargs)
        self.pos: Vector2 = Vector2(self.get_center(pos, sprite) if kwargs.get("centre", False) else pos)
        self.current_sprite: Surface = sprite
        self.size: tuple[int, int] = sprite.get_size()
        self.width: int = self.size[0]
        self.height: int = self.size[1]

    def get_center(self, pos: tuple[int, int], sprite: Surface) -> tuple[int, int]:
        size = sprite.get_size()
        return pos[0] + size[0] // 2, pos[1] + size[1] // 2

    def redner(self, context: Surface):
        context.blit(self.current_sprite, self.pos)
