WINDOWS = ['main', 'player options', 'game options',
           'setting options', 'game']


class WindowChange:
    def __init__(self, first_window, second_window):
        self.first_window = first_window
        self.second_window = second_window

    def __call__(self):
        self.first_window.hide()
        self.second_window.show()
