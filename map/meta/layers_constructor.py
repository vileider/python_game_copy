
from map.abstracts.layer_constructor_contract import LayersConstructorProtocol
import numpy as np
import csv
#from layer_constructor_contract import LayersConstructorProtocol


class TileLayerConstructor(LayersConstructorProtocol):

    def load_layer(self,path):
        
        with open(path, newline="") as file:
            layer_data = np.array(list(csv.reader(file)), dtype=str)
            
        return self.prepare_loaded_layer(layer_data)      
    
    def prepare_loaded_layer(self, layer):
        rows, cols = layer.shape
        return np.array([
                    {'element_name': element, 'coordinates': (row, col)}
                    for row in range(rows)
                    for col, element in enumerate(layer[row])
                ], dtype=object).reshape(rows, cols)



class UpperLayersConstructor(LayersConstructorProtocol):
    def __init__(self):
        pass        
        

    def load_layer(self, path):
        pass
    
    ### EXTENSION PORTION
    def prepare_loaded_layer(self, layer):
        pass