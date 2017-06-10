#!/usr/bin/python

from vk_helper import _vk_autorization
from vk_account import LOGIN, PASSWORD
from csv_helper import USERS, LOCATIONS, add_user, add_location, SEP

from windows import MainWindow
from game import Game

from PyQt5.QtWidgets import QApplication
import os
import pandas as pd
import sys


def main():
    if not os.path.exists(LOCATIONS):
        pd.DataFrame(columns=['Location', 'Role']).to_csv(LOCATIONS,
                                                          index=False,
                                                          sep=SEP)
    if not os.path.exists(USERS):
        pd.DataFrame(columns=['Name', 'ID']).to_csv(USERS,
                                                    index=False,
                                                    sep=SEP)
    app = QApplication(sys.argv)
    game = Game()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
