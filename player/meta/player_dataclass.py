from dataclasses import dataclass, field
import pygame


@dataclass
class PlayerValuesDefinition:
    PLAYER_SIZE: tuple
    pos: tuple  = field(init=False)
    surf: pygame.image
    path_string: str
    rect: pygame.Rect 
    collision_rect: pygame.rect = 0
    mask: pygame.mask = 0
    mask_image: pygame.image = 0
    collision_mask: pygame.mask = field(init=False)
    collision_surf: pygame.surface = field(init=False)
    ground_collision_mask: pygame.mask = field(init=False)
    ground_collision_rect: pygame.Rect = field(init=False)
    global_player_position: tuple = field(init=False)
    direction: pygame.math.Vector2 = field(init=False)

    def _post_init_(self) -> None:
        self.surf = pygame.transform.scale(self.surf, self.PLAYER_SIZE)
        self.rect = self.surf.get_rect()


class PlayerData(PlayerValuesDefinition):
    def __init__(self, position_on_screen):

        ### [T-75] PLAYER_SIZE must be a multiplication of 32.
        self.PLAYER_SIZE= 32
        self.surf=pygame.image.load('player/player.png')
        self.path_string="player/player.png"

        self.surf = pygame.transform.scale(self.surf, (self.PLAYER_SIZE * 10,self.PLAYER_SIZE * 5))
        self.pos = position_on_screen
        self.rect = self.surf.get_rect()
       
        # Rect for ground collision
        # [T-74]: Changed rect's size to a constant of (16,8)
        self.ground_collision_rect = pygame.Rect((self.rect.centerx - self.PLAYER_SIZE // 4,
                                            self.rect.centery + self.PLAYER_SIZE // 4)
                                                 ,(16, 8))
        
        ### [T-74]: This is to prevent spawning outside the active area
        self.ground_collision_rect.topleft = self.pos
        self.rect.midbottom = self.ground_collision_rect.midbottom
        
        ### General purpose mask
        self.mask = pygame.mask.from_surface(self.surf)
        self.mask_image = self.mask.to_surface()
        
        ### Ground collisions mask
        self.collision_surf = pygame.Surface((self.PLAYER_SIZE // 2,
                                             self.PLAYER_SIZE // 4))
        self.collision_surf.fill('GREEN')
        self.collision_mask = pygame.mask.from_surface(self.collision_surf)
        self.mask_surf = pygame.mask.Mask.to_surface(self.collision_mask)

        self.direction = pygame.math.Vector2()

        self.start_coordx = 0
        self.start_coordy = 0

        
        