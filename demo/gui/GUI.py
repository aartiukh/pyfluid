#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5 import uic


class mwindow(QWidget):

    m_ui = None

    def __init__(self):
        super().__init__()
        m_ui = uic.loadUi('GUI.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mwindow()
    ex.show()
    sys.exit(app.exec_())
