from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget
from keyboard import add_hotkey
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from sys import argv, exit
import pyautogui as pyag
from time import sleep


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stumble Farm v1.2")
        self.setWindowIcon(QIcon("images\\icon.jpeg"))
        self.setFixedSize(300, 300)
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        self.label = QLabel("Enable - Press 1\n\nDisable - Press 2", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_status = QLabel("Disabled", self)
        self.label_status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        layout.addWidget(self.label_status)

        buttons_info = [("1 Event", self.first_event_farm),
                        ("2 Event", self.second_event_farm),
                        ("3 Event", self.third_event_farm),
                        ("Default Game", self.default_game_farm),
                        ("Exit", exit)]

        for button_text, function in buttons_info:
            button = QPushButton(button_text, self)
            button.clicked.connect(function)
            layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)

    def first_event_farm(self):
        global first_event, second_event, third_event, default_game
        self.label_status.setText("AutoFarm: 1 Event")
        first_event = True
        second_event, third_event, default_game = False * 3

    def second_event_farm(self):
        global first_event, second_event, third_event, default_game
        self.label_status.setText("AutoFarm: 2 Event")
        second_event = True
        first_event, third_event, default_game = False * 3

    def third_event_farm(self):
        global first_event, second_event, third_event, default_game
        self.label_status.setText("AutoFarm: 3 Event")
        third_event = True
        first_event, second_event, default_game = False * 3

    def default_game_farm(self):
        global first_event, second_event, third_event, default_game
        self.label_status.setText("AutoFarm: Default Game")
        default_game = True
        first_event, second_event, third_event = False * 3


app = QApplication(argv)
window = MyWindow()
leave_x = 250
leave_y = 1000
take_x = 1777
take_y = 1000
default_game = False
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
    return is_clicking


add_hotkey("1", clicker)
add_hotkey("2", off_clicker)


if __name__ == "__main__":
    window.show()
    exit(app.exec())
