import sys,os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QAbstractItemView, QFileDialog)
from PyQt5.QtCore import (Qt, pyqtSlot, QItemSelectionModel, QDir, QModelIndex)
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from ui.ui_mainwindow import Ui_MainWindow
from ui.res_rc import *
from cfs.regmap import RegMap

class AppMainWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__ui_init()

    def __ui_init(self):
        self.ui.actionDisconnect.setDisabled(True)
        self.ui.actionDownload.setDisabled(True)
        self.ui.actionImport.setDisabled(True)
        self.ui.actionOpen.setDisabled(True)

    @pyqtSlot()
    def on_actionOpen_triggered(self):
        pass

    @pyqtSlot()
    def on_actionImport_triggered(self):
        curpath = os.getcwd()
        filename,flt = QFileDialog.getOpenFileName(self,"Open the excel file",curpath,
               "regmap file(*.xlsx);;All(*.*)")
        if filename == '':
            return
        self.regmaps = RegMap()
        self.regmaps.load(filename)
        regblocks = self.regmaps.get_regblocks()
        self.ui.regmapComBox.addItems(regblocks)

    @pyqtSlot()
    def on_actionConnect_triggered(self):
        self.ui.actionDisconnect.setEnabled(True)
        self.ui.actionDownload.setEnabled(True)
        self.ui.actionImport.setEnabled(True)
        self.ui.actionOpen.setEnabled(True)
        self.ui.actionConnect.setDisabled(True)

    @pyqtSlot()
    def on_actionDisconnect_triggered(self):
        self.ui.actionDisconnect.setDisabled(True)
        self.ui.actionDownload.setDisabled(True)
        self.ui.actionImport.setDisabled(True)
        self.ui.actionOpen.setDisabled(True)
        self.ui.actionConnect.setEnabled(True)

    @pyqtSlot(str)
    def on_regmapComBox_currentIndexChanged(self, block):
        self.regmap = self.regmaps.get_regmap(block)
        for regdata in self.regmap:
            print(regdata)