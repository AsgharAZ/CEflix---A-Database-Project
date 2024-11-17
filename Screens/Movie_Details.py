from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox, QApplication, QGraphicsView, QGraphicsScene, QFileDialog, QWidget, QVBoxLayout, QPushButton # Import QMessageBox correctly
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QRectF  # Ensure this import is correct
import sys


class Movie_Details(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        
        super(Movie_Details, self).__init__()
        # Load the .ui file
        uic.loadUi('screens_final/Movie_Details.ui', self)
        
        # # Set up the QGraphicsScene
        # print('hello world')
        # self.scene = QGraphicsScene(self)
        
        # # Find the existing QGraphicsView by its object name
        # self.view = self.findChild(QGraphicsView, "Poster")
        # if self.view:
        #     self.view.setScene(self.scene)
        # else:
        #     print("QGraphicsView with object name 'Poster' not found")
            
        # self.image_path = "C:/Users/DELL/Pictures/work/University/Semester 7/CEflix - A Database Project/Screens/facade.jpg"
        
        # pixmap = QPixmap(self.image_path)
        
        # # Check if the QPixmap is valid
        # if not pixmap.isNull():
        #     # Create a QGraphicsPixmapItem to hold the image
        #     pixmap_item = self.scene.addPixmap(pixmap)
        #     rect = pixmap_item.pixmap().rect()
        #     rect_f = QRectF(rect)  # Convert QRect to QRectF
        #     # Adjust the scene size to the image size
        #     self.scene.setSceneRect(rect_f)
        # else:
        #     print("Failed to load image. Check the path.")
        
    # def fit_image_to_view(self, pixmap_item):
    #     # Simply set the scene rect to the size of the pixmap
    #     self.scene.setSceneRect(pixmap_item.pixmap().rect())
    #     # Fit the view to the scene
    #     self.view.fitInView(self.scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
    #     self.view.centerOn(pixmap_item)
        
        
        
        # file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.xpm *.jpg)")
        # if file_name:
        #     # Load the image into a QPixmap
        #     pixmap = QPixmap(file_name)
        #     # Create a QGraphicsPixmapItem to hold the image
        #     pixmap_item = self.scene.addPixmap(pixmap)
        #     # Optionally, adjust the scene size to the image size
        #     self.scene.setSceneRect(pixmap_item.pixmap().rect())
        
        
app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
window = Movie_Details()  # Create an instance of our UI class
window.show()  # Show the UI
app.exec()  # Start the application