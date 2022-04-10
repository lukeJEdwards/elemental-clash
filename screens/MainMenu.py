from dataclasses import dataclass

from components.base import Size, Vec2
from components.objects import RenderObject

from screens.screen import Screen

from ui.button import Button

from utils.constants import BACKGROUND, SCREEN

@dataclass
class MainMenu(Screen):
    size:Size
    tag: SCREEN = SCREEN.MENU

    next_screen: bool = False
    exit: bool = False


    @property 
    def background(self) -> BACKGROUND:
        return BACKGROUND.MENU_BACKGROUND

    @property
    def switch_screen(self) -> SCREEN:
        if self.next_screen:
            return SCREEN.SELECTION
        if self.exit:
            return SCREEN.CLOSE
            
        return self.tag

    def load_pool(self) -> list[RenderObject]:
        return [Button(Vec2(self.size.width//2, self.size.height//2), 'PLAY')]