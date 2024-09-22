import pyglet as pg
from .config import *
from .map_handler import MapHandler
import threading

class App(pg.window.Window):
    def __init__(self) -> None:
        
        config = pg.gl.Config(double_buffer=True)
        super().__init__(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, config=config, caption=WINDOW_TITLE, resizable=True)
        self.set_minimum_size(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        
        self._map_handler = MapHandler()
        self._map_render_batch = pg.graphics.Batch()
    
    def on_draw(self) -> None:
        self.clear()
        
        
    def update(self, dt: float) -> None:
        if not self._map_handler.is_loading_map():
            print("map finished loading")
    
    def start(self) -> None:
        threading.Thread(target=self._map_handler.download_map, daemon=True).start()
        pg.clock.schedule_interval(self.update, 1/FPS)
        pg.app.run()