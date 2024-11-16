from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic
from database import authenticate_user, authenticate_admin

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('login.ui', self)
        self.loginButton.clicked.connect(self.login)

    def login(self):
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()

        if username.endswith(".admin"):
            if authenticate_admin(username, password):
                self.open_admin_screen()
            else:
                QMessageBox.warning(self, "Login Failed", "Invalid admin username or password.")
        else:
            if authenticate_user(username, password):
                self.open_user_screen()
            else:
                QMessageBox.warning(self, "Login Failed", "Invalid user username or password.")

    def open_admin_screen(self):
        from ui_admin import AdminScreen
        self.admin_screen = AdminScreen()
        self.admin_screen.show()
        self.close()

    def open_user_screen(self):
        from ui_user import UserScreen
        self.user_screen = UserScreen()
        self.user_screen.show()
        self.close()
