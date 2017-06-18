from PyQt5.QtWidgets import QLineEdit, QCheckBox
from ._base_window import BaseWindow


class BaseOptionsWindow(BaseWindow):
    def __init__(self, view, title, line_edit_size=(130, 30)):
        self.line_edits = []
        self.check_boxes = []

        self.line_edit_size = line_edit_size
        self.check_box_size = (30, 30)

        super().__init__(view, title)

    def get_buttons_places(self):
        return [(self.size().width() - self.pad[0] - self.buttons_size[0],
                 self.size().height() - self.pad[1] - self.buttons_size[1]),
                (self.pad[0], self.size().height() - self.pad[1] -
                 self.buttons_size[1])]

    def init_buttons(self):
        places = self.get_buttons_places()
        self.init_button('to main', places[1])
        self.connect(self.buttons['to main'].clicked,
                     self.view.window_change,
                     self,
                     self.view.windows['main'])

        self.init_button('to game', places[0])
        self.connect(self.buttons['to game'].clicked, self.view.to_game)

    def recover_geometry(self):
        # TODO: maybe should move it to BaseWindow
        self.set_geometry()
        places = self.get_buttons_places()
        for place, button in zip(places, sorted(self.buttons.keys())):
            self.buttons[button].move(*place)
        self.center()
