import pygame
from support_classes.calculation_classes import Calculation_on_array

class Master_Values(Calculation_on_array):
    def __init__(self):
        super().__init__()
        self.dt = 0
        self.most_tile = 0
        self.player_cartesian_pos = 0
        self.offset = (0,0)
        self.previous_offset =(0,0)
        self.TRIMMED_MAP_SIZE = 17
        self.current_player_pos = (0,0) 
        self.current_array_pos = (34,25)
        self.TILE_SIZE = (128,128)
        self.colliding_tiles = []
        #self.highest_overlap = 0
        self.highest_overlap_tile = None
        self.distance_from_middle_of_tile = (0,0)
        self.old_player_pos = (0,0)
        self.adjacent_tiles = {
            'top': '',
            'left': '',
            'bottom': '',
            'right': '',
            
            'topleft': '',
            'topright': '',
            'bottomleft': '',
            'bottomright': '',
        }
        self.impassable_tiles = [
            'water',
            'W'
        ]
        value = 0.75
        self.direction_dict = {
            pygame.K_UP: -value,
            pygame.K_DOWN: value,
            
            pygame.K_LEFT: -value,
            pygame.K_RIGHT: value
        }    

        self.directions_x = {
            pygame.K_LEFT: -value,
            pygame.K_RIGHT: value
        }
        self.directions_y = {
            pygame.K_UP: -value,
            pygame.K_DOWN: value
        }
