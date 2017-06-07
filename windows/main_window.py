from PyQt5.QtWidgets import QWidget, QPushButton, QDesktopWidget
from .base_window import BaseWindow


class MainWindow(BaseWindow):
    def __init__(self):
        self.buttons_number = 4
        super().__init__('The Spy')
        self.show()

    def set_geometry(self):
        self.resize(self.pad[0] * 2 + self.buttons_size[0],
                    self.pad[1] * (self.buttons_number + 1) +
                    self.buttons_number * self.buttons_size[1])

    def init_buttons(self):
        names = ['player options',
                 'game options',
                 'setting options',
                 'start game']

        click_functions = [lambda x: None] * 4

        for ind, (name, click_func) in enumerate(zip(names, click_functions)):
            vertical_size = self.buttons_size[1] + self.pad[1]
            vertical_shift = self.pad[1] + ind*vertical_size
            place = (self.pad[0], vertical_shift)
            self.init_button(name, click_func, place)
