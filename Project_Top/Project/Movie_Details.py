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

class Movie_Details(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        
        super(Movie_Details, self).__init__()
        # Load the .ui file
        uic.loadUi('screens_final/Movie_Details.ui', self)
        
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

        # Connect Submit Button to Event Handling Code
        self.Update.clicked.connect(self.update_movie)
        movie_id = 0
        
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

        # Step 3: Execute main query
        query = f"""
        SELECT movie.Movie_ID, Movie_Name, Summary, Year, Admin_ID, Duration, User_ID, Watchlist, Favourite, Status
        FROM movie
        INNER JOIN User_Movie ON movie.Movie_ID = User_Movie.Movie_ID
        WHERE User_Movie.Movie_ID = {movie_id} OR User_ID = {user_id}
        """
        cursor.execute(query)
        movie_data = cursor.fetchone()

        if not movie_data:
            QMessageBox.information(self, "No Data Found", f"No movie found with Movie_ID {movie_id} and/or User_ID {user_id}.")
            connection.close()
            return 
        
        # Step 4: Populate the labels
        self.MovieTitle.setText(movie_data[1])  # Movie_Name
        self.Summary.setText(movie_data[2])  # Summary
        self.Duration.setText(movie_data[5])  # Duration
        self.Year.setText(str(movie_data[3]))  # Year
        # Step to load movie poster image based on movie name
        movie_name = movie_data[1]  # Get the movie name
        image_path = f'Assets/{movie_name}.jpg'  # Construct the image path
        print(image_path)
        print
    # Step 9: Load image into QLabel (Poster) and scale it to fit
        try:
            pixmap = QPixmap(image_path)
            if pixmap.isNull():
                raise ValueError("Image not found")
        
            # Use KeepAspectRatioByExpanding to ensure the image covers the QLabel without stretching
            scaled_pixmap = pixmap.scaled(self.Poster.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation)
        
            # Optionally, center the image if it doesn't fill the entire QLabel area
            self.Poster.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.Poster.setPixmap(scaled_pixmap)  # Set the image to the Poster QLabel
        except Exception as e:
            print(f"Error loading image: {e}")
            self.Poster.setText("Poster image not available")


        # Step 5: Set the checkboxes
        self.Watched.setChecked(movie_data[9] == 1)  # Status
        self.Watchlist.setChecked(movie_data[7] == 1)  # Watchlist
        self.Favourite.setChecked(movie_data[8] == 1)  # Favourite

        # Step 6: Execute genre query
        genre_query = f"SELECT Genre FROM Genre WHERE Movie_ID = {movie_id}"
        cursor.execute(genre_query)
        genres = [row[0] for row in cursor.fetchall()]
        self.Genres.setText("\n".join(genres))  # Populate Genres QTextBrowser

        # Step 7: Execute crew query
        crew_query = f"SELECT Cast FROM Crew WHERE Movie_ID = {movie_id}"
        cursor.execute(crew_query)
        cast_members = [row[0] for row in cursor.fetchall()]
        self.Cast.setText("\n".join(cast_members))  # Populate Cast QTextBrowser

        # Step 8: Close the database connection
        connection.close()
        
    def update_movie(self):
        # Get the current states of checkboxes (1 if checked, 0 if unchecked)
        watchlist = 1 if self.Watchlist.isChecked() else 0
        favourite = 1 if self.Favourite.isChecked() else 0
        status = 1 if self.Watched.isChecked() else 0

        # Connect to the database
        connection = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=DESKTOP-JBCSQ90\\MYSQLSERVER1;"
            "Database=CEflix;"
            "Trusted_Connection=yes;"
        )
        cursor = connection.cursor()

        # Use the dynamic Movie_ID and User_ID stored from populate_table
        update_query = """
        UPDATE User_Movie
        SET Watchlist = ?, Favourite = ?, Status = ?
        WHERE Movie_ID = ? AND User_ID = ?
        """
        cursor.execute(update_query, (watchlist, favourite, status, self.movie_id, self.user_id))
        connection.commit()

        # Close connection
        connection.close()

        # Optionally, show a confirmation message
        QtWidgets.QMessageBox.information(self, "Update", "Movie details updated successfully!")



app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
window = Movie_Details()  # Create an instance of our UI class
window.show()  # Show the UI
app.exec()  # Start the application