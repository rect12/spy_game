#!/usr/bin/python

from csv_helper import USERS, LOCATIONS, SEP

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
    application = QApplication(sys.argv)
    game = Game(application)
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
