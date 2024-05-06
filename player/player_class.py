import pygame
import time
from player.meta.player_stats import PlayerStats
from player.meta.player_dataclass import PlayerData
from player.meta.player_actions import PlayerActions

class Player(PlayerStats,PlayerData,PlayerActions):
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.start_position = (self.screen.get_size()[0] // 2, self.screen.get_size()[1] // 2)
        PlayerStats.__init__(self)
        PlayerData.__init__(self,self.start_position)
        PlayerActions.__init__(self,self.stats)
        self.inventory = []
        self.equipment = {
            'head': None,
            'chest': None,
            'legs': None,
            'feet': None,
            'ring1': None,
            'ring2': None,
            'necklace': None,
            'left_hand': None,
            'right_hand': None}
        
