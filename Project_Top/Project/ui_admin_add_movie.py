from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
from database import add_movie

class AdminAddMovieScreen(QMainWindow):
    def __init__(self, admin_id):
        """
        Initialize the Admin Add Movie Screen.

        :param admin_id: The ID of the logged-in admin, passed from Admin_Main_Screen.
        """
        super(AdminAddMovieScreen, self).__init__()
        uic.loadUi('screens_final/Admin_Add_Movie.ui', self)

        # Store the admin_id for associating with the movie
        self.admin_id = admin_id

        # Connect the Submit button
        self.pushButton_2.clicked.connect(self.add_movie)   # Okay button

        # Connect the Submit button
        self.pushButton_3.clicked.connect(self.go_back)   # Cancel button


    def add_movie(self):
        """
        Collects movie details from the form and adds the movie to the database.
        """
        # Retrieve data from input fields
        movie_name = self.lineEdit_2.text()
        genre = self.lineEdit_3.text()
        summary = self.lineEdit_4.text()
        year = self.lineEdit.text()
        duration = self.lineEdit_5.text()
        crew = self.lineEdit_6.text()

        # Add movie to the database
        add_movie(movie_name, genre, summary, year, duration, crew, self.admin_id)

        # Clear the form fields after successful submission
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()

    def go_back(self):
        """
        Navigate back to the Admin Main Screen.
        """
        from ui_admin_main import AdminMainScreen  # Delayed import to avoid circular dependency

        self.main_screen = AdminMainScreen(self.admin_id)
        self.main_screen.show()
        self.close()
