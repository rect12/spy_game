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
        click_method = self.view.window_change
        click_function = lambda: click_method(self, self.view.windows['main'])
        self.init_button('to main page',
                         click_function,
                         places[1])
        self.init_button('to game', self.view.to_game, places[0])

    def init_line_edit(self, text, place):
        # TODO: maybe should move it to BaseWindow
        self.line_edits.append(QLineEdit(str(text), self))
        self.line_edits[-1].resize(*self.line_edit_size)
        self.line_edits[-1].move(*place)
        self.line_edits[-1].show()

    def init_check_box(self, place, click_function=None):
        # TODO: maybe should move it to BaseWindow
        self.check_boxes.append(QCheckBox(self))
        self.check_boxes[-1].move(*place)
        self.check_boxes[-1].resize(*self.check_box_size)
        if click_function is not None:
            self.check_boxes[-1].stateChanged.connect(click_function)
        self.check_boxes[-1].show()

    def recover_geometry(self):
        # TODO: maybe should move it to BaseWindow
        self.set_geometry()
        places = self.get_buttons_places()
        for place, button in zip(places, sorted(self.buttons.keys())):
            self.buttons[button].move(*place)
        self.center()
