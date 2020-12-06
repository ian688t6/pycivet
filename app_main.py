import sys

from PyQt5.QtWidgets import  QApplication
from app_mainwindow import AppMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    appMain = AppMainWindow()
    appMain.show()
    sys.exit(app.exec_())