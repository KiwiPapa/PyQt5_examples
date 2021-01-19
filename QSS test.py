import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        button = QPushButton("Button")
        self.layout = QHBoxLayout()
        self.layout.addWidget(button)
        self.setLayout(self.layout)
        qss = "QPushButton{color:red;}"
        self.setStyleSheet(qss)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())