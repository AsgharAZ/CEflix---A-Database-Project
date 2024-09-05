from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox  # Import QMessageBox correctly
import sys

class Movie_Details(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(Movie_Details, self).__init__()
        # Load the .ui file
        uic.loadUi('Movie_Details.ui', self)
        
        