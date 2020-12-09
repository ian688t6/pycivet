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
        MainWindow.resize(801, 507)
        MainWindow.setStyleSheet("font: 10pt \"Source Code Pro\";\n")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.groupBox_5 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_5)
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setObjectName("tabWidget")
        self.binfileTab = QtWidgets.QWidget()
        self.binfileTab.setObjectName("binfileTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.binfileTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.binTabView = QtWidgets.QTableView(self.binfileTab)
        self.binTabView.setObjectName("binTabView")
        self.verticalLayout_3.addWidget(self.binTabView)
        self.tabWidget.addTab(self.binfileTab, "")
        self.regmapTab = QtWidgets.QWidget()
        self.regmapTab.setObjectName("regmapTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.regmapTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.regmapTab)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.reggetButton = QtWidgets.QPushButton(self.groupBox_2)
        self.reggetButton.setObjectName("reggetButton")
        self.gridLayout.addWidget(self.reggetButton, 1, 0, 1, 1)
        self.regaddrLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.regaddrLineEdit.setObjectName("regaddrLineEdit")
        self.gridLayout.addWidget(self.regaddrLineEdit, 1, 1, 1, 3)
        self.regvalLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.regvalLineEdit.setObjectName("regvalLineEdit")
        self.gridLayout.addWidget(self.regvalLineEdit, 2, 1, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 4, 1, 1)
        self.decRadioBtn = QtWidgets.QRadioButton(self.groupBox_2)
        self.decRadioBtn.setObjectName("decRadioBtn")
        self.gridLayout.addWidget(self.decRadioBtn, 3, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 4, 1, 1)
        self.binRadioBtn = QtWidgets.QRadioButton(self.groupBox_2)
        self.binRadioBtn.setObjectName("binRadioBtn")
        self.gridLayout.addWidget(self.binRadioBtn, 3, 1, 1, 1)
        self.regsetButton = QtWidgets.QPushButton(self.groupBox_2)
        self.regsetButton.setObjectName("regsetButton")
        self.gridLayout.addWidget(self.regsetButton, 2, 0, 1, 1)
        self.hexRadioBtn = QtWidgets.QRadioButton(self.groupBox_2)
        self.hexRadioBtn.setObjectName("hexRadioBtn")
        self.gridLayout.addWidget(self.hexRadioBtn, 3, 2, 1, 1)
        self.datafmtLabel = QtWidgets.QLabel(self.groupBox_2)
        self.datafmtLabel.setObjectName("datafmtLabel")
        self.gridLayout.addWidget(self.datafmtLabel, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.regmapComBox = QtWidgets.QComboBox(self.groupBox_2)
        self.regmapComBox.setObjectName("regmapComBox")
        self.gridLayout.addWidget(self.regmapComBox, 0, 1, 1, 3)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.regmapTabView = QtWidgets.QTableView(self.regmapTab)
        self.regmapTabView.setObjectName("regmapTabView")
        self.verticalLayout.addWidget(self.regmapTabView)
        self.tabWidget.addTab(self.regmapTab, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.groupBox_4 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.logStartButton = QtWidgets.QPushButton(self.groupBox_4)
        self.logStartButton.setObjectName("logStartButton")
        self.gridLayout_3.addWidget(self.logStartButton, 0, 0, 1, 1)
        self.logfileButton = QtWidgets.QPushButton(self.groupBox_4)
        self.logfileButton.setObjectName("logfileButton")
        self.gridLayout_3.addWidget(self.logfileButton, 0, 1, 1, 1)
        self.logilelineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.logilelineEdit.setObjectName("logilelineEdit")
        self.gridLayout_3.addWidget(self.logilelineEdit, 0, 2, 1, 1)
        self.logPlainText = QtWidgets.QPlainTextEdit(self.groupBox_4)
        self.logPlainText.setObjectName("logPlainText")
        self.gridLayout_3.addWidget(self.logPlainText, 1, 0, 1, 3)
        self.horizontalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 22))
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
        self.groupBox_5.setTitle(_translate("MainWindow", "Control Panel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.binfileTab), _translate("MainWindow", "Binary File"))
        self.groupBox.setTitle(_translate("MainWindow", "Register Block"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Reg R/W"))
        self.reggetButton.setText(_translate("MainWindow", "Get"))
        self.decRadioBtn.setText(_translate("MainWindow", "dec"))
        self.binRadioBtn.setText(_translate("MainWindow", "bin"))
        self.regsetButton.setText(_translate("MainWindow", "Set"))
        self.hexRadioBtn.setText(_translate("MainWindow", "hex"))
        self.datafmtLabel.setText(_translate("MainWindow", "Data format:"))
        self.label.setText(_translate("MainWindow", "Select map"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.regmapTab), _translate("MainWindow", "Register Map"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Console"))
        self.logStartButton.setText(_translate("MainWindow", "Start"))
        self.logfileButton.setText(_translate("MainWindow", "Logfile"))
        self.mainToolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setToolTip(_translate("MainWindow", "Open firmware bin file"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionImport.setToolTip(_translate("MainWindow", "Import the register map file"))
        self.actionConnect.setText(_translate("MainWindow", "Connect"))
        self.actionConnect.setToolTip(_translate("MainWindow", "Connect the device"))
        self.actionDisconnect.setText(_translate("MainWindow", "Disconnect"))
        self.actionDisconnect.setToolTip(_translate("MainWindow", "Disconnect the device"))
        self.actionDownload.setText(_translate("MainWindow", "Download"))
        self.actionDownload.setToolTip(_translate("MainWindow", "Download the firmware"))
