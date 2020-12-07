# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.tab)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout.addWidget(self.plainTextEdit_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.regmapComBox = QtWidgets.QComboBox(self.groupBox)
        self.regmapComBox.setObjectName("regmapComBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.regmapComBox)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tableView = QtWidgets.QTableView(self.tab_2)
        self.tableView.setObjectName("tableView")
        self.gridLayout_2.addWidget(self.tableView, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.splitter)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/binary.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionImport = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/import.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImport.setIcon(icon1)
        self.actionImport.setObjectName("actionImport")
        self.actionConnect = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/connect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConnect.setIcon(icon2)
        self.actionConnect.setObjectName("actionConnect")
        self.actionDisconnect = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/disconnect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDisconnect.setIcon(icon3)
        self.actionDisconnect.setObjectName("actionDisconnect")
        self.actionDownload = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDownload.setIcon(icon4)
        self.actionDownload.setObjectName("actionDownload")
        self.mainToolBar.addAction(self.actionOpen)
        self.mainToolBar.addAction(self.actionImport)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionConnect)
        self.mainToolBar.addAction(self.actionDisconnect)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionDownload)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Binary File"))
        self.groupBox.setTitle(_translate("MainWindow", "Register Block"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Register Map"))
        self.mainToolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionConnect.setText(_translate("MainWindow", "Connect"))
        self.actionConnect.setToolTip(_translate("MainWindow", "Connect"))
        self.actionDisconnect.setText(_translate("MainWindow", "Disconnect"))
        self.actionDisconnect.setToolTip(_translate("MainWindow", "Disconnect"))
        self.actionDownload.setText(_translate("MainWindow", "Download"))