import PyQt5.QtCore as QtCore

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QPushButton
import time


WINDOWS = ['main', 'player options', 'game options',
           'setting options', 'game']
LOCATION = 'Локация'
ROLE = 'Роль'
NAME = 'Имя'
ID = 'ID'


class Timer:
    # TODO: Add pause button
    # TODO (but it realy can wait): Make format argument somehow
    # TODO (but it realy can wait): Rewrite to QWidget interface
    """
    Timer Widget. Has 'Start' and 'Stop' buttons and shows

    how much time is left.

    It is assumed that tick_duration is one second.

    In this case time is shown in format 'minutes:seconds'.

    If you specify end_epoch_function and epoch_duration each

    epoch_duration of tick end_epoch_function will be executed.

    Description of init parametrs:

    parent - parent Widget

    place - place in parent Widget (pixels)

    size - Widget size (pixels)

    tick_duration - duration of one tick in milliseconds.

    After each tick the remaining time decreases for a second.

    epoch_duration and end_epoch_function - look above, if it is not clear

    end_function - if 'Stop' button is pressed it will be executed with

    True argument, in case of timeout it will be executed with False argument.

    start_funcion - it will be executed if 'Start' button is pressed.
    """
    def __init__(self, parent, place, size, epoch_duration,
                 end_epoch_function=None, end_function=None,
                 start_funcion=None, tick_duration=1000):
        # if you want to know WTF is this
        # 5/12 + 5/12 + 1/6 = 1
        # TODO: remove magic numbers
        self.time_left = 0
        self.label_size = (size[0], size[1] * 5 / 12)
        self.label_font = QFont('Times', size[1] / 4)
        self.pad = (size[0] * 3 / 20, size[1] / 6)
        self.buttons_size = (self.label_size[0]/2-self.pad[0]/2,
                             size[1] * 5 / 12)

        self.epoch_duration = epoch_duration
        self.tick_duration = tick_duration
        self.end_epoch_function = end_epoch_function
        self.end_function = end_function
        self.start_funcion = start_funcion
        self.parent = parent
        self._init_gui(place)
        self._init_timers()

    def set_epoch_number(self, epoch_number):
        self.epoch_number = epoch_number

    def _init_gui(self, place):
        self.label = QLabel(self.get_time_left_str(), self.parent)
        self.label.move(*place)
        self.label.resize(*self.label_size)
        self.label.setFont(self.label_font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        button_place = [place[0],
                        place[1] + self.label_size[1] + self.pad[1]]
        self._init_button('Start', button_place, self.start)

        button_place[0] += self.pad[0] + self.buttons_size[0]
        self._init_button('Stop', button_place, self.stop)

    def _init_button(self, text, place, click_function):
        button = QPushButton(text, self.parent)
        button.resize(*self.buttons_size)
        button.move(*place)
        button.clicked.connect(click_function)

    def _init_timers(self):
        self.small_timer = QTimer()
        self.small_timer.timeout.connect(self._tick)
        self.small_timer.setInterval(self.tick_duration)

        self.epoch_timer = QTimer()
        if self.end_epoch_function is not None:

            def event_function():
                self.end_epoch_function(self.time_left)

            self.epoch_timer.timeout.connect(event_function)
        self.epoch_timer.setInterval(self.tick_duration * self.epoch_duration)

    def start(self):
        self.time_left = self.epoch_duration * self.epoch_number
        self.update_label()
        if self.start_funcion is not None:
            self.start_funcion()

        self.small_timer.start()
        self.epoch_timer.start()

    def stop(self):
        self.small_timer.stop()
        self.epoch_timer.stop()
        if self.end_function is not None:
            self.end_function(True)

    def update_label(self):
        self.label.setText(self.get_time_left_str())

    def _tick(self):
        self.time_left -= 1
        self.update_label()
        if self.time_left == 0:
            self.small_timer.stop()
            self.epoch_timer.stop()
            if self.end_function is not None:
                self.end_function(False)

    def get_time_left_str(self):
        return seconds_to_time(self.time_left)


def seconds_to_time(time):
    minutes = add_zero(time // 60)
    seconds = add_zero(time % 60)
    return "{}:{}".format(minutes, seconds)


def add_zero(value):
    return str(value) if value > 9 else '0' + str(value)
