from ._base_options import BaseOptionsWindow


class PlayerOptionsWindow(BaseOptionsWindow):
    def __init__(self, game):
        super().__init__(game, 'Player options')

    def set_geometry(self):
        self.resize(300, 300)


class GameOptionsWindow(BaseOptionsWindow):
    def __init__(self, game):
        super().__init__(game, 'Game options')

    def set_geometry(self):
        self.resize(300, 300)

class SettingOptionsWindow(BaseOptionsWindow):
    def __init__(self, game):
        super().__init__(game, 'Game options')

    def set_geometry(self):
        self.resize(300, 300)
