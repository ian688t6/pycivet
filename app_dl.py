import sys,os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QProgressBar,QAbstractItemView, QFileDialog)
from PyQt5.QtCore import (Qt, pyqtSlot, QItemSelectionModel, QDir, QModelIndex, QTimer)
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from ui.ui_mainwindow import Ui_MainWindow
from ui.res_rc import *

class AppDownloader(QTimer):
    def __init__(self, ui, rx, progbar, parent = None):
        super().__init__(parent)
        self.ui = ui
        self.rx = rx
        self._binfile = ''
        self._ui_bin_tabview_init()
        self._progbar = progbar
        self.stop()
        self.setInterval(0)
        self.timeout.connect(self.do_download)

    def _ui_bin_tabview_init(self):
        self._bin_colmax = 17
        self.bin_data_model = QStandardItemModel(5, self._bin_colmax, self)
        self.bin_sel_model = QItemSelectionModel(self.bin_data_model)
        self.ui.binTabView.setModel(self.bin_data_model)
        self.ui.binTabView.setSelectionModel(self.bin_sel_model)
        self.ui.binTabView.setEnabled(False)

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

    def open(self, filename, verify=1):
        self._binfile = filename
        self._verify = verify
        self._binsize = os.path.getsize(filename)
        self._pagesize = 1024
        self._address = 0
        with open(filename, 'rb') as binfile:
            content = binfile.read(self._binsize)
            self._bincontent = list(bytes(content))
            self._ui_init_bincontent(self._bincontent)
            self._progbar.setRange(0, self._binsize)
            self._progbar.setValue(0)

    def start(self):
        self._binsize = os.path.getsize(self._binfile)
        self._pagesize = 1024
        self._address = 0
        super().start()

    def do_download(self):
        if self._binsize > 0:
            if self._binsize > self._pagesize:
                self.rx.writepage(self._address, self._bincontent[self._address:(self._address + self._pagesize)], self._pagesize)
                if self._verify:
                    verifydata = self.rx.readpage(self._address, self._pagesize)
                    if verifydata != self._bincontent[self._address: (self._address + self._pagesize)]:
                        self.rx.writesram(0x50100031, 0x01)
                        self.stop()
                        return
                self._binsize -= self._pagesize
                self._address += self._pagesize
            else:
                self.rx.writepage(self._address, self._bincontent[self._address:], self._binsize)
                if self._verify:
                    verifydata = self.rx.readpage(self._address, self._binsize)
                    if verifydata != self._bincontent[self._address:]:
                        self.rx.writesram(0x50100031, 0x01)
                        self.stop()
                        return
                self._address += self._binsize
                self._binsize = 0
                self.rx.writesram(0x50100031, 0x01)
                self.stop()
            self._progbar.setValue(self._address)
