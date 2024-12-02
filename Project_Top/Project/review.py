from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox, QApplication, QGraphicsView, QGraphicsScene, QFileDialog, QWidget, QVBoxLayout, QPushButton # Import QMessageBox correctly
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QRectF  # Ensure this import is correct
import sys
import pyodbc
import os  # Import os module to handle file paths

# Replace these with your own database connection details
server = 'CEflix'
database = 'DESKTOP-JBCSQ90\\MYSQLSERVER'  # Name of your Northwind database
use_windows_authentication = True  # Set to True to use Windows Authentication

# Create the connection string based on the authentication method chosen
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

class review(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        
        super(review, self).__init__()
        # Load the .ui file
        uic.loadUi('screens_final/reviews.ui', self)
        
        # Step 1: Prompt for Movie_ID and User_ID
        movie_id, ok1 = QtWidgets.QInputDialog.getInt(self, "Input Movie_ID", "Enter Movie_ID:")
        if not ok1:
            return  # Exit if user cancels the input
    
        user_id, ok2 = QtWidgets.QInputDialog.getInt(self, "Input User_ID", "Enter User_ID:")
        if not ok2:
            return  # Exit if user cancels the input
        
        # Store movie_id and user_id as instance variables
        self.movie_id = movie_id
        self.user_id = user_id
        
        # Load Orders data
        self.populate_table(movie_id, user_id)
        
    def populate_table(self, movie_id, user_id):
                    # Step 2: Establish database connection
            try:
                connection = pyodbc.connect(
                "Driver={SQL Server};"
                "Server=DESKTOP-JBCSQ90\\MYSQLSERVER1;"
                "Database=CEflix;"
               "Trusted_Connection=yes;"
            )
            except pyodbc.Error as ex:
                QMessageBox.critical(self, "Database Error", f"Connection failed: {ex}")
                return
            cursor = connection.cursor()
            # Step 3: Execute query to fetch reviews for the specified movie and user
            query = f"""
            SELECT Review_ID, Rating, Review_Description, Num_Of_Likes, Date
            FROM Review
            WHERE Movie_ID = {movie_id}
            """
            # WHERE User_ID = {user_id} AND Movie_ID = {movie_id}
            cursor.execute(query)
            reviews = cursor.fetchall()

            # Step 4: Populate the QTableWidget with the review data
            if reviews:
                self.ReviewTable.setRowCount(len(reviews))  # Set number of rows
                self.ReviewTable.setColumnCount(5)  # Set number of columns

                # Set the column headers
                self.ReviewTable.setHorizontalHeaderLabels(["UserID", "Rating", "Description", "Likes", "Date"])

                # Populate the table with the review data
                for row, review in enumerate(reviews):
                    for col, value in enumerate(review):
                        self.ReviewTable.setItem(row, col, QtWidgets.QTableWidgetItem(str(value)))
            else:
                QMessageBox.information(self, "No Reviews", "No reviews found for this movie and user.")

            # Close the database connection
            connection.close()
        



app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
window = review()  # Create an instance of our UI class
window.show()  # Show the UI
app.exec()  # Start the application