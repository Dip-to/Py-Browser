import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainPage(QMainWindow):
    def __init__(brow):
        super(MainPage, brow).__init__()
        brow.browser = QWebEngineView()
        brow.browser.setUrl(QUrl('http://google.com'))
        # brow.centralWidget(brow.browser)
        brow.setCentralWidget(brow.browser)
        brow.showMaximized()

        # taskbar
        task_bar = QToolBar()
        brow.addToolBar(task_bar)

        # img load
        bck_img = QIcon("icons/arrow-curve-180-left.png")
        next_img = QIcon("icons/arrow-curve.png")
        reload_img = QIcon("icons/arrow-circle-225-left.png")

        # back next reload
        bck = QAction(bck_img, 'Back', brow)
        bck.triggered.connect(brow.browser.back)
        task_bar.addAction(bck)

        forwrd = QAction(next_img, 'Forward', brow)
        forwrd.triggered.connect(brow.browser.forward)
        task_bar.addAction(forwrd)

        rel = QAction(reload_img, 'reload', brow)
        rel.triggered.connect(brow.browser.reload)
        task_bar.addAction(rel)

        # address bar
        brow.add_bar = QLineEdit()
        # brow.add_bar.setText("http://")
        brow.add_bar.returnPressed.connect(brow.to_Url)
        task_bar.addWidget(brow.add_bar)

    # address formatting
    def to_Url(self):
        url = self.add_bar.text()
        if "http://" not in url:
            url = "http://" + url
        self.browser.setUrl(QUrl(url))


# app run
rend = QApplication(sys.argv)
QApplication.setApplicationName('Py Browser')
page = MainPage()
rend.exec_()
