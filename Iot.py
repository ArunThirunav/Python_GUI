from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
import sys
import urllib.request
import time


def func():
    print("Hello")
    dlg.lineEdit.setText("Hello")

def getdata():
    while True:
        request_url = urllib.request.urlopen('https://api.thingspeak.com/channels/2071274/feeds.json?api_key=UJG4FP1L1XVSO0GO&results=2')
        print(request_url.read())
        time.sleep(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = uic.loadUi('frontEnd.ui')
    dlg.pushButton.clicked.connect(func)
    dlg.show()
app.exec()
getdata()