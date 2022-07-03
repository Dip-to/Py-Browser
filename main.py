import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainPage(QMainWindow):
    def __init__(brow):
        super(MainPage, brow).__init__()
        brow.browser=QWebEngineView()
        brow.browser.setUrl(QUrl('http://google.com'))
       # brow.centralWidget(brow.browser)
        brow.setCentralWidget(brow.browser)
        brow.showMaximized()


rend = QApplication(sys.argv)
QApplication.setApplicationName('Py Browser')
page=MainPage()
rend.exec_()
