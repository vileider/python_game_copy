from map.meta.layer_composer import LayerComposer


class GameMenuActions(LayerComposer):
    def __init__(self,
                     raw_ground_layer,
                     visible_array_size):
        self.raw_ground_layer = raw_ground_layer
        self.visible_array_size = visible_array_size
        self.sliced_array = self.cut_piece_from_TwoD_Arr_based_on_cooords(
                                            self.raw_ground_layer,
                                            (34,25) ,
                                            self.visible_array_size)
        self.player_position_dataset = ()
    def prepare_restart_pos(self):
        self.sliced_array = self.cut_piece_from_TwoD_Arr_based_on_cooords(
                                            self.raw_ground_layer,
                                            (33,25) ,
                                            self.visible_array_size)
    def create_restart_game_tuple(self,TRIMMED_MAP_SIZE,TILE_SIZE):
        visible_tiles_array = self.create_a_coord_array_for_each_tile(TRIMMED_MAP_SIZE,
                                                                    TILE_SIZE,
                                                                    self.sliced_array)
        colliding_tiles = [(128, (464, 336), {'element_name': 'L', 'coordinates': (42, 33)}, (5, 24))]
        current_array_pos=(33, 25)

        return(visible_tiles_array,colliding_tiles,current_array_pos)
    
    def save_player_position_dataset(self,
                                    visible_tiles_array,
                                    colliding_tiles,
                                    current_array_pos):
        self.player_position_dataset = (visible_tiles_array,colliding_tiles,current_array_pos)

    def dataset_empty(self):
        if self.player_position_dataset != () :
            return False
        else:
            return True

        