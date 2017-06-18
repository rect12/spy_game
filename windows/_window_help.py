from PyQt5.QtCore import QTimer
import time


WINDOWS = ['main', 'player options', 'game options',
           'setting options', 'game']
LOCATION = 'Локация'
ROLE = 'Роль'
NAME = 'Имя'
ID = 'ID'


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
        self.parent.init_button('START', button_place)
        self.parent.buttons['START'].clicked.connect(self.run)

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


def seconds_to_time(time):
    minutes = add_zero(time // 60)
    seconds = add_zero(time % 60)
    return "{}:{}".format(minutes, seconds)


def add_zero(value):
    return str(value) if value > 9 else '0' + str(value)
