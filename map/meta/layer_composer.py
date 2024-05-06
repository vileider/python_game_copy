import numpy as np
from map.abstracts.layer_composer_contract import(LayerComposerVariables,
                                                    LayerComposerOperations,
                                                    LayerAlignmentOperations)


class LayerComposer(LayerComposerVariables,
                    LayerComposerOperations,
                    LayerAlignmentOperations):
    def __init__(self,array_of_objects,current_array_pos,visible_array_size,tile_size):
        self.array_of_objects = array_of_objects
        self.current_array_pos = current_array_pos
        self.visible_array_size = visible_array_size
        self.tile_size = tile_size
        self.sliced_array = self.cut_piece_from_TwoD_Arr_based_on_cooords(
                                                array_of_objects,
                                                self.current_array_pos,
                                                visible_array_size)
        
        self.visible_tiles_array = self.create_a_coord_array_for_each_tile(
                                                            self.visible_array_size,
                                                            self.tile_size,
                                                            self.sliced_array )

    def set_map_y_cooridnates_to_center_player_on_map(self,
                                                    visible_array_size,
                                                    playery_pos_on_screen,
                                                    tile_size,
                                                    ):

        return  playery_pos_on_screen - ((tile_size//2) * (visible_array_size/2)) - (tile_size//4) - (tile_size//8)

    def set_map_x_cooridnates_to_center_player_on_map(self,
                                                    playerx_pos_on_screen,
                                                    tile_size):
        eighth_tile = tile_size // 8
        return  playerx_pos_on_screen + eighth_tile
    
    def cut_piece_from_TwoD_Arr_based_on_cooords(self,
                                                array_of_objects,
                                                position,
                                                visible_array_size):

        coords_x = position[0] #4
        coords_y = position[1] # 5

        if coords_x < 0:
            coords_x = 0

        if coords_y <0:
            coords_y = 0
             
        start_row = int(coords_x)
        end_row= int(coords_y)      
        start_column=  int(coords_x + visible_array_size) 
        end_column= int(coords_y + visible_array_size)
        
        return array_of_objects[start_row:start_column, end_row:end_column]
    
    def create_a_coord_array_for_each_tile(self,
                                        visible_array_size,
                                        tile_size,
                                        sliced_array):
        
        half_screen_width = self.screen.get_size()[0] // 2
        half_screen_height = self.screen.get_size()[1] // 2

        start_x = self.set_map_x_cooridnates_to_center_player_on_map(
            half_screen_width,
            tile_size)   
             
        start_y = self.set_map_y_cooridnates_to_center_player_on_map(
            visible_array_size, 
            half_screen_height,
            tile_size)
        
        value_x = start_x
        value_y = start_y

        half_tile_size = tile_size // 2
        quarter_tile_size = tile_size // 4
        sliced_array = list(sliced_array)
        temp_arr = []
        #print("before",sliced_array)
        for index, element in np.ndenumerate(sliced_array):
            #x coordinate equals starting point minus half of tile width 
            #and the half of the width is multipled
            #by the column number counting from 0
            #to adjust next lines half of tile width is added to x coordinate, multiplied by row number couting from 0
            
            # index holds isometric coordinates of a block.
            # We divide tilesize in half to create this "honeycomb" pattern.
            # This only calculates relative coordinates to other tiles.
            value_x = start_x - half_tile_size * (1 + index[0] - index[1])
            
            value_y = start_y + quarter_tile_size * (1 + index[0] + index[1]) 

            temp_arr.extend([tuple([element,value_x, value_y])])

        return temp_arr