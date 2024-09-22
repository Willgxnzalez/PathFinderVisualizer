import pyglet as pg
from .const import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE


class App(pg.window.Window):
    def __init__(self) -> None:
        super().__init__(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, caption=WINDOW_TITLE, resizable=True)
        self.set_minimum_size(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    
    def start(self):
        pg.app.run()