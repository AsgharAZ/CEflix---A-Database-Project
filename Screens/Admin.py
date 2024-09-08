from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox, QApplication
import sys

class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        try:
            uic.loadUi('login.ui', self)  # Load the UI file for login
        except Exception as e:
            print(f"Error loading UI file: {e}")

        # Find the buttons and input fields
        self.sign_in_button = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.lineEdit = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.lineEdit_2 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_2')
        
        # Connect the buttons to their respective functions
        self.sign_in_button.pressed.connect(self.login_decider)

    # Simulating a user database
    user_database = {'sadiqah.admin': '123', 'lyeba.admin': '123', 'Asghar.admin': '123'}

    def login_decider(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        
        if username in self.user_database and password == self.user_database[username]:
            user_type = "admin" if username.split(".")[1] == "admin" else "user"
            print(f"{username.split('.')[0]} logged in successfully as: {user_type}")
            if user_type == 'admin':
                self.switch_to_main_screen()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    def switch_to_main_screen(self):
        self.main_screen = MainScreen()
        self.main_screen.show()
        self.close()  # Close the login window


class MainScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        try:
            uic.loadUi('Proposal_screen_g.ui', self)  # Load the admin screen UI
            print("Switched to admin main screen: proposal_screen_g.ui")
        except Exception as e:
            print(f"Error loading UI file: {e}")

        self.add_movie_button = self.findChild(QtWidgets.QPushButton, 'pushButton_2')

        self.add_movie_button.pressed.connect(self.switch_to_add_movie_screen)

    def switch_to_add_movie_screen(self):
        self.movie_screen = AddMovieScreen()
        self.movie_screen.show()
        self.close()  # Close the admin main window

class AddMovieScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(AddMovieScreen, self).__init__()
        try:
            uic.loadUi('Proposal_screen_h.ui', self)  # Load the add movie screen UI
            print("Switched to add movie screen: proposal_screen_h.ui")
        except Exception as e:
            print(f"Error loading UI file: {e}")

        # Initialize the movie database
        self.movie_database = {}

        self.Genre = self.findChild(QtWidgets.QLineEdit, 'lineEdit3')
        self.Movie_name = self.findChild(QtWidgets.QLineEdit, 'lineEdit_2')   
        self.date = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.summary = self.findChild(QtWidgets.QLineEdit, 'lineEdit_4')
        self.duration = self.findChild(QtWidgets.QLineEdit, 'lineEdit_5')
        self.crew = self.findChild(QtWidgets.QLineEdit, 'lineEdit_6')
        self.okay_button = self.findChild(QtWidgets.QPushButton, 'pushButton_2')

        self.okay_button.pressed.connect(self.add_movie)

    def add_movie(self):
        print(self.movie_database)
        Movie_name = self.lineEdit_2.text()
        Genre = self.lineEdit_3.text()
        Date = self.lineEdit.text()
        Summary = self.lineEdit_4.text()
        Duration = self.lineEdit_5.text()
        Crew = self.lineEdit_6.text()
        self.movie_database[Movie_name] = [Genre, Date, Summary, Duration, Crew]
        print(self.movie_database)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
