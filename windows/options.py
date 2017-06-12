from ._base_options import BaseOptionsWindow
from ._window_help import UpdatePlayerState, AddNewLine, DeleteDefaultText

from importlib.machinery import SourceFileLoader
from PyQt5.QtWidgets import QLineEdit, QCheckBox

import pandas as pd

csv = SourceFileLoader('csv', 'csv_helper.py').load_module()


class PlayerOptionsWindow(BaseOptionsWindow):
    def __init__(self, game):
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

        for ind_y, (name, user_id) in enumerate(players):
            for ind_x, text in enumerate([name, user_id]):
                 move = [pad + ind*(pad+size) for pad, ind, size
                         in zip(self.pad, [ind_x, ind_y], self.line_edit_size)]
                 self.init_line_edit(text, move, lambda x: lambda x: None)


            move[0] += self.pad[0] + self.line_edit_size[0]
            click_function = UpdatePlayerState(self, ind_y)
            self.init_check_box(move, click_function)

        self.set_geometry()


class GameOptionsWindow(BaseOptionsWindow):
    def __init__(self, game):
        super().__init__(game, 'Game options')

    def set_geometry(self):
        self.resize(300, 300)


class SettingOptionsWindow(BaseOptionsWindow):
    def __init__(self, game):
        super().__init__(game, 'Setting options')
        self.init_location_line()

    def set_geometry(self):
        shift = self.line_edit_size[1] + self.pad[1]
        y_size = (len(self.line_edits)*shift +
                  self.pad[1]*2 +
                  self.buttons_size[1])
        x_size = 2*self.buttons_size[0] + 3*self.pad[0]
        self.resize(x_size, y_size)

    def init_location_line(self):
        default_text = 'Локация'
        self.init_line_edit(default_text, self.pad, AddNewLine)
        event_function = DeleteDefaultText(self.line_edits[-1], default_text)
        # self.line_edits[-1].cursorPositionChanged.connect(event_function)
        self.set_geometry()

    def init_new_line(self):
        pass
