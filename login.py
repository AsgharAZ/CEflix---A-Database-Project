import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic  # for loading the .ui file

# Load the UI from the .ui file
class LoginScreen(QMainWindow):
    def __init__(self):
        super(LoginScreen, self).__init__()
        uic.loadUi("login.ui", self)  # Load the .ui file

        # Get references to the UI elements
        self.lineEdit= self.findChild(QLineEdit, 'usernameLineEdit')
        self.password_input = self.findChild(QLineEdit, 'passwordLineEdit')
        self.login_button = self.findChild(QPushButton, 'loginButton')

        # Connect the login button to the login function
        self.login_button.clicked.connect(self.login)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Simple login check (you can replace this with database or more complex validation)
        if username == "admin" and password == "password":
            QMessageBox.information(self, "Login Successful", "Welcome!")
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password")

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginScreen()
    window.show()
    sys.exit(app.exec_())
