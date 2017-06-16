from PyQt5.QtCore import QTimer
from importlib.machinery import SourceFileLoader
import time


csv = SourceFileLoader('csv', 'csv_helper.py').load_module()
vk = SourceFileLoader('vk', 'vk_helper.py').load_module()

WINDOWS = ['main', 'player options', 'game options',
           'setting options', 'game']
LOCATION = 'Локация'
ROLE = 'Роль'
NAME = 'Имя'
ID = 'ID'


class WindowChange:
    def __init__(self, first_window, second_window):
        self.first_window = first_window
        self.second_window = second_window

    def __call__(self):
        self.first_window.hide()
        self.second_window.show()


class ToGame:
    def __init__(self, game):
        self.game = game

    def __call__(self):
        for window in self.game.windows.values():
            window.hide()
        self.game.windows['game'].show()
        update_csv(self.game)

        self.game.to_game()


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


class BaseTextEditFunction:
    def __init__(self, line_edit):
        self.window = line_edit.parent()
        self.line_edit = line_edit


class AddNewLine(BaseTextEditFunction):
    def __call__(self):
        self.line_edit.textEdited.disconnect()
        self.line_edit.textEdited.connect(lambda x: None)
        self.window.init_new_line()


class DeleteDefaultText:
    def __init__(self, line_edit, default_text):
        self.line_edit = line_edit
        self.default_text = default_text

    def __call__(self):
        text = self.line_edit.text()
        if text == self.default_text:
            self.line_edit.clear()
            event_function = ReturnDefaultText(self.line_edit, text)
            self.line_edit.cursorPositionChanged.disconnect()
            self.line_edit.editingFinished.connect(event_function)


class ReturnDefaultText:
    def __init__(self, line_edit, default_text):
        self.line_edit = line_edit
        self.default_text = default_text

    def __call__(self):
        if self.line_edit.text() == '':
            self.line_edit.setText(self.default_text)
            event_function = DeleteDefaultText(self.line_edit,
                                               self.default_text)
            self.line_edit.cursorPositionChanged.connect(event_function)
            self.line_edit.editingFinished.disconnect()


class AllowOnlyNumbers(BaseTextEditFunction):
    def __call__(self):
        if self.line_edit.text().isdigit():
            error = ''
        else:
            self.line_edit.setText('')
            error = 'Time should be an integer'

        self.window.labels['error'].setText(error)


class Timer:
    def __init__(self, epoch_duration, epoch_number, place,
                 parent, end_epoch_function=None):
        self.epoch_duration = epoch_duration
        self.end_epoch_function = end_epoch_function
        self.epoch_number = epoch_number
        self.parent = parent
        self.init_gui(place)
        self.init_timer()

    def init_gui(self, place):
        self.parent.init_label('timer', place, self.get_time_left_str())
        button_place = [place[0] + self.parent.label_size[0]/2 -
                        self.parent.buttons_size[0]/2,
                        place[1] + self.parent.label_size[1] + self.parent.pad[1]]
        self.parent.init_button('START', self.run, button_place)

    def init_timer(self):
        self.small_timer = QTimer()
        self.small_timer.timeout.connect(self.tick)
        self.small_timer.setInterval(999.9) # in ms

    def run(self):
        for epoch_index in range(self.epoch_number):
            for _ in range(self.epoch_duration):
                self.small_timer.start()
            if self.end_epoch_function is not None:
                self.end_epoch_function(self.epoch_number - epoch_index - 1)

    def tick(self):
        label = self.parent.labels['timer']
        label.setText(self.get_time_left_str())

    def get_time_left_str(self):
        return seconds_to_time(self.time_left)


def update_csv(game):
    csv.add_location(game.get_location(), game.get_roles())
    all_players = game.get_players(True)
    csv._to_csv(csv.USERS, all_players)


def seconds_to_time(time):
    minutes = add_zero(time // 60)
    seconds = add_zero(time % 60)
    return "{}:{}".format(minutes, seconds)


def add_zero(value):
    return str(value) if value > 9 else '0' + str(value)
