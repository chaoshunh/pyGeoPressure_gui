# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pygeopressure.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1068, 628)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.DataTree = QtGui.QTreeWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DataTree.sizePolicy().hasHeightForWidth())
        self.DataTree.setSizePolicy(sizePolicy)
        self.DataTree.setMinimumSize(QtCore.QSize(40, 0))
        self.DataTree.setMaximumSize(QtCore.QSize(200, 16777215))
        self.DataTree.setBaseSize(QtCore.QSize(0, 0))
        self.DataTree.setToolTip(_fromUtf8(""))
        self.DataTree.setObjectName(_fromUtf8("DataTree"))
        self.DataTree.headerItem().setText(0, _fromUtf8("1"))
        self.tabWidget = QtGui.QTabWidget(self.splitter)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_seis = QtGui.QWidget()
        self.tab_seis.setObjectName(_fromUtf8("tab_seis"))
        self.tabWidget.addTab(self.tab_seis, _fromUtf8(""))
        self.toolBox = QtGui.QToolBox(self.splitter)
        self.toolBox.setMinimumSize(QtCore.QSize(240, 0))
        self.toolBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page_Velocity = QtGui.QWidget()
        self.page_Velocity.setObjectName(_fromUtf8("page_Velocity"))
        self.formLayoutWidget_2 = QtGui.QWidget(self.page_Velocity)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 241, 111))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_3 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_3.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_4 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.comboBox_2 = QtGui.QComboBox(self.formLayoutWidget_2)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox_2)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.comboBox_3 = QtGui.QComboBox(self.formLayoutWidget_2)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBox_3)
        self.label_5 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_4 = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_4)
        self.pushButton_3 = QtGui.QPushButton(self.formLayoutWidget_2)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.pushButton_3)
        spacerItem = QtGui.QSpacerItem(80, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout_3.setItem(3, QtGui.QFormLayout.LabelRole, spacerItem)
        self.toolBox.addItem(self.page_Velocity, _fromUtf8(""))
        self.page_tdc = QtGui.QWidget()
        self.page_tdc.setObjectName(_fromUtf8("page_tdc"))
        self.formLayoutWidget_3 = QtGui.QWidget(self.page_tdc)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 241, 109))
        self.formLayoutWidget_3.setObjectName(_fromUtf8("formLayoutWidget_3"))
        self.formLayout_4 = QtGui.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_4.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.label_6 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_6)
        self.comboBox_6 = QtGui.QComboBox(self.formLayoutWidget_3)
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox_6)
        self.label_7 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_7)
        self.comboBox_7 = QtGui.QComboBox(self.formLayoutWidget_3)
        self.comboBox_7.setObjectName(_fromUtf8("comboBox_7"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBox_7)
        self.label_8 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_5 = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_5)
        spacerItem1 = QtGui.QSpacerItem(80, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout_4.setItem(3, QtGui.QFormLayout.LabelRole, spacerItem1)
        self.pushButton_4 = QtGui.QPushButton(self.formLayoutWidget_3)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.FieldRole, self.pushButton_4)
        self.toolBox.addItem(self.page_tdc, _fromUtf8(""))
        self.page_gardner = QtGui.QWidget()
        self.page_gardner.setObjectName(_fromUtf8("page_gardner"))
        self.formLayoutWidget_4 = QtGui.QWidget(self.page_gardner)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 241, 129))
        self.formLayoutWidget_4.setObjectName(_fromUtf8("formLayoutWidget_4"))
        self.formLayout_5 = QtGui.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_5.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.label_11 = QtGui.QLabel(self.formLayoutWidget_4)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_2 = QtGui.QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_12 = QtGui.QLabel(self.formLayoutWidget_4)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_3 = QtGui.QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_9 = QtGui.QLabel(self.formLayoutWidget_4)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_9)
        self.comboBox_5 = QtGui.QComboBox(self.formLayoutWidget_4)
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.FieldRole, self.comboBox_5)
        self.label_10 = QtGui.QLabel(self.formLayoutWidget_4)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_5.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_10)
        self.lineEdit = QtGui.QLineEdit(self.formLayoutWidget_4)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout_5.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit)
        spacerItem2 = QtGui.QSpacerItem(80, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout_5.setItem(4, QtGui.QFormLayout.LabelRole, spacerItem2)
        self.pushButton_5 = QtGui.QPushButton(self.formLayoutWidget_4)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.formLayout_5.setWidget(4, QtGui.QFormLayout.FieldRole, self.pushButton_5)
        self.toolBox.addItem(self.page_gardner, _fromUtf8(""))
        self.page_obp = QtGui.QWidget()
        self.page_obp.setObjectName(_fromUtf8("page_obp"))
        self.formLayoutWidget_5 = QtGui.QWidget(self.page_obp)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 241, 81))
        self.formLayoutWidget_5.setObjectName(_fromUtf8("formLayoutWidget_5"))
        self.formLayout_6 = QtGui.QFormLayout(self.formLayoutWidget_5)
        self.formLayout_6.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_6.setObjectName(_fromUtf8("formLayout_6"))
        self.label_13 = QtGui.QLabel(self.formLayoutWidget_5)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_13)
        self.comboBox_4 = QtGui.QComboBox(self.formLayoutWidget_5)
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox_4)
        self.label_14 = QtGui.QLabel(self.formLayoutWidget_5)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_14)
        self.lineEdit_6 = QtGui.QLineEdit(self.formLayoutWidget_5)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_6)
        spacerItem3 = QtGui.QSpacerItem(80, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout_6.setItem(2, QtGui.QFormLayout.LabelRole, spacerItem3)
        self.pushButton_6 = QtGui.QPushButton(self.formLayoutWidget_5)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.formLayout_6.setWidget(2, QtGui.QFormLayout.FieldRole, self.pushButton_6)
        self.toolBox.addItem(self.page_obp, _fromUtf8(""))
        self.page_eaton = QtGui.QWidget()
        self.page_eaton.setEnabled(True)
        self.page_eaton.setGeometry(QtCore.QRect(0, 0, 300, 407))
        self.page_eaton.setAccessibleName(_fromUtf8(""))
        self.page_eaton.setObjectName(_fromUtf8("page_eaton"))
        self.gridLayoutWidget = QtGui.QWidget(self.page_eaton)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 241, 135))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.gridLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.comboBox = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.pushButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.pushButton)
        spacerItem4 = QtGui.QSpacerItem(80, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout.setItem(5, QtGui.QFormLayout.LabelRole, spacerItem4)
        self.spinBox = QtGui.QSpinBox(self.gridLayoutWidget)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.spinBox)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_17 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_17)
        self.lineEdit_8 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_8)
        self.label_18 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_18)
        self.lineEdit_9 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_9)
        self.toolBox.addItem(self.page_eaton, _fromUtf8(""))
        self.page_bowers = QtGui.QWidget()
        self.page_bowers.setGeometry(QtCore.QRect(0, 0, 300, 407))
        self.page_bowers.setObjectName(_fromUtf8("page_bowers"))
        self.formLayoutWidget = QtGui.QWidget(self.page_bowers)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 241, 155))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.wellLabel = QtGui.QLabel(self.formLayoutWidget)
        self.wellLabel.setObjectName(_fromUtf8("wellLabel"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.wellLabel)
        self.wellComboBox = QtGui.QComboBox(self.formLayoutWidget)
        self.wellComboBox.setObjectName(_fromUtf8("wellComboBox"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.wellComboBox)
        self.aLabel = QtGui.QLabel(self.formLayoutWidget)
        self.aLabel.setObjectName(_fromUtf8("aLabel"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.aLabel)
        self.aLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.aLineEdit.setObjectName(_fromUtf8("aLineEdit"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.aLineEdit)
        self.bLabel = QtGui.QLabel(self.formLayoutWidget)
        self.bLabel.setObjectName(_fromUtf8("bLabel"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.bLabel)
        self.bLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.bLineEdit.setObjectName(_fromUtf8("bLineEdit"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.bLineEdit)
        spacerItem5 = QtGui.QSpacerItem(80, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout_2.setItem(5, QtGui.QFormLayout.LabelRole, spacerItem5)
        self.pushButton_2 = QtGui.QPushButton(self.formLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.pushButton_2)
        self.label_15 = QtGui.QLabel(self.formLayoutWidget)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_15)
        self.label_16 = QtGui.QLabel(self.formLayoutWidget)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_16)
        self.comboBox_8 = QtGui.QComboBox(self.formLayoutWidget)
        self.comboBox_8.setObjectName(_fromUtf8("comboBox_8"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox_8)
        self.lineEdit_7 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_7)
        self.toolBox.addItem(self.page_bowers, _fromUtf8(""))
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1068, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuData = QtGui.QMenu(self.menubar)
        self.menuData.setObjectName(_fromUtf8("menuData"))
        self.menuImport = QtGui.QMenu(self.menuData)
        self.menuImport.setObjectName(_fromUtf8("menuImport"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuWindow = QtGui.QMenu(self.menubar)
        self.menuWindow.setObjectName(_fromUtf8("menuWindow"))
        self.menuSurvey = QtGui.QMenu(self.menubar)
        self.menuSurvey.setObjectName(_fromUtf8("menuSurvey"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport = QtGui.QAction(MainWindow)
        self.actionImport.setCheckable(False)
        self.actionImport.setObjectName(_fromUtf8("actionImport"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionOutput = QtGui.QAction(MainWindow)
        self.actionOutput.setObjectName(_fromUtf8("actionOutput"))
        self.actionWell_Log = QtGui.QAction(MainWindow)
        self.actionWell_Log.setObjectName(_fromUtf8("actionWell_Log"))
        self.actionSeismic = QtGui.QAction(MainWindow)
        self.actionSeismic.setObjectName(_fromUtf8("actionSeismic"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.action2D_Time = QtGui.QAction(MainWindow)
        self.action2D_Time.setObjectName(_fromUtf8("action2D_Time"))
        self.action3D_Time = QtGui.QAction(MainWindow)
        self.action3D_Time.setObjectName(_fromUtf8("action3D_Time"))
        self.action2D_Depth = QtGui.QAction(MainWindow)
        self.action2D_Depth.setObjectName(_fromUtf8("action2D_Depth"))
        self.action3D_Depth = QtGui.QAction(MainWindow)
        self.action3D_Depth.setObjectName(_fromUtf8("action3D_Depth"))
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionNewSurvey = QtGui.QAction(MainWindow)
        self.actionNewSurvey.setObjectName(_fromUtf8("actionNewSurvey"))
        self.actionDocumentation = QtGui.QAction(MainWindow)
        self.actionDocumentation.setObjectName(_fromUtf8("actionDocumentation"))
        self.actionOpen_2 = QtGui.QAction(MainWindow)
        self.actionOpen_2.setObjectName(_fromUtf8("actionOpen_2"))
        self.actionSelectSurvey = QtGui.QAction(MainWindow)
        self.actionSelectSurvey.setObjectName(_fromUtf8("actionSelectSurvey"))
        self.actionMapView = QtGui.QAction(MainWindow)
        self.actionMapView.setObjectName(_fromUtf8("actionMapView"))
        self.actionSectionView = QtGui.QAction(MainWindow)
        self.actionSectionView.setObjectName(_fromUtf8("actionSectionView"))
        self.actionManageSeismic = QtGui.QAction(MainWindow)
        self.actionManageSeismic.setObjectName(_fromUtf8("actionManageSeismic"))
        self.actionWellLogView = QtGui.QAction(MainWindow)
        self.actionWellLogView.setObjectName(_fromUtf8("actionWellLogView"))
        self.menuImport.addAction(self.actionWell_Log)
        self.menuData.addAction(self.menuImport.menuAction())
        self.menuData.addAction(self.actionOutput)
        self.menuData.addSeparator()
        self.menuData.addAction(self.actionManageSeismic)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuWindow.addAction(self.action3D_Time)
        self.menuWindow.addAction(self.action3D_Depth)
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.actionMapView)
        self.menuWindow.addAction(self.actionSectionView)
        self.menuWindow.addAction(self.actionWellLogView)
        self.menuSurvey.addAction(self.actionSelectSurvey)
        self.menuSurvey.addAction(self.actionNewSurvey)
        self.menuSurvey.addAction(self.actionOpen_2)
        self.menuSurvey.addSeparator()
        self.menuSurvey.addAction(self.actionExit)
        self.menubar.addAction(self.menuSurvey.menuAction())
        self.menubar.addAction(self.menuData.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(5)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "pyGeoPressure", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_seis), _translate("MainWindow", "Seismic 3D", None))
        self.label_4.setText(_translate("MainWindow", "Conversion Type", None))
        self.label_3.setText(_translate("MainWindow", "INPUT", None))
        self.label_5.setText(_translate("MainWindow", "OUTPUT", None))
        self.pushButton_3.setText(_translate("MainWindow", "Run", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_Velocity), _translate("MainWindow", "Velocity Conversion", None))
        self.label_6.setText(_translate("MainWindow", "Average Velocity", None))
        self.label_7.setText(_translate("MainWindow", "INPUT", None))
        self.label_8.setText(_translate("MainWindow", "OUTPUT", None))
        self.pushButton_4.setText(_translate("MainWindow", "Run", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_tdc), _translate("MainWindow", "Time Depth Conversion", None))
        self.label_11.setText(_translate("MainWindow", "           Gardner A", None))
        self.label_12.setText(_translate("MainWindow", "Gardner B", None))
        self.label_9.setText(_translate("MainWindow", "Interval Velocity", None))
        self.label_10.setText(_translate("MainWindow", "OUTPUT", None))
        self.pushButton_5.setText(_translate("MainWindow", "Run", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_gardner), _translate("MainWindow", "Density Conversion", None))
        self.label_13.setText(_translate("MainWindow", "Density", None))
        self.label_14.setText(_translate("MainWindow", "OUTPUT", None))
        self.pushButton_6.setText(_translate("MainWindow", "Run", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_obp), _translate("MainWindow", "Overburden Pressure Calculation", None))
        self.label.setText(_translate("MainWindow", "OBP", None))
        self.pushButton.setText(_translate("MainWindow", "Calculate", None))
        self.label_2.setText(_translate("MainWindow", "N", None))
        self.label_17.setText(_translate("MainWindow", "NCT a", None))
        self.label_18.setText(_translate("MainWindow", "NCT b", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_eaton), _translate("MainWindow", "Eaton Method", None))
        self.wellLabel.setText(_translate("MainWindow", "Interval Velocity", None))
        self.aLabel.setText(_translate("MainWindow", "a", None))
        self.bLabel.setText(_translate("MainWindow", "b", None))
        self.pushButton_2.setText(_translate("MainWindow", "Calculate", None))
        self.label_15.setText(_translate("MainWindow", "OUTPUT", None))
        self.label_16.setText(_translate("MainWindow", "OBP", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_bowers), _translate("MainWindow", "Bowers Method", None))
        self.menuData.setTitle(_translate("MainWindow", "Data", None))
        self.menuImport.setTitle(_translate("MainWindow", "Import", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuWindow.setTitle(_translate("MainWindow", "Scene", None))
        self.menuSurvey.setTitle(_translate("MainWindow", "Survey", None))
        self.actionImport.setText(_translate("MainWindow", "Import", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionOutput.setText(_translate("MainWindow", "Output", None))
        self.actionWell_Log.setText(_translate("MainWindow", "Well Log", None))
        self.actionSeismic.setText(_translate("MainWindow", "Seismic", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.action2D_Time.setText(_translate("MainWindow", "2D - Time", None))
        self.action3D_Time.setText(_translate("MainWindow", "3D - Time", None))
        self.action2D_Depth.setText(_translate("MainWindow", "2D - Depth", None))
        self.action3D_Depth.setText(_translate("MainWindow", "3D - Depth", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionNewSurvey.setText(_translate("MainWindow", "New", None))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation", None))
        self.actionOpen_2.setText(_translate("MainWindow", "Open", None))
        self.actionSelectSurvey.setText(_translate("MainWindow", "Select/Setup", None))
        self.actionMapView.setText(_translate("MainWindow", "Map view", None))
        self.actionSectionView.setText(_translate("MainWindow", "Section", None))
        self.actionManageSeismic.setText(_translate("MainWindow", "Seismic", None))
        self.actionWellLogView.setText(_translate("MainWindow", "Well log", None))

