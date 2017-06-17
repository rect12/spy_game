from ._base_options import BaseOptionsWindow
from ._window_help import *

import pandas as pd


class PlayerOptionsWindow(BaseOptionsWindow):
    def __init__(self, view, players):
        super().__init__(view, 'Player options')
        self.init_player_lines(players)

    def set_geometry(self):
        shift = self.line_edit_size[1] + self.pad[1]
        y_size = (len(self.line_edits)*shift/2 +
                  self.pad[1]*2 +
                  self.buttons_size[1])
        x_size = (2*(self.line_edit_size[0] + self.pad[0]) +
                  2*self.pad[0] + self.check_box_size[0])
        self.resize(x_size, y_size)

    def init_player_lines(self, players):
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
            self.init_line_edit(text, move)
            if is_last and ind_x == 0:
                edit_function = lambda: self.view.add_new_line(self.line_edits[-1],
                                                               self)
                self.line_edits[-1].textEdited.connect(edit_function)

        if need_check_box:
            move = [self.pad[0]*3 + self.line_edit_size[0]*2,
                    ind_y*(self.pad[1] + self.line_edit_size[1]) +
                    self.pad[1]]
            if is_last:
                move[1] -= self.pad[1] + self.line_edit_size[1]
            self.init_check_box(move)

        self.recover_geometry()


class GameOptionsWindow(BaseOptionsWindow):
    def __init__(self, view):
        self.label_size = (230, 30)

        super().__init__(view, 'Game options', (30, 30))
        self.init_label('error', self.pad, '')
        self.init_time_options()

    def set_geometry(self):
        # TODO write this correctly
        self.resize(self.label_size[0] + self.pad[0]*3 +
                    self.line_edit_size[0], 300)

    def init_time_options(self):
        label_place = [self.pad[0], self.pad[1]*2 + self.label_size[1]]
        self.init_label('Длительность игры (в минутах)', label_place)
        place = [self.pad[0]*2 + self.label_size[0],
                 label_place[1]]
        self.init_line_edit('10', place)
        event_method = self.view.allow_only_numbers
        event_function = lambda: event_method(self.line_edits[-1],
                                              self)
        self.line_edits[-1].textEdited.connect(event_function)


class SettingOptionsWindow(BaseOptionsWindow):
    def __init__(self, view, settings):
        super().__init__(view, 'Setting options')
        self.init_location_line()

    def set_geometry(self):
        shift = self.line_edit_size[1] + self.pad[1]
        y_size = (len(self.line_edits)*shift +
                  self.pad[1]*2 +
                  self.buttons_size[1])
        x_size = 2*self.buttons_size[0] + 3*self.pad[0]
        self.resize(x_size, y_size)

    def init_location_line(self):
        # TODO: remove this method. Put its logic to init_new_line
        self.init_line_edit(LOCATION, self.pad)
        edit_function = lambda: self.view.add_new_line(self.line_edits[-1],
                                                       self)
        self.line_edits[-1].textEdited.connect(edit_function)

        event_method = self.view.delete_default_text
        event_function = lambda: event_method(self.line_edits[-1], LOCATION)
        self.line_edits[-1].cursorPositionChanged.connect(event_function)
        self.set_geometry()

    def init_new_line(self):
        shift = self.line_edit_size[1] + self.pad[1]
        y_move = len(self.line_edits)*shift + self.pad[1]
        self.init_line_edit(ROLE, [self.pad[0], y_move])
        edit_function = lambda: self.view.add_new_line(self.line_edits[-1],
                                                       self)
        self.line_edits[-1].textEdited.connect(edit_function)

        event_method = self.view.delete_default_text
        event_function = lambda: event_method(self.line_edits[-1], ROLE)
        self.line_edits[-1].cursorPositionChanged.connect(event_function)

        self.recover_geometry()
