import pygame
# from support_classes.master_values import Master_Values
from support_classes.calculation_classes import  Calculation_on_array
from player.meta.movement_calculations_meta import CalculationsOnMovement

class Collision_handler(Calculation_on_array, CalculationsOnMovement):
    def __init__(self):
        super().__init__()
        CalculationsOnMovement.__init__(self)
        
        self.translate_direction = {
            '[0, -1]': 'top', 'top': [0, -1],
            '[-1, 0]': 'left', 'left': [-1, 0],
            '[0, 1]': 'bottom', 'bottom': [0, 1],
            '[1, 0]': 'right', 'right': [1, 0],

            '[-1, -1]': 'topleft', 'topleft': [-1, -1],
            '[1, -1]': 'topright', 'topright': [1, -1],
            '[1, 1]': 'bottomright', 'bottomright': [1, 1],
            '[-1, 1]': 'bottomleft', 'bottomleft': [-1, 1]
        }

        self.impassable_objects = [
            'W', 'water'
        ] # Open for expansion
        self.passable_objects = [
            'L', 'ground'
        ] # Open for expansion

    def approve_player_movement(self, collision_object, player, dt):
        
        # Collision object must have the following properties:
        # .name, .mask_rect, .mask
        
        if collision_object.name in self.impassable_objects:
            
            if player.direction:
                direction_x, direction_y = player.direction.x, player.direction.y
            else:
                direction_x, direction_y = player.last_direction[0], player.last_direction[1]
            
            expected_player_position = (player.rect.midbottom[0] + (direction_x*(player.stats.speed) *dt),
                                            player.rect.midbottom[1] + (direction_y / 2*(player.stats.speed) *dt))
            
            expected_player_position_surf = player.collision_surf.copy()
            expected_player_position_rect = expected_player_position_surf.get_rect(midbottom=expected_player_position)
            expected_player_position_mask = pygame.mask.from_surface(expected_player_position_surf)
            expected_player_position_mask_offset = tuple(map(lambda x,y: x - y, collision_object.mask_rect.topleft, expected_player_position_rect.midbottom))
            expected_player_position_overlap_area = expected_player_position_mask.overlap_area(collision_object.mask, expected_player_position_mask_offset)
            
            
            if expected_player_position_overlap_area:

                # If player is moving in a single direction
                if direction_x and not direction_y or direction_y  and not direction_x:

                    expected_player_position = (player.rect.midbottom[0] + (direction_x *(player.stats.speed) *dt),
                                                player.rect.midbottom[1] + (direction_y  / 2*(player.stats.speed) *dt))
                    if expected_player_position_overlap_area:
                        return False
                    else:
                        return True

                # If player is moving diagonally
                elif direction_x and direction_y :

                    expected_movement = self.ensure_diagonal_movement_ratio(pygame.math.Vector2(
                        direction_x,
                        direction_y /2 ) * player.stats.speed * dt)

                    expected_player_position = (player.rect.midbottom + expected_movement)                
                    if expected_player_position_overlap_area:
                        return False
                    else:
                        return True

    def package_collision_data(self,
                                tile,
                                element,
                                player_instance,
                                current_overlap):

        if tile.rect.collidepoint(player_instance.rect.center):                   
            distance_from_middle = tuple(map(lambda x, y: x - y,tile.rect.center, player_instance.ground_collision_rect.midbottom))
            packaged_tile = (current_overlap, tile.rect.topleft,element[0],distance_from_middle )
            return packaged_tile
                    
    ### GDSG
    def get_overlap_between_tile_and_player(self, tile, player):
        mask_offset = tuple(map(lambda x, y: x - y, tile.mask_rect.topleft,player.rect.midbottom ))

        if player.collision_mask.overlap(tile.mask, mask_offset):
            current_overlap = player.collision_mask.overlap_area(tile.mask, mask_offset)
            return current_overlap
        return int(0)


    def get_highest_overlapping_element(self, colliding_tiles):
        tuple_with_highest_value = max(colliding_tiles, key=lambda x: x[0])    
        return tuple_with_highest_value