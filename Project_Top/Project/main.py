import sys
from PyQt6.QtWidgets import QApplication
from ui_login import UI  # Import login UI class

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec())