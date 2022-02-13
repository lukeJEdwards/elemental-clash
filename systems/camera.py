from pygame import Vector2


class camera:
    def __init__(self, player):
        self.player = player
        self.offset = Vector2(0, 0)
        self.offset_float = Vector2(0, 0)

        self.DISPLAY_W, self.DISPLAY_H = 0, 0
        self.const = Vector2(-self.DISPLAY_W / 2 + self.player.width / 2, -self.player.ground + 20)

    def scroll(self):
        self.offset_float.x += self.player.pos.x - self.offset_float.x + self.const.x
        self.offset_float.y += self.player.pos.y - self.offset_float.y + self.const.y
        self.offset.x, self.offset.y = int(self.offset_float.x), int(self.offset_float.y)
        self.offset.x = max(self.player.left_border, self.offset.x)
        self.offset.x = min(self.offset.x, self.player.right_border - self.DISPLAY_W)
