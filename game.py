from windows import WINDOWS, MainWindow, PlayerOptionsWindow
from windows import GameOptionsWindow, SettingOptionsWindow
from windows import GameWindow


class Game:
    def __init__(self, application):
        self.players = []
        self.roles = []
        self.application = application

        windows = [MainWindow, PlayerOptionsWindow, GameOptionsWindow,
                   SettingOptionsWindow, GameWindow]
        self.windows = {name: window(self)
                        for name, window in zip(WINDOWS, windows)}

        for window in self.windows.values():
            window._post_init()

    def set_parametrs(self):
        self.set_location()
        self.set_roles()
        self.set_players()

    def set_location(self):
        self.location = self.windows['setting options'].line_edits[0].text()

    def set_roles(self):
        for line_edit in self.windows['setting options'].line_edits[1:-1]:
            self.roles.append(line_edit.text())

    def set_players(self):
        po_window = self.windows['player options']
        for player_ind in range(len(po_window.line_edits) // 2 - 1):
            name = po_window.line_edits[2*player_ind].text()
            user_id = po_window.line_edits[2*player_ind + 1].text()

            if po_window.check_boxes[player_ind].isChecked():
                self.players.append([name, user_id])

    def get_all_players(self):
        all_players = []
        po_window = self.windows['player options']
        for player_ind in range(len(po_window.line_edits) // 2 - 1):
            name = po_window.line_edits[2*player_ind].text()
            user_id = po_window.line_edits[2*player_ind + 1].text()

            all_players.append([name, user_id])

        return all_players

