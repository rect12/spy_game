from PyQt5.QtGui import QFont, QFontMetrics
from ._base_window import BaseWindow
from ._window_help import Timer


class GameWindow(BaseWindow):
    def __init__(self, view):
        super().__init__(view, 'Game')

        self.label_size = (300, 30)
        self.timer_size = (200, 120)

    def get_button_place(self):
        return [self.size().width()/2 - self.buttons_size[0]/2,
                self.size().height() - self.pad[1] - self.buttons_size[1]]

    def set_geometry(self):
        self.width_minimun = 300
        self.resize(self.width_minimun, 300)

    def recover_geometry(self):
        self.resize(self.get_width(),
                    self.timer_size[1] +
                    self.buttons_size[1] +
                    self.label_size[1]*len(self.labels) +
                    self.pad[1]*(len(self.labels) + 3))
        self.buttons['to main'].move(*self.get_button_place())
        self.center()

    def init_buttons(self):
        place = self.get_button_place()
        self.init_button('to main', place)
        self.connect(self.buttons['to main'].clicked,
                     self.view.window_change,
                     self,
                     self.view.windows['main'])

    def get_width(self):
        return max(self.width_minimun, self.pad[1]*2 +
                   max(label.size().width()
                       for label in self.labels.values()))

    def to_game(self):
        first = self.view.game.first_player[0]
        asking_first = 'Первым спрашивает: {}'.format(first)
        place = [self.pad[0],
                 self.timer_size[1] +
                 self.pad[1]*2]
        self.init_label(asking_first, place)

        for player, role in zip(self.view.game.get_players_names(),
                                self.view.game.roles):
            place[1] += self.pad[1] + self.label_size[1]
            self.init_label('{} играет роль "{}"'.format(player, role), place)

        self.recover_geometry()
        place = [self.size().width()/2 - self.timer_size[0]/2, self.pad[1]]
        self.timer = Timer(self,
                           place,
                           self.timer_size,
                           self.view.game.epoch_duration,
                           self.view.game.time_left_newsletter,
                           self.view.game.game_over,
                           self.view.game.start_game)
        self.timer.set_epoch_number(self.view.get_duration())

        self.show()
