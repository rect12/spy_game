from PyQt5.QtGui import QFont
from ._base_window import BaseWindow
from ._window_help import Timer


class GameWindow(BaseWindow):
    def __init__(self, view):
        super().__init__(view, 'Game')

        self.label_size = (200, 50)
        self.label_font = QFont('Times', 20)

    def _post_init(self):
        super()._post_init()
        place = [self.size().width()/2 - self.label_size[0]/2, self.pad[1]]
        self.timer = Timer(self.view.game.epoch_duration,
                           place,
                           self,
                           self.view.game.time_left_newsletter,
                           self.view.game.game_over,
                           self.buttons['to main'].hide)

    def set_geometry(self):
        self.resize(300, 300)

    def init_buttons(self):
        place = [self.size().width()/2 - self.buttons_size[0]/2,
                 self.size().height() - self.pad[1] - self.buttons_size[1]]
        self.init_button('to main', place)
        self.connect(self.buttonss['to main'].clicked,
                     self.view.window_change,
                     self,
                     self.view.windows['main'])

    def to_game(self):
        self.timer.set_epoch_number(self.view.get_duration())
        self.show()
