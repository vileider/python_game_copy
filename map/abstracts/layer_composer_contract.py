from typing import Protocol
from abc import abstractmethod
import numpy as np
from dataclasses import dataclass, field


@dataclass
class LayerComposerVariables():
    visible_tiles_array: np.array = field(init=True)
    sliced_array: np.array = field(init=False)
    
    current_array_pos: tuple = field(init=False)
    tile_size: tuple = field(init=False)
    visible_array_size: tuple = field(init=False)

class LayerComposerOperations(Protocol):
    @abstractmethod
    def cut_piece_from_TwoD_Arr_based_on_cooords(array_of_objects_array:np.array,
                                                position:tuple,
                                                visible_array_size:int
                                                ) -> np.array:
        ...

    @abstractmethod
    def create_a_coord_array_for_each_tile(sliced_array: np.array,
                                           visible_array_size: int,
                                           tile_size:int
                                           ) -> np.array:
        ...


class LayerAlignmentOperations(Protocol):
    @abstractmethod
    def set_map_x_cooridnates_to_center_player_on_map(playerx_pos_on_screen:int,
                                                      tile_size:int
                                                      ) -> int:
        ...
    
    @abstractmethod
    def set_map_y_cooridnates_to_center_player_on_map(playery_pos_on_screen:int,
                                                      tile_size:int,
                                                      visible_array_size:int
                                                      ) -> int:
        ...


