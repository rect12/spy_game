from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QDesktopWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.buttons_number = 4
        self.buttons_size = (100, 50)
        self.pad = (30, 20)
        self.setWindowTitle('The Spy')
        self.set_geometry()
        self.init_buttons()
        self.show()

    def set_geometry(self):
        self.setGeometry(0, 0, self.pad[0] * 2 + self.buttons_size[0],
                         self.pad[1] * (self.buttons_number + 1) +
                         self.buttons_number * self.buttons_size[1])
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def init_buttons(self):
        self.buttons = {}
        names = ['player options',
                 'game options',
                 'setting options',
                 'start game']

        click_functions = [lambda x: None] * 4

        for name, click_func in zip(names, click_functions):
            self.init_button(name, click_func)
            print(name)

    def init_button(self, name, click_function, title=None):
        if title is None:
            title = name.capitalize()
        self.buttons[name] = QPushButton(title, self)
        self.buttons[name].clicked.connect(click_function)

        vertical_size = self.buttons_size[1] + self.pad[1]
        vertical_shift = self.pad[1] + (len(self.buttons) - 1)*vertical_size
        self.buttons[name].setGeometry(self.pad[0],
                                       vertical_shift,
                                       self.buttons_size[0],
                                       self.buttons_size[1])
        self.buttons[name].show()
