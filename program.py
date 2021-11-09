#hello!

import subprocess
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import os

form_class = uic.loadUiType("youtube.ui")[0] #https://www.youtube.com/watch?v=uQ1N0u7Nr1g

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.down_start)

    def down_start(self):
        url = self.lineEdit.text()
        path = self.lineEdit_2.text()

        self.label_3.setText("Downloading..")

        if not self.checkBox.isChecked() ^ self.checkBox_2.isChecked():
            subprocess.run(['youtube-dl', '-f', 'bestvideo+bestaudio', '-o', path+"%(title)s.%(ext)s", url], shell=True)

        elif self.checkBox.isChecked():
            subprocess.run(['youtube-dl', '-f', 'bestaudio', '-o', path+"%(title)s.%(ext)s", '-x', '--audio-format', 'mp3',
                            url], shell=True)

        else:
            subprocess.run(['youtube-dl', '-f', 'bestvideo', '-o', path+"%(title)s.%(ext)s",
                            url], shell=True)

        self.label_3.setText("Download complete")
if __name__=='__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
