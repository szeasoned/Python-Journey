import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QLabel, QGridLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 500)
        self.setStyleSheet("background-color: #1E1E1E;")
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("7", self)
        label2 = QLabel("8", self)
        label3 = QLabel("9", self)
        label4 = QLabel("+", self)

        label5 = QLabel("4", self)
        label6 = QLabel("5", self)
        label7 = QLabel("6", self)
        label8 = QLabel("-", self)

        label9 = QLabel("1", self)
        labelA = QLabel("2", self)
        labelB = QLabel("3", self)
        labelC = QLabel("*", self)

        labelD = QLabel(".", self)
        labelE = QLabel("0", self)
        labelF = QLabel("/", self)
        labelG = QLabel("=", self)

        labels = [
            label1, label2, label3, label4,
            label5, label6, label7, label8,
            label9, labelA, labelB, labelC,
            labelD, labelE, labelF, labelG
        ]

        for label in labels:
            label.setAlignment(Qt.AlignCenter)
            label.setFont(QFont("Arial", 15))
            label.setStyleSheet("background-color: #2D2D2D;"
                                "color: #E8EAED;")

        grid = QGridLayout()

        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 0, 2)
        grid.addWidget(label4, 0, 3)
        grid.addWidget(label5, 1, 0)
        grid.addWidget(label6, 1, 1)
        grid.addWidget(label7, 1, 2)
        grid.addWidget(label8, 1, 3)
        grid.addWidget(label9, 2, 0)
        grid.addWidget(labelA, 2, 1)
        grid.addWidget(labelB, 2, 2)
        grid.addWidget(labelC, 2, 3)
        grid.addWidget(labelD, 3, 0)
        grid.addWidget(labelE, 3, 1)
        grid.addWidget(labelF, 3, 2)
        grid.addWidget(labelG, 3, 3)

        central_widget.setLayout(grid)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()