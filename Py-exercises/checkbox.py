import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.checkbox = QCheckBox("Are you gae?", self)
        self.initUI()
        self.setFixedSize(500, 500)

    def initUI(self):
        self.checkbox.setStyleSheet("font-size: 20px;")
        self.checkbox.setGeometry(170, 150, 200, 200)
        self.checkbox.stateChanged.connect(self.on_changed)

    def on_changed(self, state):
        if state == Qt.Checked:
            print("Bitch ass mf")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()