import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("mainWindow")
        qss = "QWidget#mainWindow{background-color:black;}"
        # qss = "QWidget#mainWindow{border-image:url(background.png);}"
        self.setStyleSheet(qss)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())