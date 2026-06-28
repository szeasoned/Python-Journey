import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import QTimer, Qt


class HIITWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.workout1 = QLineEdit(self)
        self.workout2 = QLineEdit(self)
        self.workout3 = QLineEdit(self)

        self.timer_label = QLabel("03:00", self)
        self.button = QPushButton("Start!", self)
        self.label = QLabel("READY, SET, ...", self)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        self.time_left = 180  # Initialize timer

        self.initUI()
        self.setGeometry(550, 300, 800, 500)

    def initUI(self):
        self.setWindowTitle("HIIT TRACKER")

        self.workout1.setGeometry(50, 20, 250, 50)
        self.workout2.setGeometry(50, 100, 250, 50)
        self.workout3.setGeometry(50, 180, 250, 50)

        self.workout1.setPlaceholderText("Enter workout #1")
        self.workout2.setPlaceholderText("Enter workout #2")
        self.workout3.setPlaceholderText("Enter workout #3")

        self.setStyleSheet("""
            QLineEdit {
                font-size: 20px;
            }
        """)

        self.timer_label.setGeometry(50, 270, 250, 50)
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setStyleSheet("""
            font-size: 25px;
            background-color: red;
            color: white;
            font-family: Roboto;
            border: 1px solid blue;
        """)

        self.button.setGeometry(50, 350, 250, 50)
        self.button.setStyleSheet("""
            font-size: 25px;
            background-color: #2C2C2C;
            color: white;
        """)

        self.label.setGeometry(380, 65, 350, 350)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("""
            font-size: 25px;
            background-color: #F4B400;
            color: #1F1F1F;
            font-family: Roboto;
        """)

        self.button.clicked.connect(self.start_timer)

    def start_timer(self):
        if self.timer.isActive():
            return

        self.time_left = 180
        self.timer_label.setText("03:00")
        self.label.setText(f"It's time for {self.workout1.text()}!")

        self.button.setEnabled(False)
        self.timer.start(1000)

    def update_timer(self):
        self.time_left -= 1

        minutes = self.time_left // 60
        seconds = self.time_left % 60

        self.timer_label.setText(f"{minutes:02}:{seconds:02}")

        if self.time_left == 130:
            self.label.setText("REST TIME!")

        elif self.time_left == 120:
            self.label.setText(f"It's time for {self.workout2.text()}!")

        elif self.time_left == 70:
            self.label.setText("REST TIME!")

        elif self.time_left == 60:
            self.label.setText(f"It's time for {self.workout3.text()}!")

        elif self.time_left == 10:
            self.label.setText("REST TIME!")

        elif self.time_left <= 0:
            self.timer.stop()
            self.timer_label.setText("00:00")
            self.label.setText("REST FOR 2 MINS!")
            self.button.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = HIITWidget()
    widget.show()
    sys.exit(app.exec_())