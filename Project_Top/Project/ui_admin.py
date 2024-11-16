from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
from database import add_movie

class AdminScreen(QMainWindow):
    def __init__(self):
        super(AdminScreen, self).__init__()
        uic.loadUi('admin_screen.ui', self)
        self.InsertOrder.clicked.connect(self.add_movie)

    def add_movie(self):
        movie_name = self.lineEdit_2.text()
        genre = self.lineEdit_3.text()
        summary = self.lineEdit_4.text()
        year = self.lineEdit.text()
        duration = self.lineEdit_5.text()
        crew = self.lineEdit_6.text()

        add_movie(movie_name, genre, summary, year, duration, crew, self.admin_id)