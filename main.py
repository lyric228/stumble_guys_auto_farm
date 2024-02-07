from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget
from keyboard import add_hotkey
from PyQt6.QtGui import QIcon
from sys import argv, exit
import pyautogui as pyag
from time import sleep


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stumble Farm PRO v1.0")
        self.setWindowIcon(QIcon("images\\icon.jpeg"))
        self.setFixedSize(300, 300)
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        self.label = QLabel("                            Включить фарм - 1\n \n                            Выключить фарм - 2", self)
        layout.addWidget(self.label)

        buttons_info = [("1 Ивент", self.first_event_farm),
                        ("2 Ивент", self.second_event_farm),
                        ("3 Ивент", self.third_event_farm),
                        ("Обычная игра", self.default_game_farm),
                        ("Выйти", exit)]

        for button_text, function in buttons_info:
            button = QPushButton(button_text, self)
            button.clicked.connect(function)
            layout.addWidget(button)

    def first_event_farm(self):
        global first_event, second_event, third_event, default_game
        self.label.setText("Включить фарм - 1   Выключить фарм - 2\nВключен режим: 1 Ивент")
        first_event = True
        second_event = False
        third_event = False
        default_game = False

    def second_event_farm(self):
        global first_event, second_event, third_event, default_game
        self.label.setText("Включить фарм - 1   Выключить фарм - 2\nВключен режим: 2 Ивент")
        second_event = True
        first_event = False
        third_event = False
        default_game = False

    def third_event_farm(self):
        global first_event, second_event, third_event, default_game
        self.label.setText("Включить фарм - 1   Выключить фарм - 2\nВключен режим: 3 Ивент")
        third_event = True
        first_event = False
        second_event = False
        default_game = False

    def default_game_farm(self):
        global first_event, second_event, third_event, default_game
        self.label.setText("Включить фарм - 1   Выключить фарм - 2\nВключен режим: Обычная игра")
        default_game = True
        first_event = False
        second_event = False
        third_event = False


app = QApplication(argv)
window = MyWindow()
leave_x = 250
leave_y = 1000
take_x = 1777
take_y = 1000
default_game = True
first_event = False
second_event = False
third_event = False
pyag.FAILSAFE = False


def clicker():
    global is_clicking
    is_clicking = True
    while is_clicking:
        sleep(5)
        if not default_game:
            pyag.click(1500, 800)
            sleep(1)
            if first_event:
                pyag.click(470, 985)

            if second_event:
                pyag.click(1250, 985)

            if third_event:
                pyag.click(1800, 985)
        else:
            pyag.click(1600, 970)
        sleep(5)
        while is_clicking:
            pixel_check = pyag.pixel(leave_x, leave_y)
            if pixel_check[0] > 230 and 90 > pixel_check[1] > 65 and 63 > pixel_check[2] > 49:
                pyag.press("esc")
                break

            if pixel_check[0] > 65 and pixel_check[1] > 180 and 30 > pixel_check[2] > 15:
                pyag.click(take_x, take_y)
                break
            else:
                sleep(0.1)


def off_clicker():
    global is_clicking
    is_clicking = False


add_hotkey("1", clicker)
add_hotkey("2", off_clicker)


if __name__ == "__main__":
    window.show()
    exit(app.exec())
