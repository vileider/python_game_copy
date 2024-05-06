### Assumed destination class
from typing import Protocol
from abc import abstractmethod
import numpy as np


class LayersConstructorProtocol(Protocol):        
    
    @abstractmethod
    def load_layer(path: str) -> np.array:
        ...

    @abstractmethod
    def prepare_loaded_layer(layer: np.array) -> np.array:
        ...

