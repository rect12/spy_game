from PyQt5.QtWidgets import QWidget, QPushButton, QDesktopWidget


class BaseWindow(QWidget):
    def __init__(self, game, title):
        super().__init__()

        self.game = game
        self.buttons = {}
        self.buttons_size = (100, 50)
        self.pad = (30, 20)

        self.setWindowTitle(title)
        self.set_geometry()
        self.init_buttons()
        self.center()

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
