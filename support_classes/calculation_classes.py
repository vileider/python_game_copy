import numpy as np

class Calculation_on_array:

    ### [T-74]: Extended neighbouring points to 2 tiles radius.
    def get_neighbouring_points(self,x,y):
        return [
            (x-1,y-1), # Adj Top
            (x-1,y  ), # Adj Topright
            (x-1,y+1), # Adj Right
            (x,y-1  ), # Adj Topleft
            (x,y+1  ), # Adj Bottomright
            (x+1,y-1), # Adj left
            (x+1,y  ), # Adj Bottomleft
            (x+1,y+1), # Adj Bottom
            
            (x-2, y-2), # Far Top
            (x+2, y+2), # Far Bottom
            (x+2, y-2), # Far Left
            (x-2, y+2), # Far Right
            
            (x-2, y-1), # Far Topright1
            (x-2, y  ), # Far Topright2
            (x-2, y+1), # Far Topright3
             
            (x-1, y+2), # Far Bottomright1
            (x, y+2  ), # Far Bottomright2
            (x+1, y+2), # Far Bottomright3
            
            (x+2, y-1), # Far bottomleft1
            (x+2, y  ), # Far Bottomleft2
            (x+2, y+1), # Far Bottomleft3
            
            (x-1, y-2), # Far Topleft1
            (x, y-2  ), # Far Topleft2
            (x+1, y-2)] # Far Topleft3
        
    
    def get_neighbouring_points_including_player(self, x,y):
        return [
            (x-1,y-1), # Adj Top
            (x-1,y  ), # Adj Topright
            (x-1,y+1), # Adj Right
            (x,y    ), # Player's position
            (x,y-1  ), # Adj Topleft
            (x,y+1  ), # Adj Bottomright
            (x+1,y-1), # Adj left
            (x+1,y  ), # Adj Bottomleft
            (x+1,y+1), # Adj Bottom
            
            (x-2, y-2), # Far Top
            (x+2, y+2), # Far Bottom
            (x+2, y-2), # Far Left
            (x-2, y+2), # Far Right
            
            (x-2, y-1), # Far Topright1
            (x-2, y  ), # Far Topright2
            (x-2, y+1), # Far Topright3
             
            (x-1, y+2), # Far Bottomright1
            (x, y+2  ), # Far Bottomright2
            (x+1, y+2), # Far Bottomright3
            
            (x+2, y-1), # Far bottomleft1
            (x+2, y  ), # Far Bottomleft2
            (x+2, y+1), # Far Bottomleft3
            
            (x-1, y-2), # Far Topleft1
            (x, y-2  ), # Far Topleft2
            (x+1, y-2)] # Far Topleft3


    
    def create_a_2darr_of_objects(self,twod_arr):
        rows, cols = twod_arr.shape
        return np.array([
                    {'element_name': element, 'coordinates': (row, col)}
                    for row in range(rows)
                    for col, element in enumerate(twod_arr[row])
                ], dtype=object).reshape(rows, cols)
    
    def create_player_isometric_position_based_on_map_and_size(self,map_size:int,array_pos: tuple):
        half_map_size_as_x = map_size //2
        half_map_size_as_y = map_size //2

        # indicators for the middle tile position2
        x_indicator = array_pos[0] + half_map_size_as_x
        y_indicator = array_pos[1] + half_map_size_as_y
        return (x_indicator,y_indicator)
    
    def create_an_array_with_eight_coords_arround_the_middle_(self,map_size:int,array_pos:tuple):
        #map size dived by 2 gives the middle index of the array
        #which might be the player`s tile
        #Example:
        #if the map size is 3, player is on tile index (1,1)
        # tiles  (0,0), (0,1), (0,2)
        # tiles  (1,0), player,(1,2)
        # tiles  (2,0), (2,1), (2,2)
        # get index of the middle of the map
        half_map_size_as_x = map_size //2
        half_map_size_as_y = map_size //2

        # indicators for the middle tile position2
        x_indicator = array_pos[0] + half_map_size_as_x
        y_indicator = array_pos[1] + half_map_size_as_y
        return self.get_neighbouring_points(x_indicator,y_indicator)
    
    
    def check_if_element_is_around_the_player(self,
                                               current_isometric_player_pos: tuple,
                                               TRIMMED_MAP_SIZE: int,
                                               current_array_pos: tuple):
        
        #creates and array of 8 elements arround the player
        arr = self.create_an_array_with_eight_coords_arround_the_middle_(TRIMMED_MAP_SIZE,
                                                                         current_array_pos)

        #if player entered one of the eight tiles:
        if current_isometric_player_pos in arr:
            return True
        else:
            return False
        
    def get_new_extension_scope(self, MAP_SIZE: int,
                                   array_pos: tuple,
                                   player_pos: tuple):
        arr = self.create_an_array_with_eight_coords_arround_the_middle_(MAP_SIZE,
                                                                         array_pos
                                                                         )
        index = arr.index(player_pos)        
        new_coord_list = self.get_neighbouring_points(0,0)
        
        extension_scope = new_coord_list[index]     
        
        return extension_scope



class Run_Only_once:
    def __init__(self):
        self.switch = True

    def run_once(self):
        if self.switch:
            self.switch = False
            return True
        else:
            False
            
            
run_once1 = Run_Only_once()
run_once2 = Run_Only_once()
