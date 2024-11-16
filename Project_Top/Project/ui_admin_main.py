from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
from ui_admin_add_movie import AdminAddMovieScreen

class AdminMainScreen(QMainWindow):
    def __init__(self, admin_id):
        """
        Initialize the Admin Main Screen.

        :param admin_id: The ID of the logged-in admin, passed from the login screen.
        """
        super(AdminMainScreen, self).__init__()
        uic.loadUi('screens_final/Admin_main.ui', self)

        # Store the admin_id for future use
        self.admin_id = admin_id

        # Connect the Add Movie button
        self.pushButton_2.clicked.connect(self.open_add_movie_screen)  # Add Movie button

    def open_add_movie_screen(self):
        """
        Opens the Admin_Add_Movie screen.
        """
        self.add_movie_screen = AdminAddMovieScreen(self.admin_id)
        self.add_movie_screen.show()
        self.close()