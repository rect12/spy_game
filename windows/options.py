from ._base_options import BaseOptionsWindow
from ._window_help import UpdatePlayerState, AddNewLine, DeleteDefaultText
from ._window_help import LOCATION, ROLE, NAME, ID

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
            self.init_new_line(name, user_id, False)
        self.init_new_line(need_check_box=False)

    def init_new_line(self, name=NAME, user_id=ID, is_last=True,
                      need_check_box=True):
        # TODO: rewrite this somehow
        ind_y = len(self.line_edits) // 2
        for ind_x, text in enumerate([name, user_id]):
             move = [pad + ind*(pad+size) for pad, ind, size
                     in zip(self.pad, [ind_x, ind_y], self.line_edit_size)]
             edit_class = AddNewLine if is_last and ind_x == 0 else None
             self.init_line_edit(text, move, edit_class)

        if need_check_box:
            move = [self.pad[0]*3 + self.line_edit_size[0]*2,
                    ind_y*(self.pad[1] + self.line_edit_size[1]) +
                    self.pad[1]]
            if is_last:
                move[1] -= self.pad[1] + self.line_edit_size[1]
            self.init_check_box(move)

        self.recover_geometry()


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
        self.init_line_edit(LOCATION, self.pad, AddNewLine)
        event_function = DeleteDefaultText(self.line_edits[-1], LOCATION)
        self.line_edits[-1].cursorPositionChanged.connect(event_function)
        self.set_geometry()

    def init_new_line(self):
        shift = self.line_edit_size[1] + self.pad[1]
        y_move = len(self.line_edits)*shift + self.pad[1]
        self.init_line_edit(ROLE, [self.pad[0], y_move], AddNewLine)
        event_function = DeleteDefaultText(self.line_edits[-1], ROLE)
        self.line_edits[-1].cursorPositionChanged.connect(event_function)

        self.recover_geometry()
