import pyglet as pg
from .config import *
from .map_handler import MapHandler
import threading

class App(pg.window.Window):
    def __init__(self) -> None:
        super().__init__(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, caption=WINDOW_TITLE, resizable=True)
        self.set_minimum_size(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        
        self._map_handler = MapHandler()
    
    def on_draw(self) -> None:
        self.clear()
        
    def update(self, dt: float) -> None:
        if not self._map_handler.is_loading_map():
            print("map finished loading")
    
    def start(self):
        threading.Thread(target=self._map_handler.download_map, daemon=True).start()
        pg.clock.schedule_interval(self.update, 1/FPS)
        pg.app.run()