from ._base_window import BaseWindow
from ._window_help import WINDOWS, WindowChange, ToGame


class MainWindow(BaseWindow):
    def __init__(self, game):
        self.buttons_number = 4
        super().__init__(game, 'The Spy')
        self.show()

    def set_geometry(self):
        self.resize(self.pad[0] * 2 + self.buttons_size[0],
                    self.pad[1] * (self.buttons_number + 1) +
                    self.buttons_number * self.buttons_size[1])

    def init_buttons(self):
        names = WINDOWS[1:]
        click_functions = [WindowChange(self, self.game.windows[name])
                           for name in names[:-1]]
        click_functions.append(ToGame(self.game))

        for ind, (name, click_func) in enumerate(zip(names, click_functions)):
            vertical_size = self.buttons_size[1] + self.pad[1]
            vertical_shift = self.pad[1] + ind*vertical_size
            place = (self.pad[0], vertical_shift)
            self.init_button(name, click_func, place)
