from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox, QApplication
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        try:
            uic.loadUi('login.ui', self)  # Load the UI file
        except Exception as e:
            print(f"Error loading UI file: {e}")

        # Find the button by its object name from Qt Designer (e.g., "pushButton")
        self.sign_in_button = self.findChild(QtWidgets.QPushButton, 'pushButton')
        
        # Find the username and password input fields by their object names
        self.lineEdit = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.lineEdit_2 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_2')
        
        # Connect the button press signal to the login_decider function
        self.sign_in_button.pressed.connect(self.login_decider)
        self.sign_in_button.pressed.connect(self.login_to_main)

    # Simulating a user database
    user_database = {'sadiqah.admin': '123', 'lyeba.admin': '123', 'Asghar.admin': '123'}

    def login_decider(self):
        username = self.lineEdit.text()  # Get username from the input field
        password = self.lineEdit_2.text()  # Get password from the input field
        
        if username in self.user_database and password == self.user_database[username]:
            # Split the username based on '.' and check if the second part is 'admin'
            user_type = "admin" if username.split(".")[1] == "admin" else "user"
            print(f"{username.split('.')[0]} logged in successfully as: {user_type}")
            return user_type
        else:
            # Display a warning message if login fails
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    def login_to_main(self):
        user_type = self.login_decider()
        if user_type == 'admin':
            try:
                uic.loadUi('Proposal_screen_g.ui', self)
                print("Switched to admin screen: proposal_screen_g.ui")
            except Exception as e:
                print(f"Error loading UI file: {e}")
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())