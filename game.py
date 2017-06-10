from windows import WINDOWS, MainWindow, PlayerOptionsWindow
from windows import GameOptionsWindow, SettingOptionsWindow
from windows import GameWindow


class Game:
    def __init__(self):
        self.players = []

        windows = [MainWindow, PlayerOptionsWindow, GameOptionsWindow,
                   SettingOptionsWindow, GameWindow]
        self.windows = {name: window(self)
                        for name, window in zip(WINDOWS, windows)}

        for window in self.windows.values():
            window._post_init()
