
__all__ = ['Controller']

import os

from pygame.constants import JOYDEVICEADDED, JOYDEVICEREMOVED
from pygame.event import Event

from utils import inputType
from systems.input import BaseInput, ButtonInput
    
        
class Controller:
    def __init__(self, key_mapping:dict[str, BaseInput]) -> None:
        self.key_mapping:dict[str, BaseInput] = {key: value for key, value in key_mapping.items() if value.input_type != inputType.BUTTON}
        self.button_mapping:dict[str, ButtonInput] = {key: value for key, value in key_mapping.items() if value.input_type == inputType.BUTTON}
        self.actions:dict[str, bool|float] = {key: 0 if value.input_type == inputType.AXIS else False for key, value in key_mapping.items()}
        self.controller_connected:bool = False
        
    def controller_state(self, event:Event) -> None: 
        if event.type == JOYDEVICEADDED:
            self.controller_connected = True
        if event.type == JOYDEVICEREMOVED:
            self.controller_connected = False
            
    def button_update(self, event:Event, dt:float) -> None:
        for key, value in self.button_mapping.items(): 
            self.actions[key] = value.input_handler(event, dt)
            
    def key_update(self, event:Event) -> None:
        for key, value in self.key_mapping.items(): self.actions[key] = value.input_handler(event)
            
    def update(self, event:Event, dt:float) -> None:
        self.controller_state(event)
        self.button_update(event, dt)
        self.key_update(event)
        
        os.system('cls')
        print(f'CONNECTED: {self.controller_connected}')
        print('----CONTROLLER INPUTS----')
        for key, value in self.actions.items(): print(f'{key}: {value}')

            
        
        