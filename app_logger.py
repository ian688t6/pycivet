from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog)
from PyQt5.QtCore import (QDir, QTimer)
from ui.ui_mainwindow import Ui_MainWindow
from ui.res_rc import *

class AppLogger(QTimer):
    def __init__(self, ui, rx, parent = None):
        super().__init__(parent)
        self.ui = ui
        self.rx = rx
        self.stop()
        self.setInterval(0)
        self.timeout.connect(self.do_update_log)

    def do_update_log(self):
        logdata = self.rx.get_logline()
        if logdata != None:
            self.ui.logPlainText.appendPlainText(logdata)
           

