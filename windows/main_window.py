from ._base_window import BaseWindow
from ._window_help import WINDOWS


class MainWindow(BaseWindow):
    def __init__(self, view):
        self.buttons_number = 4
        super().__init__(view, 'The Spy')
        self.show()

    def set_geometry(self):
        self.resize(self.pad[0] * 2 + self.buttons_size[0],
                    self.pad[1] * (self.buttons_number + 1) +
                    self.buttons_number * self.buttons_size[1])

    def init_buttons(self):
        for ind, name in enumerate(WINDOWS[1:]):
            vertical_size = self.buttons_size[1] + self.pad[1]
            vertical_shift = self.pad[1] + ind*vertical_size
            place = (self.pad[0], vertical_shift)
            self.init_button(name, place)
            if name == 'game':
                self.connect(self.buttons[name].clicked, self.view.to_game)
            else:
                self.connect(self.buttons[name].clicked,
                             self.view.window_change,
                             self,
                             self.view.windows[name])
