import pygame
from support_classes.master_values import Master_Values 

class Tiles():
    
    def __init__(self):
        self.TILE_SIZE = Master_Values().TILE_SIZE
        
        self.land_polygon_vertices = [
                (0, self.TILE_SIZE[1] // 2)
                ,
                (self.TILE_SIZE[0] // 2, (self.TILE_SIZE[1] // 4))
                ,
                (self.TILE_SIZE[0], self.TILE_SIZE[1] // 2)
                ,
                (self.TILE_SIZE[0] // 2, self.TILE_SIZE[1] - self.TILE_SIZE[1] // 4)
            ]
        self.water_polygon_vertices = [
                (0, (self.TILE_SIZE[1] // 2) + self.TILE_SIZE[1] // 8) # LEFT: O
                ,
                (self.TILE_SIZE[0] // 2, (self.TILE_SIZE[1] // 4) + self.TILE_SIZE[1] // 8) # TOP
                ,
                (self.TILE_SIZE[0], (self.TILE_SIZE[1] // 2) + self.TILE_SIZE[1] // 8) # RIGHT
                ,
                (self.TILE_SIZE[0] // 2, self.TILE_SIZE[1] - self.TILE_SIZE[1] // 8)# BOTTOM O
            ]
        
        

        self.tile_dict = { "W":  self.createSprite( "water", "./images/water_tile",
                                        (0, 0),self.TILE_SIZE[0],self.TILE_SIZE[1]),
                        "L": self.createSprite("ground", "./images/ground_tile",
                                        (0, 0), self.TILE_SIZE[0], self.TILE_SIZE[1])}


    
    def create_tile(self,t_value):

        tile = self.tile_dict[t_value[0]['element_name']]
        x,y = t_value[1],t_value[2]
        tile.rect.topleft = (x,y)
        tile.mask_rect.topleft = (x,y) 
    
        return  tile
    
    #def check_for_collision()
                                                                # + player, master_val
    def createSprite(self, name, fileName, position, width=0, height=0):
        print(f'''
              name = {name},
              filename = {fileName},
              position = {position},
              width = {width},
              height = {height}
              ''')
        sprite = pygame.sprite.Sprite()
        sprite.name = name
        sprite.filename = fileName
        sprite.image = pygame.image.load(f"{fileName}.png").convert_alpha()

        if width and height:
            sprite.image = pygame.transform.scale(sprite.image, (width, height))

        sprite.rect = sprite.image.get_rect(topleft=position)
        sprite.mask = pygame.mask.from_surface(sprite.image)
        sprite.mask_surface = sprite.mask.to_surface()
        #sprite.rect.collidepoint(player)
        if name == 'water':
            sprite.mask_surface = pygame.Surface(self.TILE_SIZE, pygame.SRCALPHA)
            sprite.mask_surface.fill((0,0,0,0))           
            sprite.mask_rect = sprite.mask_surface.get_rect(topleft=position)
                        
            pygame.draw.polygon(sprite.mask_surface, "WHITE", self.water_polygon_vertices, 0)
            sprite.mask = pygame.mask.from_surface(sprite.mask_surface)
            sprite.mask_surface = pygame.mask.Mask.to_surface(sprite.mask).convert_alpha()
            #pygame.image.save(tile.mask_surface1, "land_mask.png")
        
        elif name == "ground":
            sprite.mask_surface = pygame.Surface(self.TILE_SIZE, pygame.SRCALPHA)
            sprite.mask_surface.fill((0,0,0,0))      

            sprite.mask_rect = sprite.mask_surface.get_rect(topleft=position)

            pygame.draw.polygon(sprite.mask_surface, "WHITE", self.land_polygon_vertices, 0)
            sprite.mask = pygame.mask.from_surface(sprite.mask_surface)
            sprite.mask_surface = pygame.mask.Mask.to_surface(sprite.mask).convert_alpha()
            
        elif name == 'waterf':
            sprite.mask_surface = pygame.Surface(self.TILE_SIZE, pygame.SRCALPHA)
            sprite.mask_surface.fill((0,0,0,0))      

            sprite.mask_rect = sprite.mask_surface.get_rect(topleft=position)

            pygame.draw.polygon(sprite.mask_surface, "WHITE", self.land_polygon_vertices, 0)
            sprite.mask = pygame.mask.from_surface(sprite.mask_surface)
            sprite.mask_surface = pygame.mask.Mask.to_surface(sprite.mask).convert_alpha()
        '''
        if sprite.rect.collidepoint(player.rect.center):
            mask_offset = tuple(map(lambda x, y: x - y, sprite.mask_rect.topleft,player.rect.midbottom ))
            current_overlap = player.collision_mask.overlap_area(sprite.mask, mask_offset)

            distance_from_middle = tuple(map(lambda x, y: x - y, sprite.rect.center, player.rect.center))
            packaged_tile = (sprite, current_overlap, tile.rect.topleft,name,distance_from_middle)
            master_val.colliding_tiles.extend([packaged_tile])
        '''
        
        return sprite