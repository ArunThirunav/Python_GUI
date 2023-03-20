from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
import sys

def func():
    print("Hello")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = uic.loadUi('frontEnd.ui')
    dlg.pushButton.clicked.connect(func)
    dlg.show()
app.exec()