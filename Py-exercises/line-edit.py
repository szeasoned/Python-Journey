import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("submit", self)
        self.setGeometry(700, 300, 500, 500)
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10, 10, 200, 50)
        self.line_edit.setStyleSheet("font-size: 25px;")
        self.line_edit.setPlaceholderText("Enter your name")

        self.button.setGeometry(210, 10, 200, 50)
        self.button.setStyleSheet("font-size: 25px;")

        self.button.clicked.connect(self.on_submit)

    def on_submit(self):
        text = self.line_edit.text()
        print(f"Hello, {text}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()