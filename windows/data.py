class Data:
    def __init__(self)
        self.vk_client = _vk_autorization(LOGIN, PASSWORD)
        self.epoch_duration = 60

        windows = [MainWindow, PlayerOptionsWindow, GameOptionsWindow,
                   SettingOptionsWindow, GameWindow]
        self.windows = {name: window(self)
                        for name, window in zip(WINDOWS, windows)}

        for window in self.windows.values():
            window._post_init()

    def set_parametrs(self):
        self.location = self.get_location()
        self.roles = self.get_roles()
        self.players = self.get_players(False)

    def get_location(self):
        return self.windows['setting options'].line_edits[0].text()

    def get_roles(self):
        return [line_edit.text()
                for line_edit
                in self.windows['setting options'].line_edits[1:-1]]

    def get_duration(self):
        return int(self.windows['game options'].line_edits[0].text())

    def get_players_id(self):
        return [player[1] for player in self.players]

    def get_players(self, need_all):
        players = []
        po_window = self.windows['player options']
        for player_ind in range(len(po_window.line_edits) // 2 - 1):
            name = po_window.line_edits[2*player_ind].text()
            user_id = po_window.line_edits[2*player_ind + 1].text()

            if need_all or po_window.check_boxes[player_ind].isChecked():
                players.append([name, user_id])
        return players
