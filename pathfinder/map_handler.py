from .config import *
import osmnx as ox

class MapHandler:
    def __init__(self) -> None:
        self._loading_map = True
    
    def download_map(self) -> None:
        if not hasattr(self, 'graph'):
            self.graph = ox.graph_from_place(LOCATION, network_type=NETWORK_TYPE)
        self._loading_map = False
        
    def is_loading_map(self) -> bool:
        return self._loading_map