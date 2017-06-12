WINDOWS = ['main', 'player options', 'game options',
           'setting options', 'game']
LOCATION = 'Локация'
ROLE = 'Роль'


class WindowChange:
    def __init__(self, first_window, second_window):
        self.first_window = first_window
        self.second_window = second_window

    def __call__(self):
        self.first_window.hide()
        self.second_window.show()


class StartGame:
    def __init__(self, game):
        self.game = game

    def __call__(self):
        for window in self.game.windows.values():
            window.hide()
        self.game.windows['game'].show()


class UpdatePlayerState:
    def __init__(self, player_options_window, player_ind):
        self.po_window = player_options_window
        self.player_ind = player_ind

    def __call__(self):
        name = self.po_window.line_edits[2*self.player_ind].text()
        user_id = self.po_window.line_edits[2*self.player_ind + 1].text()

        if self.po_window.check_boxes[self.player_ind].isChecked():
            self.po_window.game.players.append((name, user_id))
        else:
            self.po_window.game.players.remove((name, user_id))


class AddNewLine:
    def __init__(self, line_edit):
        self.window = line_edit.parent()
        self.line_edit = line_edit

    def __call__(self):
        self.line_edit.textEdited.disconnect()
        self.line_edit.textEdited.connect(lambda x: None)
        self.window.init_new_line()


class DeleteDefaultText:
    # Doesn't work yet
    def __init__(self, line_edit, default_text):
        self.line_edit = line_edit
        self.default_text = default_text

    def __call__(self):
        text = self.line_edit.text()
        if text == self.default_text:
            self.line_edit.clear()
            print('delete', text)
            event_function = ReturnDefaultText(self.line_edit, text)
            self.line_edit.cursorPositionChanged.disconnect()
            self.line_edit.editingFinished.connect(event_function)


class ReturnDefaultText:
    # Doesn't work yet
    def __init__(self, line_edit, default_text):
        self.line_edit = line_edit
        self.default_text = default_text

    def __call__(self):
        if self.line_edit.text() == '':
            print('return', self.default_text)
            self.line_edit.setText(self.default_text)
            event_function = DeleteDefaultText(self.line_edit, self.default_text)
            self.line_edit.cursorPositionChanged.connect(event_function)
            self.line_edit.editingFinished.disconnect()
