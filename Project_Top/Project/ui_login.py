from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic
from database import authenticate_admin

class LoginScreen(QMainWindow):
    def __init__(self):
        super(LoginScreen, self).__init__()
        uic.loadUi('screens_final/login.ui', self)

        # Connect the login button
        self.pushButton.clicked.connect(self.login)

    def login(self):
        """
        Handle user/admin login.
        """
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if username.endswith(".admin"):
            admin_id = authenticate_admin(username, password)
            if admin_id:
                self.open_admin_main_screen(admin_id)
            else:
                QMessageBox.warning(self, "Login Failed", "Invalid admin username or password.")
        else:
            # Logic for user login (if applicable)
            pass

    def open_admin_main_screen(self, admin_id):
        """
        Opens the Admin_Main_Screen for the logged-in admin.

        :param admin_id: The ID of the logged-in admin.
        """
        from ui_admin_main import AdminMainScreen
        self.admin_main_screen = AdminMainScreen(admin_id)
        self.admin_main_screen.show()
        self.close()
