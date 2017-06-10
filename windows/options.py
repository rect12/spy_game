from ._base_options import BaseOptionsWindow


class PlayerOptionsWindow(BaseOptionsWindow):
    def __init__(self, game):
        super().__init__(game, 'Player options')

    def set_geometry(self):
        self.resize(300, 300)
