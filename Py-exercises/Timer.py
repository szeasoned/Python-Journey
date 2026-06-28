import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class TimeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("12:12:12", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        self.setLayout(vbox)

        self.label.setAlignment(Qt.AlignCenter)

        self.update_time()

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def update_time(self):
        current_time = QTime().currentTime().toString("hh:mm:ss AP")
        self.label.setText(current_time)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = TimeWidget()
    widget.show()
    sys.exit(app.exec_())