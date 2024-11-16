from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class UserScreen(QMainWindow):
    def __init__(self):
        super(UserScreen, self).__init__()
        uic.loadUi('user_screen.ui', self)
