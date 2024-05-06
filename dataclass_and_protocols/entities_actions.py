from typing import Protocol
import pygame
from abc import abstractmethod
from types import MethodType

class LiveEntitiesActions(Protocol):
    @abstractmethod
    def equip_item(item: str, slot_name:str) -> None:
        ...
               
    @abstractmethod
    def heal(amount:int) -> None:
        ...

    @abstractmethod
    def gain_experience(experience: int) -> None:
        ...
        
    @abstractmethod
    def level_up(levels: int) -> None:
        ...

    @abstractmethod
    def melee_attack() -> int:
        ...

    @abstractmethod
    def magic_attack() -> int:
        ...

    @abstractmethod
    def range_attack() -> int:
        ...  
          
    @abstractmethod
    def display_chatbox() -> None:
        ...
    
    @abstractmethod
    def add_item(item:str) -> None:
        ...
    
    @abstractmethod
    def remove_item(item:str) -> None:
        ...
    

       
class EntitesMotionActions(Protocol):
    @abstractmethod
    def update_position(delta_time: float) -> None:
        ... 

    @abstractmethod
    def start_animation() -> None:
        ...
    
    @abstractmethod
    def move_to(coordinates: tuple) -> None:
        ...

    @abstractmethod
    def follow(followee) -> None:
        ...
    

class LifelessEntitiesActions(Protocol):
    @abstractmethod
    def use(class_instance: any) -> None: 
        ...
    
    @abstractmethod
    def take_damage(damage: int) -> None:
        ...
    
    @abstractmethod
    def display_info() -> None:
        ...


