from ._base_options import BaseOptionsWindow
from ._window_help import UpdatePlayerState

from importlib.machinery import SourceFileLoader
import pandas as pd
from PyQt5.QtWidgets import QLineEdit, QCheckBox


csv = SourceFileLoader('csv', 'csv_helper.py').load_module()


class PlayerOptionsWindow(BaseOptionsWindow):
    def __init__(self, game):
        self.line_edit_size = (100, 30)
        self.check_box_size = (30, 30)
        self.line_edits = []
        super().__init__(game, 'Player options')
        self.init_player_lines()

    def set_geometry(self):
        shift = self.line_edit_size[1] + self.pad[1]
        y_size = (len(self.line_edits)*shift/2 +
                  self.pad[1]*2 +
                  self.buttons_size[1])
        x_size = (2*(self.line_edit_size[0] + self.pad[0]) +
                  2*self.pad[0] + self.check_box_size[0])
        self.resize(x_size, y_size)

    def init_player_lines(self):
        players = pd.read_csv(csv.USERS, header=0, sep=csv.SEP).values
        self.check_boxes = []

        for ind_y, (name, user_id) in enumerate(players):
            for ind_x, text in enumerate([name, user_id]):
                self.line_edits.append(QLineEdit(str(text), self))
                self.line_edits[-1].resize(*self.line_edit_size)

                move = [pad + ind*(pad+size) for pad, ind, size
                        in zip(self.pad, [ind_x, ind_y], self.line_edit_size)]
                self.line_edits[-1].move(*move)

            self.check_boxes.append(QCheckBox(self))
            self.check_boxes[-1].resize(*self.check_box_size)
            move[0] += self.pad[0] + self.line_edit_size[0]
            self.check_boxes[-1].move(*move)
            click_function = UpdatePlayerState(self, ind_y)
            self.check_boxes[-1].stateChanged.connect(click_function)

        self.set_geometry()


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
