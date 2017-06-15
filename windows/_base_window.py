from PyQt5.QtWidgets import QWidget, QPushButton, QDesktopWidget, QLabel
from PyQt5.QtGui import QFont
import PyQt5.QtCore as QtCore

class BaseWindow(QWidget):
    def __init__(self, game, title):
        # TODO: rewrite all size params to init arguments.
        # In _base_options same thing
        super().__init__()

        self.game = game
        self.buttons = {}
        self.labels = {}
        self.label_font = QFont('Times', 10)

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

    def init_button(self, name, click_function, place, title=None):
        if title is None:
            title = name.capitalize()
        self.buttons[name] = QPushButton(title, self)
        self.buttons[name].clicked.connect(click_function)
        self.buttons[name].resize(*self.buttons_size)
        self.buttons[name].move(*place)
        self.buttons[name].show()

    def init_label(self, name, place, text=None):
        if text is None:
            text = name
        self.labels[name] = QLabel(text, self)
        self.labels[name].move(*place)
        self.labels[name].resize(*self.label_size)
        self.labels[name].setFont(self.label_font)
        self.labels[name].setAlignment(QtCore.Qt.AlignCenter)
