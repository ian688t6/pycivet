import sys,os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QProgressBar,QLabel, QAbstractItemView, QFileDialog, QButtonGroup)
from PyQt5.QtCore import (Qt, pyqtSlot, QItemSelectionModel, QDir, QModelIndex, QTimer)
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from ui.ui_mainwindow import Ui_MainWindow
from ui.res_rc import *
from cfs.regmap import RegMap
from cfs.prx import Prx
from app_logger import AppLogger
from app_dl import AppDownloader

class AppMainWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.rx = Prx()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._ui_init()
        self._db_init()
        self.applogger = AppLogger(self.ui, self.rx)
        self.appdl = AppDownloader(self.ui, self.rx, self._progress_bar)

    def _db_init(self):
        self._regblocks=[]

    def _ui_init(self):
        self.ui.actionDisconnect.setDisabled(True)
        self.ui.actionDownload.setDisabled(True)
        self.ui.actionImport.setDisabled(True)
        self.ui.actionOpen.setDisabled(True)
        self.ui.reggetButton.setDisabled(True)
        self.ui.regsetButton.setDisabled(True)
        self.ui.logStartButton.setDisabled(True)
        self.ui.logfileButton.setDisabled(True)
        self._btngroup = QButtonGroup()
        self._btngroup.addButton(self.ui.hexRadioBtn)
        self._btngroup.setId(self.ui.hexRadioBtn, 0)
        self._btngroup.addButton(self.ui.decRadioBtn)
        self._btngroup.setId(self.ui.decRadioBtn, 1)
        self._btngroup.addButton(self.ui.binRadioBtn)
        self._btngroup.setId(self.ui.binRadioBtn, 2)
        self._btngroup.buttonToggled[int, bool].connect(self.do_toggle_datafmt)
        self._ui_statusbar_init()
        self._ui_reg_tabview_init()
        self._ui_init_regctl()

    def _ui_statusbar_init(self):
        self._progress_bar = QProgressBar(self)      # progressBar1
        self._progress_bar.setMaximumWidth(200)
        self._progress_bar.setValue(0)
        self.ui.statusbar.addWidget(self._progress_bar)

    def _ui_reg_tabview_init(self):
        self._regmap_colmax = 3
        self.regmap_data_model = QStandardItemModel(5, self._regmap_colmax, self)
        self.regmap_sel_model = QItemSelectionModel(self.regmap_data_model)
        self.regmap_sel_model.currentChanged.connect(self.do_regmapChanged)
        self.ui.regmapTabView.setModel(self.regmap_data_model)
        self.ui.regmapTabView.setSelectionModel(self.regmap_sel_model)
        self.ui.regmapTabView.setEnabled(False)

    def _ui_init_regctl(self):
        self.ui.hexRadioBtn.setChecked(True)

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
        if current == None:
            return
        self._regindex = self.regmap_data_model.index(current.row(), 0, QModelIndex())
        regitem = self.regmap_data_model.itemFromIndex(self._regindex)
        self.ui.regaddrLineEdit.setText(regitem.text())

    def closeEvent(self, event):
        self.applogger.stop()
        self.appdl.stop()
        self.rx.disconnect()

    @pyqtSlot()
    def on_actionOpen_triggered(self):
        self.ui.actionDownload.setEnabled(True)
        curpath = os.getcwd()
        filename,flt = QFileDialog.getOpenFileName(self,"Open the binary file",curpath,
               "binary file(*.bin);;All(*.*)")
        if filename == '':
            return
        self.appdl.open(filename)
        
    @pyqtSlot()
    def on_actionImport_triggered(self):
        curpath = os.getcwd()
        filename,flt = QFileDialog.getOpenFileName(self,"Open the excel file",curpath,
               "regmap file(*.xlsx);;All(*.*)")
        if filename == '':
            return
        self.ui.reggetButton.setEnabled(True)
        self.ui.regsetButton.setEnabled(True)
        self.regmaps = RegMap()
        self.regmaps.load(filename)
        self._regblocks = self.regmaps.get_regblocks()
        self.ui.regmapComBox.addItems(self._regblocks)

    @pyqtSlot()
    def on_actionConnect_triggered(self):
        self.rx.connect(b'FT4222 A')
        self.ui.actionDisconnect.setEnabled(True)
        self.ui.actionImport.setEnabled(True)
        self.ui.actionOpen.setEnabled(True)
        self.ui.logStartButton.setEnabled(True)
        self.ui.logfileButton.setEnabled(True)
        if len(self._regblocks) > 0:
            self.ui.reggetButton.setEnabled(True)
            self.ui.regsetButton.setEnabled(True)
        self.ui.actionConnect.setDisabled(True)

    @pyqtSlot()
    def on_actionDisconnect_triggered(self):
        self.applogger.stop()
        self.ui.logStartButton.setText('Start')
        self.rx.disconnect()
        self.ui.actionDisconnect.setDisabled(True)
        self.ui.actionDownload.setDisabled(True)
        self.ui.actionImport.setDisabled(True)
        self.ui.actionOpen.setDisabled(True)
        self.ui.logStartButton.setDisabled(True)
        self.ui.logfileButton.setDisabled(True)
        self.ui.reggetButton.setDisabled(True)
        self.ui.regsetButton.setDisabled(True)        
        self.ui.actionConnect.setEnabled(True)

    @pyqtSlot()
    def on_actionDownload_triggered(self):
        if self.appdl.isActive() == True:
            return
        self.applogger.stop()
        self.ui.logStartButton.setText('Start')
        self.rx.writesram(0x50100088, 0x01)
        self.rx.writesram(0x50100031, 0x00)
        self.rx.writesram(0x50100038, 0xFF)
        self.rx.writesram(0x38000074, 0x10)
        self.rx.writesram(0x38000075, 0x10)
        self.rx.writesram(0x50020000, 0x00)
        self.rx.writesram(0x50020040, 0x00)
        self.rx.writesram(0x3800005F, 0x44)
        self.appdl.start()

    @pyqtSlot(str)
    def on_regmapComBox_currentIndexChanged(self, block):
        self.regmap = self.regmaps.get_regmap(block)
        self._ui_init_regmap(self.regmap)

    @pyqtSlot()
    def on_reggetButton_clicked(self):
        addrstr = self.ui.regaddrLineEdit.text()
        if addrstr == '':
            return
        try:
            addr = int(addrstr, 16)
            data = self.rx.regget(addr)
            if self._btngroup.checkedId() == 0:
                self.ui.regvalLineEdit.setText('0x{:02X}'.format(data))
            elif self._btngroup.checkedId() == 1:
                self.ui.regvalLineEdit.setText('{0}'.format(data))
            else:
                self.ui.regvalLineEdit.setText('0b{:b}'.format(data))
            if self._regindex != None:
                item = QStandardItem('0x{:02X}'.format(data))
                self.regmap_data_model.setItem(self._regindex.row(), 2, item)
        except ValueError:
            pass

    @pyqtSlot()
    def on_regsetButton_clicked(self):
        addrstr = self.ui.regaddrLineEdit.text()
        if addrstr == '':
            return
        datastr = self.ui.regvalLineEdit.text()
        if datastr == '':
            return
        try:
            data = int(datastr, 0)
            addr = int(addrstr, 16)
            self.rx.regset(addr, data)
            rdata = self.rx.regget(addr)
            if self._regindex != None:
                item = QStandardItem('0x{:02X}'.format(rdata))
                self.regmap_data_model.setItem(self._regindex.row(), 2, item)
        except ValueError:
            pass

    @pyqtSlot()
    def on_logStartButton_clicked(self):
        if self.ui.logStartButton.text() == 'Start':
            self.applogger.start()
            self.ui.logStartButton.setText('Stop')
        else:
            self.applogger.stop()
            self.ui.logStartButton.setText('Start')

    @pyqtSlot()
    def on_logfileButton_clicked(self):
        self.applogger.stop()
        self.ui.logStartButton.setText('Start')
        curpath = os.getcwd()
        filename,flt = QFileDialog.getOpenFileName(self,"Open the log file",curpath,
               "binary file(*.txt);;All(*.*)")
        if filename == '':
            self.ui.logilelineEdit.setText(filename)
            return
        self.ui.logilelineEdit.setText(filename)
        self.applogger.save(filename)
        pass

    def do_toggle_datafmt(self, id, checked):
        datastr = self.ui.regvalLineEdit.text()
        if datastr == '':
            return
        data = int(datastr, 0)
        if checked == True:
            if id == 0:
                self.ui.regvalLineEdit.setText('0x{:02X}'.format(data))
            elif id == 1:
                self.ui.regvalLineEdit.setText('{0}'.format(data))
            else:
                self.ui.regvalLineEdit.setText('0b{:b}'.format(data))
