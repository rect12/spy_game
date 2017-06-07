from PyQt5.QtWidgets import QWidget, QPushButton
from .base_window import BaseWindow


class PlayerOptionsWindow(BaseWindow):
    def __init__(self):
        super().__init__('Player options')

    def set_geometry(self):
        self.size = (300, 300)
        self.resize(*self.size)

    def init_buttons(self):
        place = (self.pad[0], self.size[1] - self.pad[1] -
                 self.buttons_size[1])
        self.init_button('to main page', lambda x: None, place)
