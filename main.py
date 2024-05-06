import pygame
from player.player_class import Player
from ui.user_interface import UserInterface
from camera.camera_class import CameraGroup
import cProfile

from support_classes.collisions_class import Collision_handler
from support_classes.master_values import Master_Values
from event_handler import Event_Handler
from input_class.input import Input

pygame.init()

# Instantiate mastervalues
master_val = Master_Values()

screen = pygame.display.set_mode((1024, 768), pygame.DOUBLEBUF)
start_position = (screen.get_size()[0] // 2, screen.get_size()[1] // 2)
# Instantiate Player
player = Player()
# Instantiate colisions
collision_handler = Collision_handler()
# Instantiate Camera:
camera = CameraGroup()
# Instantiate UI
ui = UserInterface()
# inputclass Initiates
input_class = Input()

# Mediator Instance
events = Event_Handler(master_val,player,collision_handler,camera,input_class,ui)

#while(1) imprive speed by couple miliseconds coparing with true
running = 1
clock = pygame.time.Clock()

pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])

def main_loop():
    while(running):

        events.main_process()            
        pygame.display.update()

#cProfile.run('main_loop()')
main_loop()
