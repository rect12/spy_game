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
    def __init__(self, epoch_duration, place, parent,
                 end_epoch_function=None, end_function=None,
                 start_funcion=None):
        self.time_left = 0
        self.epoch_duration = epoch_duration
        self.end_epoch_function = end_epoch_function
        self.end_function = end_function
        self.start_funcion = start_funcion
        self.parent = parent
        self.init_gui(place)
        self.init_timers()

    def set_epoch_number(self, epoch_number):
        self.epoch_number = epoch_number

    def init_gui(self, place):
        self.parent.init_label('timer', place, self.get_time_left_str())
        button_place = [place[0] + self.parent.label_size[0]/2 -
                        self.parent.buttons_size[0]/2,
                        place[1] + self.parent.label_size[1] +
                        self.parent.pad[1]]
        self.parent.init_button('START', self.run, button_place)

    def init_timers(self):
        second = 1000  # in ms
        self.small_timer = QTimer()
        self.small_timer.timeout.connect(self.tick)
        self.small_timer.setInterval(second)

        self.epoch_timer = QTimer()
        if self.end_epoch_function is not None:
            event_function = lambda: self.end_epoch_function(self.time_left)
            self.epoch_timer.timeout.connect(event_function)
        self.epoch_timer.setInterval(second * self.epoch_duration)

    def run(self):
        self.time_left = self.epoch_duration * self.epoch_number
        self.update_label()
        if self.start_funcion is not None:
            self.start_funcion()

        self.small_timer.start()
        self.epoch_timer.start()

    def update_label(self):
        label = self.parent.labels['timer']
        label.setText(self.get_time_left_str())

    def tick(self):
        self.time_left -= 1
        self.update_label()
        if self.time_left == 0:
            self.small_timer.stop()
            self.epoch_timer.stop()
            if self.end_function is not None:
                self.end_function()

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
