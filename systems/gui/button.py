
__all__ = ['MenuButton']


from utils import load_image, scale_image_2x, assetsDirs, WHITE, FONT_NORMAL_L

from systems.renderer import render_text
from systems.gameObjects import RenderObject, SelectableGuiObject


class MenuButton(RenderObject, SelectableGuiObject):
    def __init__(self, pos:list[int, int], text:str, call_back:callable):
        DEFAULT_SPRITE = scale_image_2x(load_image(f'{assetsDirs.UI.BUTTONS}\\menu-button.png'))
        ACTIVE_SPRITE = scale_image_2x(load_image(f'{assetsDirs.UI.BUTTONS}\\menu-button-active.png'))
        super().__init__(pos=pos, sprite=DEFAULT_SPRITE, default_sprite=DEFAULT_SPRITE, active_sprite=ACTIVE_SPRITE)
        
        self.text:str = text
        self.call_back:callable = call_back
        self.last_updated:float = 0
        self.moving_up:bool = True
        self.o_pos:tuple[int, int] = tuple(pos)
        
    def call(self) -> None: self.call_back()
        
    def update(self, dt:float) -> None:
        offset = 3
        self.last_updated += dt
        
        if not self.is_active and tuple(self.pos) != self.o_pos: self.pos = self.o_pos
        
        if self.last_updated > .06 and self.is_active:
            self.last_updated = 0
            self.pos[1] = self.pos[1] + 1 if self.moving_up else self.pos[1] - 1
            if self.pos[1] == self.o_pos[1] + offset: self.moving_up = False
            if self.pos[1] == self.o_pos[1] - offset: self.moving_up = True
        
        
    def render(self, context):
        self.change_sprite(self.get_current_sprite())
        render_text(self.current_sprite, FONT_NORMAL_L, self.text, WHITE, (self.width//2, self.height//2))
        context.blit(self.current_sprite, self.get_center())
        
        
        