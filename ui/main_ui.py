# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(898, 1002)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAcceptDrops(False)
        MainWindow.setStyleSheet(u"")
        self.actionabout = QAction(MainWindow)
        self.actionabout.setObjectName(u"actionabout")
        self.actionclose = QAction(MainWindow)
        self.actionclose.setObjectName(u"actionclose")
        self.actionopen = QAction(MainWindow)
        self.actionopen.setObjectName(u"actionopen")
        self.actiondesign = QAction(MainWindow)
        self.actiondesign.setObjectName(u"actiondesign")
        self.actionPowerlink = QAction(MainWindow)
        self.actionPowerlink.setObjectName(u"actionPowerlink")
        self.actionModbus = QAction(MainWindow)
        self.actionModbus.setObjectName(u"actionModbus")
        self.actionhelp = QAction(MainWindow)
        self.actionhelp.setObjectName(u"actionhelp")
        self.actionTcp_ip = QAction(MainWindow)
        self.actionTcp_ip.setObjectName(u"actionTcp_ip")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_1 = QFrame(self.frame)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setMaximumSize(QSize(16777215, 55))
        self.frame_1.setStyleSheet(u"")
        self.frame_1.setFrameShape(QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label_6 = QLabel(self.frame_1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_1)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)


        self.verticalLayout.addWidget(self.frame_1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMouseTracking(False)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.progressBar = QProgressBar(self.frame_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"   border: 1px solid grey;\n"
"   border-radius: 5px;\n"
"   background-color: #FFFFFF;\n"
"}\n"
"QProgressBar::chunk {\n"
"   background-color: rgb(117, 255, 202);\n"
"}\n"
"")
        self.progressBar.setValue(25)
        self.progressBar.setTextVisible(False)

        self.verticalLayout_3.addWidget(self.progressBar)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 800))
        self.frame_3.setStyleSheet(u"QPushButton{\n"
"min-width: 80px; max-width: 80px; max-height: 80px; min-height: 80px; border-radius: 40px;\n"
"border:0px solid #000;\n"
"background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.29602, fy:0.227, stop:0 rgba(255, 111, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(223, 121, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableWidget_2 = QTableWidget(self.frame_6)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget_2.rowCount() < 2):
            self.tableWidget_2.setRowCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setCheckState(Qt.Checked);
        self.tableWidget_2.setItem(0, 2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(1, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(1, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setCheckState(Qt.Checked);
        self.tableWidget_2.setItem(1, 2, __qtablewidgetitem10)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setAutoScroll(True)
        self.tableWidget_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setHighlightSections(True)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setHighlightSections(True)

        self.gridLayout_2.addWidget(self.tableWidget_2, 0, 1, 1, 2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pushButton_add = QPushButton(self.frame_6)
        self.pushButton_add.setObjectName(u"pushButton_add")

        self.verticalLayout_7.addWidget(self.pushButton_add)

        self.pushButton_delete = QPushButton(self.frame_6)
        self.pushButton_delete.setObjectName(u"pushButton_delete")

        self.verticalLayout_7.addWidget(self.pushButton_delete)


        self.gridLayout_2.addLayout(self.verticalLayout_7, 0, 0, 2, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBox = QCheckBox(self.frame_6)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.horizontalLayout_3.addWidget(self.checkBox)

        self.toolButton = QToolButton(self.frame_6)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setStyleSheet(u"QToolButton{\n"
"max-width: 20px; max-height: 20px;\n"
"width:20px;\n"
"height:20px;\n"
"border-radius: 5px;\n"
"border:1px solid #FFF;\n"
"text-align:center;\n"
"background-color:rgb(233, 185, 110)\n"
"}\n"
"QToolButton:hover{\n"
"	background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.75, fx:0.5, fy:0.5, stop:0 rgba(223, 121, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}")

        self.horizontalLayout_3.addWidget(self.toolButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.radioButton_1 = QRadioButton(self.frame_6)
        self.radioButton_1.setObjectName(u"radioButton_1")
        self.radioButton_1.setChecked(True)

        self.horizontalLayout_3.addWidget(self.radioButton_1)

        self.radioButton_2 = QRadioButton(self.frame_6)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_3.addWidget(self.radioButton_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.spinBox = QSpinBox(self.frame_6)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(10)
        self.spinBox.setMaximum(10000)
        self.spinBox.setValue(30)

        self.horizontalLayout_3.addWidget(self.spinBox)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_7)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_6.addWidget(self.label_10)


        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)

        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 0, 1, 1, 1)

        self.treeWidget_2 = QTreeWidget(self.frame_7)
        self.treeWidget_2.setObjectName(u"treeWidget_2")
        self.treeWidget_2.header().setDefaultSectionSize(150)
        self.treeWidget_2.header().setStretchLastSection(True)

        self.gridLayout.addWidget(self.treeWidget_2, 1, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.frame_7)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setStyleSheet(u"font: 75 9pt \"Ubuntu Mono\";\n"
"font-weight:bold;\n"
"background-color:rgb(255, 235, 220);")
        self.plainTextEdit.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.plainTextEdit.setOverwriteMode(False)

        self.gridLayout.addWidget(self.plainTextEdit, 1, 1, 1, 1)

        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.treeWidget_3 = QTreeWidget(self.frame_7)
        self.treeWidget_3.setObjectName(u"treeWidget_3")
        self.treeWidget_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.treeWidget_3.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.treeWidget_3.setHeaderHidden(False)
        self.treeWidget_3.header().setVisible(True)
        self.treeWidget_3.header().setCascadingSectionResizes(True)
        self.treeWidget_3.header().setMinimumSectionSize(75)
        self.treeWidget_3.header().setDefaultSectionSize(125)
        self.treeWidget_3.header().setStretchLastSection(True)

        self.gridLayout.addWidget(self.treeWidget_3, 3, 0, 1, 2)


        self.verticalLayout_9.addWidget(self.frame_7)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_open = QPushButton(self.frame_4)
        self.pushButton_open.setObjectName(u"pushButton_open")
        self.pushButton_open.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.pushButton_open)

        self.pushButton_design = QPushButton(self.frame_4)
        self.pushButton_design.setObjectName(u"pushButton_design")

        self.verticalLayout_4.addWidget(self.pushButton_design)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.treeWidget = QTreeWidget(self.frame_4)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setEnabled(True)
        self.treeWidget.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.treeWidget.setDragEnabled(False)
        self.treeWidget.setAlternatingRowColors(False)
        self.treeWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.treeWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.treeWidget.setUniformRowHeights(False)
        self.treeWidget.setItemsExpandable(True)
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.setAnimated(False)
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setCascadingSectionResizes(False)

        self.horizontalLayout_2.addWidget(self.treeWidget)


        self.verticalLayout_9.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.tableWidget = QTableWidget(self.frame_5)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_5.addWidget(self.tableWidget)


        self.verticalLayout_9.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_previous = QPushButton(self.frame)
        self.pushButton_previous.setObjectName(u"pushButton_previous")
        self.pushButton_previous.setStyleSheet(u"QPushButton{\n"
"min-width: 100px; max-width: 100px; max-height: 30px; min-height: 30px; border-radius: 15px;\n"
"border:2px solid rgb(163, 163, 163);\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.766169, y2:0.784, stop:0 rgba(255, 178, 102, 255), stop:0.746269 rgba(235, 148, 61, 255), stop:1 rgba(233, 178, 0, 255))\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid #fff\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.pushButton_previous)

        self.pushButton_next = QPushButton(self.frame)
        self.pushButton_next.setObjectName(u"pushButton_next")
        self.pushButton_next.setStyleSheet(u"QPushButton{\n"
"min-width: 100px; max-width: 100px; max-height: 30px; min-height: 30px; border-radius: 15px;\n"
"border:2px solid rgb(163, 163, 163);\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.766169, y2:0.784, stop:0 rgba(255, 178, 102, 255), stop:0.746269 rgba(235, 148, 61, 255), stop:1 rgba(233, 178, 0, 255))\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid #fff;\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.pushButton_next)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 898, 28))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_model = QMenu(self.menubar)
        self.menu_model.setObjectName(u"menu_model")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menubar.addAction(self.menu_model.menuAction())
        self.menu_file.addAction(self.actionopen)
        self.menu_file.addAction(self.actiondesign)
        self.menu_file.addAction(self.actionclose)
        self.menu_model.addAction(self.actionPowerlink)
        self.menu_model.addAction(self.actionModbus)
        self.menu_model.addAction(self.actionTcp_ip)
        self.menu_help.addAction(self.actionhelp)
        self.menu_help.addAction(self.actionabout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Zing", None))
        self.actionabout.setText(QCoreApplication.translate("MainWindow", u"\u7248\u672c\u4fe1\u606f", None))
        self.actionclose.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u6a21\u578b", None))
        self.actiondesign.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u8ba1\u6a21\u578b", None))
        self.actionPowerlink.setText(QCoreApplication.translate("MainWindow", u"Powerlink", None))
        self.actionModbus.setText(QCoreApplication.translate("MainWindow", u"Modbus", None))
        self.actionhelp.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u8bf4\u660e", None))
        self.actionTcp_ip.setText(QCoreApplication.translate("MainWindow", u"Tcp/ip", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u9009\u4e2d\u9879\u76ee\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u672a\u9009\u62e9\u6a21\u578b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u9009\u62e9", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u53d8\u91cf\u8bbe\u7f6e", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u8bbe\u7f6e", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u6267\u884c", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u7c7b\u578b", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u6027\u8d28", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u68c0\u67e5", None));
        ___qtablewidgetitem3 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem4 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"2", None));

        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.tableWidget_2.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u6b7b\u9501\u68c0\u67e5", None));
        ___qtablewidgetitem6 = self.tableWidget_2.item(0, 1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"DeadLock", None));
        ___qtablewidgetitem7 = self.tableWidget_2.item(0, 2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5", None));
        ___qtablewidgetitem8 = self.tableWidget_2.item(1, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u53ef\u8fbe\u5355\u5143\u683c", None));
        ___qtablewidgetitem9 = self.tableWidget_2.item(1, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Unreachable", None));
        ___qtablewidgetitem10 = self.tableWidget_2.item(1, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)

        self.pushButton_add.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.pushButton_delete.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u72b6\u6001\u7a7a\u95f4\u6811", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.radioButton_1.setText(QCoreApplication.translate("MainWindow", u"\u679d\u53bb\u91cd\u7b56\u7565", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"BMC\u7b56\u7565\u6df1\u5ea6", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u68c0\u67e5", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u72b6\u6001\u7a7a\u95f4\u6811", None))
        ___qtreewidgetitem = self.treeWidget_2.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u72b6\u6001", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u6027\u8d28", None));
        self.plainTextEdit.setPlainText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u53cd\u4f8b\u6b65\u9aa4\u5206\u6790", None))
        ___qtreewidgetitem1 = self.treeWidget_3.headerItem()
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"\u72b6\u6001\u7a7a\u95f4", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"\u6df1\u5ea6", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"\u72b6\u6001\u5750\u6807", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"STM", None));
        self.pushButton_open.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u6a21\u578b", None))
        self.pushButton_design.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u8ba1\u6a21\u578b", None))
        ___qtreewidgetitem2 = self.treeWidget.headerItem()
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"\u8bf4\u660e", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"\u9879\u76ee", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u8303\u56f4", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u7c7b\u578b", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u540d\u79f0", None));
        ___qtablewidgetitem14 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u521d\u59cb\u503c", None));
        self.pushButton_previous.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u6b65", None))
        self.pushButton_next.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u6b65", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_model.setTitle(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u6848\u4f8b", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

