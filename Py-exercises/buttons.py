import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 500)
        self.button = QPushButton("Hello", self)
        self.label = QLabel("Nice to meet you!", self)
        self.initUI()

    def initUI(self):
        self.button.setStyleSheet("font-size: 30px;")
        self.button.setGeometry(200, 0, 100, 100)
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(175, 80, 200, 100)
        self.label.setStyleSheet("font-size: 20px;")

    def on_click(self):
        self.button.setText("Bye")
        self.button.setStyleSheet("color: red;")
        self.button.setStyleSheet("font-size: 30px;")

        self.label.setText("Goodbye, friend!")
        self.label.setStyleSheet("font-size: 20px;")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()