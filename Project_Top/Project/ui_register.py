from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
from database import register_user, register_admin

class RegisterScreen(QMainWindow):
    def __init__(self):
        super(RegisterScreen, self).__init__()
        uic.loadUi('screens_final/register.ui', self)
        self.registerButton.clicked.connect(self.register_user)

    def register_user(self):
        username = self.usernameLineEdit.text()
        email = self.emailLineEdit.text()
        password = self.passwordLineEdit.text()

        if username.endswith(".admin"):
            register_admin(username, email, password)
        else:
            register_user(username, email, password)

        self.open_login_screen()

    def open_login_screen(self):
        from ui_login import UI
        self.login_screen = UI()
        self.login_screen.show()
        self.close()
