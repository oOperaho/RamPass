import sys
import random
import clipboard as pc
import webbrowser

from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


def mix(string):
    password_list = list(string)
    random.shuffle(password_list)
    return "".join(password_list)


class MainWidget(QMainWindow):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.url = "https://github.com/oOperaho/RamPass"
        self.final_password = ""
        self.label_pass = QtWidgets.QLabel(self)
        self.genpass = QtWidgets.QLabel(self)
        self.go_button = QPushButton(self)
        self.repo_button = QPushButton(self)
        self.copy_text = QPushButton(self)
        self.setStyleSheet("background-color: #161B22;")
        self.setGeometry(100, 100, 520, 400)
        self.setWindowTitle("RamPass")
        self.mainui()

    def mainui(self):
        self.genpass.setText("• Generate Password •")
        self.genpass.setGeometry(173, 40, 200, 100)
        self.genpass.setFont(QFont("Impact", 15))
        self.genpass.setStyleSheet("""background-color: #161B22; color: #65F791;""")

        self.label_pass.setText(" " * 16 + "-")
        self.label_pass.setGeometry(212, 140, 100, 40)
        self.label_pass.setFont(QFont("Times New Roman", 10))
        self.label_pass.setStyleSheet("""background-color: #161B22; color: #ffffff;""")

        self.go_button.setText("GO")
        self.go_button.setGeometry(227, 180, 70, 25)
        self.go_button.setFont(QFont("Times New Roman", 8))
        self.go_button.setStyleSheet("background-color: #4DA9F9; color: #1b1c1e")
        self.go_button.clicked.connect(self.go_button_clicked)

        self.repo_button.setText("••")
        self.repo_button.setGeometry(10, 10, 12, 12)
        self.repo_button.setStyleSheet("background-color: #161B22; color: #65F791")
        self.repo_button.clicked.connect(self.open_repo)

        self.copy_text.setText("Copy")
        self.copy_text.setGeometry(250, 210, 27, 17)
        self.copy_text.setStyleSheet("background-color: #161B22; color: white")
        self.copy_text.clicked.connect(self.copy_to_clipboard)

    def go_button_clicked(self):
        fnum1 = random.randint(0, 9)
        fnum2 = random.randint(0, 9)
        uletter1 = chr(random.randint(65, 90))
        uletter2 = chr(random.randint(65, 90))
        lletter1 = chr(random.randint(97, 122))
        lletter2 = chr(random.randint(97, 122))
        spcchar1 = chr(random.randint(33, 64))
        spcchar2 = chr(random.randint(33, 64))

        self.final_password = uletter1 + uletter2 + str(fnum1) + str(fnum2) + lletter1 + lletter2 + spcchar1 + spcchar2
        self.final_password = mix(self.final_password)

        self.label_pass.setText(" " * 8 + self.final_password)
        print(self.final_password)

    def open_repo(self):
        webbrowser.open_new(self.url)

    def copy_to_clipboard(self):
        pc.copy(self.final_password)


def window():
    qt = QApplication(sys.argv)
    widget = MainWidget()
    qt.setStyle("Oxygen")
    widget.show()
    sys.exit(qt.exec_())


window()
