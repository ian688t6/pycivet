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
        self._ui_init()

    def _ui_bin_tabview_init(self):
        self._bin_colmax = 17
        self.bin_data_model = QStandardItemModel(5, self._bin_colmax, self)
        self.bin_sel_model = QItemSelectionModel(self.bin_data_model)
        self.ui.binTabView.setModel(self.bin_data_model)
        self.ui.binTabView.setSelectionModel(self.bin_sel_model)
        self.ui.binTabView.setEnabled(False)

    def _ui_reg_tabview_init(self):
        self._regmap_colmax = 3
        self.regmap_data_model = QStandardItemModel(5, self._regmap_colmax, self)
        self.regmap_sel_model = QItemSelectionModel(self.regmap_data_model)
        self.regmap_sel_model.currentChanged.connect(self.do_regmapChanged)
        self.ui.regmapTabView.setModel(self.regmap_data_model)
        self.ui.regmapTabView.setSelectionModel(self.regmap_sel_model)
        self.ui.regmapTabView.setEnabled(False)

    def _ui_init(self):
        self.ui.actionDisconnect.setDisabled(True)
        self.ui.actionDownload.setDisabled(True)
        self.ui.actionImport.setDisabled(True)
        self.ui.actionOpen.setDisabled(True)
        self._ui_bin_tabview_init()
        self._ui_reg_tabview_init()

    def _ui_init_bincontent(self, content):
        total_count = len(content)
        row_count = (total_count // 16) + 1
        self.bin_data_model.setRowCount(row_count)
        j = 0
        for i in range(row_count):
            item = QStandardItem('0x{:08X}'.format(i * 16))
            self.bin_data_model.setItem(i, 0, item)
            if total_count >= 16:
                for j in range(16):
                    item = QStandardItem('0x{:02X}'.format(content[i * 16 + j]))
                    item.setFlags(item.flags() & (~Qt.ItemIsEditable))
                    self.bin_data_model.setItem(i, 1+j, item)
                total_count -= 16
            else:
                for j in range(total_count):
                    item = QStandardItem('0x{:02X}'.format(content[i * 16 + j]))
                    item.setFlags(item.flags() & (~Qt.ItemIsEditable))
                    self.bin_data_model.setItem(i, 1+j, item)
                total_count = 0
        self.ui.binTabView.setEnabled(True)

    def _ui_init_regmap(self, regs):
        self.regmap_data_model.setRowCount(len(regs))
        self.regmap_data_model.setHorizontalHeaderLabels(regs[0].keys())
        j = 0
        for i in range(len(regs)):
            for v in regs[i].values():
                item = QStandardItem(v)
                if j == 0 or j == 1:
                    item.setFlags(item.flags() & (~Qt.ItemIsEditable))
                self.regmap_data_model.setItem(i, j, item)
                j += 1
            j = 0
        self.ui.regmapTabView.setEnabled(True)


    def do_regmapChanged(self, current, previous):
        pass

    @pyqtSlot()
    def on_actionOpen_triggered(self):
        curpath = os.getcwd()
        filename,flt = QFileDialog.getOpenFileName(self,"Open the binary file",curpath,
               "binary file(*.bin);;All(*.*)")
        if filename == '':
            return
        size = os.path.getsize(filename)
        with open(filename, 'rb') as binfile:
            content = binfile.read(size)
            self.bincontent = list(bytes(content))
            self._ui_init_bincontent(self.bincontent)
        
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
        self._ui_init_regmap(self.regmap)
