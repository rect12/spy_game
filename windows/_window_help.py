WINDOWS = ['main', 'player options', 'game options',
           'setting options', 'game']


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
