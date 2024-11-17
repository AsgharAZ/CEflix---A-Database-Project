from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic
from database import register_user, register_admin

class RegisterScreen(QMainWindow):
    def __init__(self):
        super(RegisterScreen, self).__init__()
        uic.loadUi('screens_final/register_final.ui', self)

        # Connect the Register button
        self.pushButton_2.clicked.connect(self.register_user)

    def register_user(self):
        """
        Validates input fields and registers a user or admin if valid.
        """
        # Retrieve input from fields
        username = self.lineEdit.text().strip()
        email = self.lineEdit_2.text().strip()
        password = self.lineEdit_3.text().strip()
        confirm_password = self.lineEdit_3.text().strip()
        terms_agreed = self.checkBox.isChecked()

        # Validation checks
        if not username or not email or not password or not confirm_password:
            QMessageBox.warning(self, "Input Error", "All fields are required.")
            return

        if password != confirm_password:
            QMessageBox.warning(self, "Input Error", "Passwords do not match.")
            return

        if not terms_agreed:
            QMessageBox.warning(self, "Terms and Conditions", "You must agree to the terms and conditions.")
            return

        # Register the user or admin
        try:
            if username.endswith(".admin"):
                register_admin(username, email, password)
            else:
                register_user(username, email, password)
            
            QMessageBox.information(self, "Success", "Registration successful.")
            self.open_login_screen()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Registration failed: {str(e)}")

    def open_login_screen(self):
        """
        Opens the login screen after successful registration.
        """
        from ui_login import LoginScreen  # Ensure correct class name
        self.login_screen = LoginScreen()
        self.login_screen.show()
        self.close()
