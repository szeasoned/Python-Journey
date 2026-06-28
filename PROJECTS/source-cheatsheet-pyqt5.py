import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.initUI()

    def initUI(self):
        pass

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

"""
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QTextEdit,
    QListWidget,
    QTableWidget,
    QMainWindow,
)

from PyQt5.QtGui import (
    QFont,
    QIcon,
    QColor,
    QPixmap,
)

from PyQt5.QtCore import (
    Qt,
    QSize,
    QTimer,
    pyqtSignal,
)
"""