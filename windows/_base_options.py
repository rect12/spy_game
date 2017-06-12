from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QCheckBox
from ._base_window import BaseWindow
from ._window_help import WindowChange, StartGame


class BaseOptionsWindow(BaseWindow):
    def __init__(self, game, title):
        self.line_edits = []
        self.check_boxes = []

        self.line_edit_size = (100, 30)
        self.check_box_size = (30, 30)

        super().__init__(game, title)

    def get_buttons_places(self):
        return [(self.size().width() - self.pad[0] - self.buttons_size[0],
                 self.size().height() - self.pad[1] - self.buttons_size[1]),
                (self.pad[0], self.size().height() - self.pad[1] -
                 self.buttons_size[1])]

    def init_buttons(self):
        places = self.get_buttons_places()
        self.init_button('to main page',
                         WindowChange(self, self.game.windows['main']),
                         places[1])
        self.init_button('start game', StartGame(self.game), places[0])

    def init_line_edit(self, text, place, edit_class):
        self.line_edits.append(QLineEdit(str(text), self))
        self.line_edits[-1].resize(*self.line_edit_size)
        self.line_edits[-1].move(*place)
        self.line_edits[-1].textEdited.connect(edit_class(self.line_edits[-1]))
        self.line_edits[-1].show()

    def init_check_box(self, place, click_function):
        self.check_boxes.append(QCheckBox(self))
        self.check_boxes[-1].move(*place)
        self.check_boxes[-1].resize(*self.check_box_size)
        self.check_boxes[-1].stateChanged.connect(click_function)

    def recover_geometry(self):
        self.set_geometry()
        places = self.get_buttons_places()
        for place, button in zip(places, sorted(self.buttons.keys())):
            self.buttons[button].move(*place)
        self.center()
