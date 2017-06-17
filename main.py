#!/usr/bin/python

from game import Game

from PyQt5.QtWidgets import QApplication
import os
import pandas as pd
import sys


def main():
    application = QApplication(sys.argv)
    game = Game(application)
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
