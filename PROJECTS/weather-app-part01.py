import requests
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit,  QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("C:\\Users\\unhol\\Downloads\\MISCS\\ICONS\\favicon-weather.jpg"))
        self.setWindowTitle("PyWeather Search")
        self.setGeometry(700, 300, 500, 500)

        self.header = QLabel("Hello! Ready to check?", self)
        self.city = QLineEdit(self)
        self.check = QPushButton("Check Weather", self)
        self.temp = QLabel(self)
        self.emoji = QLabel(self)
        self.status = QLabel(self)
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.header)
        vbox.addWidget(self.city)
        vbox.addWidget(self.check)
        vbox.addWidget(self.temp)
        vbox.addWidget(self.emoji)
        vbox.addWidget(self.status)

        self.setLayout(vbox)

        self.setStyleSheet("""
        QLabel, QLineEdit, QPushButton{
            font-size: 25px;
            padding: 15px;
        }
        """)

        self.header.setAlignment(Qt.AlignCenter)
        self.city.setAlignment(Qt.AlignCenter)
        self.temp.setAlignment(Qt.AlignCenter)
        self.emoji.setAlignment(Qt.AlignCenter)
        self.status.setAlignment(Qt.AlignCenter)

        self.check.clicked.connect(self.getWeather)

    def getWeather(self):
        city_name = self.city.text()
        API_key = "65f559fc73cc14b22bf620d8313aa696"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            pass

        else:
            match data['cod']:
                case '400':
                    self.emoji.setText(f"{data['message'].upper()} error!")
                case '401':
                    self.emoji.setText(f"{data['message'].upper()} error!")
                case '404':
                    self.emoji.setText(f"{data['message'].upper()} error!")
                case '5xx':
                    self.emoji.setText(f"{data['message'].upper()} error!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())
