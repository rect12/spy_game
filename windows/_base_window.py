from PyQt5.QtWidgets import QWidget, QPushButton, QDesktopWidget, QLabel
from PyQt5.QtWidgets import QLineEdit, QCheckBox
from PyQt5.QtGui import QFont
import PyQt5.QtCore as QtCore


class BaseWindow(QWidget):
    def __init__(self, view, title):
        # TODO: rewrite all size params to init arguments.
        # TOD): DO IT!!!
        super().__init__()

        self.view = view
        self.buttons = {}
        self.labels = {}
        self.label_font = QFont('Times', 10)
        self.label_size = (100, 30)

        self.buttons_size = (100, 50)
        self.pad = (30, 20)

        self.setWindowTitle(title)
        self.set_geometry()
        self.center()

    def _post_init(self):
        self.init_buttons()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def set_geometry(self):
        pass

    def init_buttons(self):
        pass

    def init_button(self, name, place, title=None):
        if title is None:
            title = name.capitalize()
        self.buttons[name] = QPushButton(title, self)
        self.buttons[name].resize(*self.buttons_size)
        self.buttons[name].move(*place)
        self.buttons[name].show()

    def init_label(self, name, place, text=None,
                   size=None, font=None):
        text = default_if_none(text, name)
        size = default_if_none(size, self.label_size)
        font = default_if_none(font, self.label_font)

        self.labels[name] = QLabel(text, self)
        self.labels[name].move(*place)
        self.labels[name].resize(*size)
        self.labels[name].setFont(font)
        self.labels[name].setAlignment(QtCore.Qt.AlignCenter)
        self.labels[name].show()

    def init_line_edit(self, text, place):
        self.line_edits.append(QLineEdit(str(text), self))
        self.line_edits[-1].resize(*self.line_edit_size)
        self.line_edits[-1].move(*place)
        self.line_edits[-1].show()

    def init_check_box(self, place):
        self.check_boxes.append(QCheckBox(self))
        self.check_boxes[-1].move(*place)
        self.check_boxes[-1].resize(*self.check_box_size)
        self.check_boxes[-1].show()

    @staticmethod
    def connect(event, function, *args, **kwargs):
        event.connect(lambda: function(*args, **kwargs))


def default_if_none(value, default):
    return default if value is None else value
