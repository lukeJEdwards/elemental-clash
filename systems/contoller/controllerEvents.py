import os
from pygame.event import Event
from pygame.constants import JOYDEVICEADDED, JOYDEVICEREMOVED

from systems.contoller.controllerInput import BaseInput, KeyboardInput, ButtonInput, AxisInput, HatInput, ControllerNavInput
from utils import inputType

__all__ = ['ControllerEvents']

class ControllerEvents:
    def __init__(self, key_mappings:dict) -> None:
        self.controller_connected:bool = False
        self.keyboard_mappings:dict[str:KeyboardInput|ButtonInput] = self.get_keyboard_mappings(key_mappings['KEYBOARD'])
        self.controller_mappings:dict[str:ButtonInput|AxisInput|HatInput] = self.get_controller_mappings(key_mappings['CONTROLLER'])
        self.actions:dict = {
            'ATK_1': False,
            'ATK_2': False,
            'ATK_3': False,
            'ATK_SP': False,
            'DEFEND': False,
            'HEAL': False,
            'JUMP': False,
            'LEFT': 0,
            'RIGHT': 0,
            'ROLL': False,
            'RUN': False,
            "UP":False,
            "DOWN":False,
            "RIGHT":False,
            "LEFT":False,
        }
        
    def get_keyboard_mappings(self, mappings:dict[str:KeyboardInput|ButtonInput]) -> dict[str:KeyboardInput|ButtonInput]:
        for key, value in mappings.items():
            if value['type'] == inputType.BUTTON: mappings[key] = ButtonInput(**value)
            if value['type'] == inputType.KEYBOARD: mappings[key] = KeyboardInput(**value)
        return mappings 
        
    def get_controller_mappings(self, mappings:dict[str:ButtonInput|AxisInput|HatInput]) -> dict[str:ButtonInput|AxisInput|HatInput]:
        for key, value in mappings.items():
            if value['type'] == inputType.BUTTON: mappings[key] = ButtonInput(**value)
            if value['type'] == inputType.AXIS: mappings[key] = AxisInput(**value) 
            if value['type'] == inputType.HAT: mappings[key] = HatInput(**value) 
            if value['type'] == inputType.NAV: mappings[key] = ControllerNavInput(**value)
        return mappings
    
    def controller_state(self, event:Event) -> None:
        if event.type == JOYDEVICEADDED: self.controller_connected = True
        if event.type == JOYDEVICEREMOVED: self.controller_connected = False
        
    def update_actions(self, event:Event, dictionary:dict[str:BaseInput]) -> None:
        for key in self.actions.keys():
            if key in dictionary:
                dictionary[key].input_handler(event)
                self.actions[key] = dictionary[key]._value    
                
    
    def update(self, event:Event) -> None:
        self.controller_state(event)
        if self.controller_connected: self.update_actions(event, self.controller_mappings)
        else: self.update_actions(event, self.keyboard_mappings)
        
        os.system('cls')
        for key, value in self.actions.items():
            if value:
                print(f'{key}: {value}')
        
        