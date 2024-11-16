from PyQt6 import QtWidgets, uic
import sys
import pyodbc

# Main Window Class
class ProposalScreenH(QtWidgets.QMainWindow):
    def __init__(self):
        super(ProposalScreenH, self).__init__()
        # Load the UI file
        uic.loadUi('Proposal_screen_h.ui', self)
        
        # Connect the Submit button to the event handler
        self.submitButton.clicked.connect(self.add_movie)

    def add_movie(self):
        """
        Collects movie details from the UI and inserts them into the database.
        """
        # Collect details from input fields
        movie_name = self.lineEdit.text()
        # TODO: Add other fields as required

        # Database connection string
        connection = pyodbc.connect(
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=DESKTOP-VO1PBUT\\SQLSERVER;"
            "Database=Project;"
            "Trusted_Connection=yes;"
        )
        cursor = connection.cursor()

        # Insert data into the Movies table
        try:
            cursor.execute("""
                INSERT INTO Movies (Name)
                VALUES (?)
            """, (movie_name,))
            connection.commit()
            QtWidgets.QMessageBox.information(self, "Success", "Movie added successfully!")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to add movie: {e}")
        finally:
            connection.close()

# Main Application Entry Point
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ProposalScreenH()
    window.show()
    sys.exit(app.exec())
