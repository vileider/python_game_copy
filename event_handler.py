import pygame
from map.tiles import Tiles
from support_classes.calculation_classes import  Calculation_on_array, Run_Only_once
from support_classes.debug_classes import Debug_window, Fps_counter
from map.meta.layers_constructor import TileLayerConstructor
from map.meta.layer_composer import LayerComposer
from support_classes.game_menu_actions import GameMenuActions


class Event_Handler(Tiles,
                    Run_Only_once,GameMenuActions,
                    Calculation_on_array,
                    Debug_window, Fps_counter,
                    TileLayerConstructor,
                    LayerComposer,
                    ):
    def __init__(self, master_val,
                player,
                collision_handler,
                camera,
                Input,
                ui,
                ):
        
        self.raw_ground_layer = TileLayerConstructor().load_layer("map/alpha_map.csv")
        Run_Only_once.__init__(self)
        Tiles.__init__(self)
        Fps_counter.__init__(self)
        Debug_window.__init__(self)
        self.screen = pygame.display.get_surface()
        self.keys = pygame.key.get_pressed()
        self.player = player
        self.camera = camera
        
        self.master_val = master_val
        self.collisions = collision_handler
        self.ui = ui
        self.input_class = Input
        GameMenuActions.__init__(self,self.raw_ground_layer,
                                 self.master_val.TRIMMED_MAP_SIZE)
        LayerComposer.__init__(self,
                            self.raw_ground_layer,
                            self.master_val.current_array_pos,
                            self.master_val.TRIMMED_MAP_SIZE,
                            self.TILE_SIZE[0])
        #raw version
    def restart_game(self):
        restart_game_tuple = self.create_restart_game_tuple(self.master_val.TRIMMED_MAP_SIZE,
                                                     self.TILE_SIZE[0])
        self.visible_tiles_array = restart_game_tuple[0]
        self.master_val.colliding_tiles =restart_game_tuple[1]
        self.master_val.current_array_pos=restart_game_tuple[2]

    def save_game(self):
        self.save_player_position_dataset(self.visible_tiles_array,
                                        self.master_val.colliding_tiles,
                                        self.master_val.current_array_pos)
        
    ### [T-75] Temporary solution to tying player's position to
    ### the ground rect after apply_interblock_offset()
    def tie_player_pos_to_ground_rect(self, player_rect, player_ground_rect):
        player_rect.midbottom = player_ground_rect.midbottom
    
    def load_saved_game(self):
        self.master_val.current_player_pos = (
                            self.create_player_isometric_position_based_on_map_and_size(
                                self.master_val.TRIMMED_MAP_SIZE,
                                self.player_position_dataset[2]))
        self.visible_tiles_array = self.player_position_dataset[0]
        self.master_val.colliding_tiles = self.player_position_dataset[1]
        self.master_val.current_array_pos = self.player_position_dataset[2]
        self.player_position_dataset = ()

    def main_process(self):
        self.is_player_allowed_to_move = True
        self.screen.fill((0, 0, 255))
        self.read_input()
        self.display_ground_tiles()
        #if camera.check_if_player_moved(master_val):
        self.camera.display_on_screen(self.player)
        dt = self.get_delta_time()
        self.master_val.dt = dt
        self.player.update_position(dt, self.input_class.max_fps_diagonal_movement_toggle, self.is_player_allowed_to_move)
        self.display_fps(60)
        self.ui.display_ui()  
        
    def read_input(self):
        self.input_class.handle_input(self.master_val,
                                    self.camera,
                                    self.player,
                                    self.ui,self.restart_game,
                                    self.dataset_empty(),
                                    self.save_game,
                                    self.load_saved_game)

    def display_ground_tiles(self):      
                 
        if self.run_once():  
            self.master_val.current_player_pos = (
                            self.create_player_isometric_position_based_on_map_and_size(
                                self.master_val.TRIMMED_MAP_SIZE,
                                self.master_val.current_array_pos))

        ### COLLISIONS
        for t_value in self.visible_tiles_array:      
            tile = self.create_tile(t_value)
            self.screen.blit(tile.image, tile.rect.topleft - self.camera.offset) 
            active_center_surface = self.get_neighbouring_points_including_player(
                self.master_val.current_player_pos[0],self.master_val.current_player_pos[1])
            if t_value[0]['coordinates'] in active_center_surface:
                #self.display_mesh(True,tile,self.camera.offset)
                current_overlap = self.collisions.get_overlap_between_tile_and_player(tile, self.player)
                packaged_tile = self.collisions.package_collision_data(tile,t_value,self.player,current_overlap)
                if packaged_tile:
                    self.master_val.colliding_tiles.extend([packaged_tile])
    
            if self.master_val.most_tile: #...exists              
                is_player_allowed_to_move = self.collisions.approve_player_movement(tile, self.player, self.master_val.dt)
                if is_player_allowed_to_move == False or is_player_allowed_to_move == True:
                    self.is_player_allowed_to_move = is_player_allowed_to_move

        if self.master_val.colliding_tiles:

            highest_overlapping_element = self.collisions.get_highest_overlapping_element(self.master_val.colliding_tiles)        
            # Gives inital value
            if not self.master_val.most_tile: #...not exists
                self.master_val.most_tile = highest_overlapping_element
            # When player step on new tile, new tile values are passed to master values
            if self.master_val.most_tile[2]['coordinates'] != highest_overlapping_element[2]['coordinates']:
                self.master_val.current_player_pos = highest_overlapping_element[2]['coordinates']
                self.master_val.most_tile = highest_overlapping_element
                self.master_val.distance_from_middle_of_tile = self.master_val.most_tile[3]   
  
        if self.check_if_element_is_around_the_player(self.master_val.current_player_pos,
                                                                    self.master_val.TRIMMED_MAP_SIZE,
                                                                    self.master_val.current_array_pos):
            
            calculation_tuple = self.get_new_extension_scope(self.master_val.TRIMMED_MAP_SIZE,
                                                                         self.master_val.current_array_pos,
                                                                         self.master_val.current_player_pos)  
    
            #CHEKS IF PLAYER                          
            if self.master_val.current_player_pos != self.master_val.old_player_pos:

                self.master_val.current_array_pos = tuple(map(lambda x, y: x + y,calculation_tuple,self.master_val.current_array_pos))
            
                self.sliced_array = self.cut_piece_from_TwoD_Arr_based_on_cooords(
                                                            self.raw_ground_layer,
                                                            self.master_val.current_array_pos ,
                                                            self.visible_array_size)
                
                
                self.camera.apply_interblock_offset(self.master_val.distance_from_middle_of_tile, self.player.ground_collision_rect)
                
                ### [T-75] - Needed to change player's position right after teleportation.
                ### I created a temporary function that does that, but it needs to be moved somewhere else.
                self.tie_player_pos_to_ground_rect(self.player.rect, self.player.ground_collision_rect)
      
                self.visible_tiles_array = self.create_a_coord_array_for_each_tile(self.master_val.TRIMMED_MAP_SIZE,
                                                                                    self.master_val.TILE_SIZE[0],
                                                                                    self.sliced_array)
                #BECAUSE NEW TILE MAP IS GENERATED IT MEANS PLAYER HAS NEW POSITION
                self.master_val.old_player_pos = self.master_val.current_player_pos

        self.master_val.colliding_tiles.clear()
        
        #self.screen.blit(self.player.collision_surf, self.player.ground_collision_rect.topleft - self.camera.offset)
        #print(self.player.ground_collision_rect.topleft)
        