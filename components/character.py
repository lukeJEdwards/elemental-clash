import math
from os import listdir
from os.path import isfile, join
from uuid import UUID, uuid4

from pygame import Rect, Surface, transform, math
from pygame.locals import KEYDOWN, KEYUP
from pygame.event import Event

from components.base import staticPoint
from systems.player import Player

from systems.settings import PLAYER_1_KEYS, PLAYER_2_KEYS, SETTINGS, keyMappings
from systems.stateMachine import GAME_STATE

from utils.constants import characterType, characterState
from utils.functions import load_image
from utils.paths import assetsDirs

def load_and_flip(file_path:str, flip:bool) -> Surface:
    return transform.flip(load_image(file_path, (672, 336)), flip, False)

def get_array(character_type: characterType, state: characterState, flip:bool) -> Surface:
    path = f"{assetsDirs.CHARACTER_FILES}\\{character_type.value}\\{state.value}"
    return [load_and_flip(join(path, f), flip) for f in listdir(path) if isfile(join(path, f))]

def load_sprites_arrays(character_type: characterType, flip: bool) -> dict[list]:
    return { state: get_array(character_type, state, flip) for state in characterState }

class Character:
    def __init__(self, pos: staticPoint, player_index: int, facing_left:bool = False) -> None:

        self.id: UUID = uuid4()

        self.player_index: int = player_index

        self.sprites_r:dict[characterState, list[Surface]] = load_sprites_arrays(self.player_info.character, False)
        self.sprites_l:dict[characterState, list[Surface]] = load_sprites_arrays(self.player_info.character, True)

        self.collision_box:Rect = Rect((0,0), (400, 144))

        self.character_state:characterState = characterState.IDLE
        self.current_index: int = 0

        self.last_updated:int = 0

        self.atk_start:bool = False
        self.atk_timer:int = 0

        self.LEFT_KEY, self.RIGHT_KEY, self.FACING_LEFT = False, False, facing_left
        self.is_jumping, self.on_ground = False, False
        self.gravity, self.friction = .35, -.25
        self.position, self.velocity = math.Vector2(pos.x, pos.y), math.Vector2(0, 0)
        self.acceleration = math.Vector2(0, self.gravity)
        self.rect:Rect = self.current_sprite.get_rect()


    @property
    def player_info(self) -> Player:
        return GAME_STATE.players[self.player_index]

    @property
    def other_player(self) -> Player:
        return GAME_STATE.players[0 if self.player_index == 1 else 1]

    @property
    def key_mappings(self) -> dict:
        return PLAYER_1_KEYS if  self.player_index == 0 else PLAYER_2_KEYS


    @property
    def current_dict(self) -> dict:
        return self.sprites_l if self.FACING_LEFT else self.sprites_r

    @property
    def current_sprite(self) -> Surface:
        return self.current_dict[self.character_state][self.current_index]

    def update(self, dt:float) -> None:
        self.last_updated += dt
        self.atk_timer += dt

        if self.atk_start:
            self.atk_timer = 0

        if self.current_index == len(self.current_dict[self.character_state]) -1:
            if self.character_state == characterState.AKT or self.character_state.DEFEND:
                self.atk_start = False
                self.character_state = characterState.IDLE
                self.current_index = 0
        
        self.horizontal_movement(dt * SETTINGS['FPS_TARGET'])
        self.vertical_movement(dt * SETTINGS['FPS_TARGET'])

        self.collision_box.bottom = self.rect.bottom
        self.collision_box.centerx = self.rect.centerx

        self.player_info.collision_box = self.collision_box
        self.player_info.atk_collision_box = self.rect
        self.player_info.pos = self.position
        self.player_info.state = self.character_state

        if self.last_updated > 0.075:
            self.last_updated = 0
            self.current_index = (self.current_index + 1) % len(self.current_dict[self.character_state])

    def capture_events(self, event:Event) -> None:
        if event.type == KEYDOWN:
            if event.key == self.key_mappings[keyMappings.DEFEND]:
                self.character_state = characterState.DEFEND
                self.current_index = 0
            elif event.key == self.key_mappings[keyMappings.AKT]:
                self.character_state = characterState.AKT
                self.atk_start = True
                self.current_index = 0
            elif event.key == self.key_mappings[keyMappings.LEFT]:
                self.LEFT_KEY = True
                self.FACING_LEFT = True
            elif event.key == self.key_mappings[keyMappings.RIGHT]:
                self.character_state = characterState.JUMP
                self.RIGHT_KEY = True
                self.FACING_LEFT = False
            elif event.key == self.key_mappings[keyMappings.JUMP]:
                self.character_state = characterState.JUMP
                self.jump()

        if event.type == KEYUP:
            if event.key == self.key_mappings[keyMappings.DEFEND]:
                self.LOCKED = False
            elif event.key == self.key_mappings[keyMappings.LEFT]:
                self.LEFT_KEY = False
            elif event.key == self.key_mappings[keyMappings.RIGHT]:
                self.RIGHT_KEY = False
            elif event.key == self.key_mappings[keyMappings.JUMP]:
                if self.is_jumping:
                    self.velocity.y *= 0.25
                    self.is_jumping = False

    # took from https://github.com/ChristianD37/YoutubeTutorials/blob/master/Physics/player.py
    # for basic movement

    def horizontal_movement(self, dt):
        a = 1.5

        self.acceleration.x = 0
        if self.LEFT_KEY:
            self.acceleration.x -= a
        elif self.RIGHT_KEY:
            self.acceleration.x += a
        self.acceleration.x += self.velocity.x * self.friction
        self.velocity.x += self.acceleration.x * dt
        self.limit_velocity(4)
        self.position.x += self.velocity.x * dt + (self.acceleration.x * .5) * (dt * dt)
        self.rect.x = self.position.x

    def vertical_movement(self, dt):
        max_height = 20

        self.velocity.y += self.acceleration.y * dt
        if self.velocity.y > max_height: self.velocity.y = max_height
        self.position.y += self.velocity.y * dt + (self.acceleration.y * .5) * (dt * dt)
        if self.position.y > 700:
            self.on_ground = True
            self.velocity.y = 0
            self.position.y = 700
        self.rect.bottom = self.position.y

    def limit_velocity(self, max_vel):
        min(-max_vel, max(self.velocity.x, max_vel))
        if abs(self.velocity.x) < .01: self.velocity.x = 0

    def jump(self):
        if self.on_ground:
            self.is_jumping = True
            self.velocity.y -= 20
            self.on_ground = False
        
    def render(self, context:Surface) -> None:
        context.blit(self.current_sprite, self.rect)

   
