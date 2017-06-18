import sys
from PyQt5.QtWidgets import QApplication

from windows import WINDOWS, MainWindow, PlayerOptionsWindow
from windows import GameOptionsWindow, SettingOptionsWindow
from windows import GameWindow

class View:
    def __init__(self, game, players, settings):
        self.game = game
        self.application = QApplication(sys.argv)
        window_classes = [MainWindow, PlayerOptionsWindow, GameOptionsWindow,
                          SettingOptionsWindow, GameWindow]
        init_arguments = [{}, {'players': players}, {},
                          {'settings': settings}, {}]

        self.windows = {name: window(self, **kwargs)
                        for name, window, kwargs
                        in zip(WINDOWS, window_classes, init_arguments)}

        for window in self.windows.values():
            window._post_init()

    def show(self):
        sys.exit(self.application.exec_())

    def get_location(self):
        return self.windows['setting options'].line_edits[0].text()

    def get_roles(self):
        return [line_edit.text()
                for line_edit
                in self.windows['setting options'].line_edits[1:-1]]

    def get_duration(self):
        return int(self.windows['game options'].line_edits[0].text())

    def get_players(self, need_all):
        players = []
        po_window = self.windows['player options']
        for player_ind in range(len(po_window.line_edits) // 2 - 1):
            name = po_window.line_edits[2*player_ind].text()
            user_id = po_window.line_edits[2*player_ind + 1].text()

            if need_all or po_window.check_boxes[player_ind].isChecked():
                players.append([name, user_id])
        return players

    def to_game(self):
        for window in self.windows.values():
            window.hide()

        self.windows['game'].to_game()
        self.game.update_data()

        self.game.to_game()

    def add_new_line(self, line_edit, window):
        line_edit.textEdited.disconnect()
        window.init_new_line()

    def window_change(self, first_window, second_window):
        first_window.hide()
        second_window.show()

    def delete_default_text(self, line_edit, default_text):
        if line_edit.text() == default_text:
            line_edit.clear()
            event_function = lambda: self.return_default_text(line_edit,
                                                              default_text)
            line_edit.cursorPositionChanged.disconnect()
            line_edit.editingFinished.connect(event_function)

    def return_default_text(self, line_edit, default_text):
        if line_edit.text() == '':
            line_edit.setText(default_text)
            event_function = lambda: self.delete_default_text(line_edit,
                                                              default_text)
            line_edit.cursorPositionChanged.connect(event_function)
            line_edit.editingFinished.disconnect()

    def allow_only_numbers(self, line_edit, window):
        if line_edit.text().isdigit():
            error = ''
        else:
            line_edit.setText('')
            error = 'Time should be an integer'

        window.labels['error'].setText(error)
