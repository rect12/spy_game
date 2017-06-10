from windows import WINDOWS, MainWindow, PlayerOptionsWindow


class Game:
    def __init__(self):
        windows = [MainWindow(self), PlayerOptionsWindow(self)]
        self.windows = {name: window for name, window in zip(WINDOWS, windows)}
