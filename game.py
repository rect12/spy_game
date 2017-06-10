from windows import WINDOWS, MainWindow, PlayerOptionsWindow


class Game:
    def __init__(self):
        windows = [MainWindow, PlayerOptionsWindow]
        self.windows = {name: window(self)
                        for name, window in zip(WINDOWS, windows)}
        for window in self.windows.values():
            window._post_init()
