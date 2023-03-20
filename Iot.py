from PyQt5.QtWidgets import QDialog, QPushButton, QApplication
from PyQt5 import uic
import sys


app = QApplication(sys.argv)
win = uic.loadUi('frontEnd.ui')
win.show()
app.exec()