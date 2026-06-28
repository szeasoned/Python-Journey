import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.radio1 = QRadioButton("Pizza", self)
        self.radio2 = QRadioButton("Hotdog", self)
        self.radio3 = QRadioButton("Pretzel", self)
        self.radio4 = QRadioButton("Cola", self)
        self.radio5 = QRadioButton("Water", self)
        self.initUI()
        self.setFixedSize(500, 500)

    def initUI(self):
        self.radio1.setGeometry(0, 0, 150, 50)
        self.radio2.setGeometry(0, 50, 150, 50)
        self.radio3.setGeometry(0, 100, 150, 50)
        self.radio4.setGeometry(0, 150, 150, 50)
        self.radio5.setGeometry(0, 200, 150, 50)

        self.setStyleSheet("QRadioButton{"
                           "font-size: 20px;"
                           "}")

        self.radio_group1 = QButtonGroup(self)
        self.radio_group2 = QButtonGroup(self)

        self.radio_group1.addButton(self.radio1)
        self.radio_group1.addButton(self.radio2)
        self.radio_group1.addButton(self.radio3)
        self.radio_group2.addButton(self.radio4)
        self.radio_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.on_changed)
        self.radio2.toggled.connect(self.on_changed)
        self.radio3.toggled.connect(self.on_changed)
        self.radio4.toggled.connect(self.on_changed)
        self.radio5.toggled.connect(self.on_changed)

    def on_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected.")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
