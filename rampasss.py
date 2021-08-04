import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


def mix(string):
    alg_list = list(string)
    random.shuffle(alg_list)
    return ''.join(alg_list)


fnum1 = random.randint(0, 9)
fnum2 = random.randint(0, 9)
uLetter1 = chr(random.randint(65, 90))
uLetter2 = chr(random.randint(65, 90))
lLetter1 = chr(random.randint(97, 122))
lLetter2 = chr(random.randint(97, 122))
spcchar1 = chr(random.randint(33, 64))
spcchar2 = chr(random.randint(33, 64))

final_password = uLetter1 + uLetter2 + str(fnum1) + str(fnum2) + lLetter1 + lLetter2 + spcchar1 + spcchar2
final_password = mix(final_password)


def window():
    qt = QApplication(sys.argv)
    widget = QWidget()
    go_button = QPushButton(widget)
    go_button.setText("Go")
    go_button.move(215, 190)
    go_button.setStyleSheet("background-color: #4DA9F9;")
    go_button.clicked.connect(go_button_clicked)

    qt.setStyle("Fusion")
    widget.setStyleSheet("background-color: #161B22;")
    widget.setGeometry(100, 100, 520, 400)
    widget.setWindowTitle("RamPass")
    widget.show()
    sys.exit(qt.exec_())


def go_button_clicked():
    print(final_password)


if __name__ == '__main__':
    window()
