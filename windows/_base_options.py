from PyQt5.QtWidgets import QWidget, QPushButton
from ._base_window import BaseWindow
from ._window_help import WindowChange


class BaseOptionsWindow(BaseWindow):
    def init_buttons(self):
        place = (self.pad[0], self.size[1] - self.pad[1] -
                 self.buttons_size[1])
        self.init_button('to main page',
                         WindowChange(self, self.game.windows['main']),
                         place)
        place = (self.size[0] - self.pad[0] - self.buttons_size[0],
                 self.size[1] - self.pad[1] - self.buttons_size[1])
        self.init_button('start game', lambda x: None, place)
