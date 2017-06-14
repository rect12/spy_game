from PyQt5.QtWidgets import QWidget, QPushButton
from ._base_window import BaseWindow
from ._window_help import WindowChange


class GameWindow(BaseWindow):
    def __init__(self, game):
        super().__init__(game, 'Game')

    def set_geometry(self):
        self.resize(300, 300)

    def get_buttons_places(self):
        return [(self.size().width() - self.pad[0] - self.buttons_size[0],
                 self.size().height() - self.pad[1] - self.buttons_size[1]),
                (self.pad[0], self.size().height() - self.pad[1] -
                 self.buttons_size[1])]

    def init_buttons(self):
        place = (self.size().width() / 2 - self.buttons_size[0] / 2,
                 self.size().height() - self.pad[1] - self.buttons_size[1])
        self.init_button('to main page',
                         WindowChange(self, self.game.windows['main']),
                         place)
