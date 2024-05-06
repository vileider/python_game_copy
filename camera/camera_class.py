import pygame

from support_classes.calculation_classes import Calculation_on_array

class CameraGroup(Calculation_on_array):
    def __init__(self):
        super().__init__()
        # Get display surface


        self.screen = pygame.display.get_surface()

        # Camera offset
        self.offset = pygame.math.Vector2()
        self.half_W = self.screen.get_size()[0] // 2
        self.half_y = self.screen.get_size()[1] // 2
        self.screen_size = self.screen.get_size()
        self.middle_of_screen = (self.screen_size[0] // 2,
                        self.screen_size[1] // 2)
        
        # Camera Rect
        self.rect = pygame.Rect(
            self.offset.x,
              self.offset.y,
                self.screen_size[0],
                  self.screen_size[1])
        
    def set_offset_on_player(self,
                             player_instance,
                             ):
        
        ### [T-75]: Centered camera at player.rect.center instead of
        ### player.rect.topleft. This is to make sure the sprite height doesn't
        ### cause issues.
        self.offset.x = player_instance.rect.center[0] - self.half_W
        self.offset.y = player_instance.rect.center[1] - self.half_y

        self.rect.centerx = player_instance.rect.center[0] - self.offset.x
        self.rect.centery = player_instance.rect.center[1] - self.offset.y

      
    def display_on_screen(self,
                          subject_instance):
        
        # Center player
        self.set_offset_on_player(subject_instance)
             
        self.screen.blit(subject_instance.surf, subject_instance.rect.topleft - self.offset)
        #self.player.rect.center = self.rect.center
        

    def apply_interblock_offset(self,
                                 map_distance_from_the_midle_of_tile: tuple, 
                                 player_rect: pygame.Rect):

        position = tuple(map(
            lambda x, y: x - y,
                 (self.middle_of_screen[0] + 8,
                  self.middle_of_screen[1] + 8),
                 map_distance_from_the_midle_of_tile))
        player_rect.topleft =  position
                                                             
    def check_if_player_moved(self,master_val_instance):
        dis_old = master_val_instance.previous_offset
        dis_new = master_val_instance.offset
        if dis_old == dis_new:
            return False
        else:
            master_val_instance.previous_offset = (
                master_val_instance.offset)
            return True






