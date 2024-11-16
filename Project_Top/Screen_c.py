from PyQt6 import QtWidgets, uic
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        try:
            uic.loadUi('Proposal_screen_c.ui', self)
        except Exception as e:
            print(f"Error loading UI file: {e}")

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
