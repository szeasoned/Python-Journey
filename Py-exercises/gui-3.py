import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Remedy")
        self.setWindowIcon(QIcon("C:/Users/unhol/OneDrive/IMAGES/profile_pic.jpg"))

        self.setFixedSize(500, 500)
        self.setStyleSheet("background-color: #1E1E1E;")

        logo_1 = QLabel(self)
        logo_1.setGeometry(200, 0, 100, 100)
        school_logo = QPixmap("C:/Users/unhol/OneDrive/IMAGES/KE_Logo.jpg")
        logo_1.setPixmap(school_logo)
        logo_1.setScaledContents(True)
        logo_1.setAlignment(Qt.AlignTop | Qt.AlignRight)

        school_name = QLabel("Biringan University of Ilocos", self)
        school_name.setGeometry(50, 100, 400, 40)
        school_name.setAlignment(Qt.AlignCenter)
        school_name.setFont(QFont("Arial", 14, QFont.Bold))
        school_name.setStyleSheet("color: #F5F5F5")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()