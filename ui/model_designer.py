# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'model_designer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ModelDesigner(object):
    def setupUi(self, ModelDesigner):
        if not ModelDesigner.objectName():
            ModelDesigner.setObjectName(u"ModelDesigner")
        ModelDesigner.resize(697, 557)
        self.actionnewstm = QAction(ModelDesigner)
        self.actionnewstm.setObjectName(u"actionnewstm")
        self.actionopen = QAction(ModelDesigner)
        self.actionopen.setObjectName(u"actionopen")
        self.actionsave = QAction(ModelDesigner)
        self.actionsave.setObjectName(u"actionsave")
        self.actionclose = QAction(ModelDesigner)
        self.actionclose.setObjectName(u"actionclose")
        self.actionignore = QAction(ModelDesigner)
        self.actionignore.setObjectName(u"actionignore")
        self.actionnormal = QAction(ModelDesigner)
        self.actionnormal.setObjectName(u"actionnormal")
        self.actiondelete = QAction(ModelDesigner)
        self.actiondelete.setObjectName(u"actiondelete")
        self.actionfilemanager = QAction(ModelDesigner)
        self.actionfilemanager.setObjectName(u"actionfilemanager")
        self.actionnewproject = QAction(ModelDesigner)
        self.actionnewproject.setObjectName(u"actionnewproject")
        self.actionabout = QAction(ModelDesigner)
        self.actionabout.setObjectName(u"actionabout")
        self.actionPowerlink = QAction(ModelDesigner)
        self.actionPowerlink.setObjectName(u"actionPowerlink")
        self.actionModbus = QAction(ModelDesigner)
        self.actionModbus.setObjectName(u"actionModbus")
        self.actionhelp = QAction(ModelDesigner)
        self.actionhelp.setObjectName(u"actionhelp")
        self.centralwidget = QWidget(ModelDesigner)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mdiArea = QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(u"mdiArea")

        self.horizontalLayout.addWidget(self.mdiArea)

        ModelDesigner.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ModelDesigner)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 697, 28))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        ModelDesigner.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ModelDesigner)
        self.statusbar.setObjectName(u"statusbar")
        ModelDesigner.setStatusBar(self.statusbar)
        self.dockWidget = QDockWidget(ModelDesigner)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.dockWidget.setWidget(self.dockWidgetContents)
        ModelDesigner.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidget)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.actionnewproject)
        self.menu.addAction(self.actionnewstm)
        self.menu.addAction(self.actionopen)
        self.menu.addAction(self.actionsave)
        self.menu_2.addAction(self.actionfilemanager)
        self.menu_4.addAction(self.actionhelp)
        self.menu_4.addAction(self.actionabout)
        self.menu_3.addAction(self.actionPowerlink)
        self.menu_3.addAction(self.actionModbus)

        self.retranslateUi(ModelDesigner)

        QMetaObject.connectSlotsByName(ModelDesigner)
    # setupUi

    def retranslateUi(self, ModelDesigner):
        ModelDesigner.setWindowTitle(QCoreApplication.translate("ModelDesigner", u"Zing Model Designer", None))
        self.actionnewstm.setText(QCoreApplication.translate("ModelDesigner", u"\u65b0\u5efaSTM(&S)", None))
        self.actionopen.setText(QCoreApplication.translate("ModelDesigner", u"\u6253\u5f00(Ctrl+O)", None))
        self.actionsave.setText(QCoreApplication.translate("ModelDesigner", u"\u4fdd\u5b58(Ctrl+S)", None))
        self.actionclose.setText(QCoreApplication.translate("ModelDesigner", u"\u5173\u95ed", None))
        self.actionignore.setText(QCoreApplication.translate("ModelDesigner", u"\u5ffd\u7565\u5355\u5143\u683c", None))
        self.actionnormal.setText(QCoreApplication.translate("ModelDesigner", u"\u5e38\u89c4\u5355\u5143\u683c", None))
        self.actiondelete.setText(QCoreApplication.translate("ModelDesigner", u"\u5220\u9664", None))
        self.actionfilemanager.setText(QCoreApplication.translate("ModelDesigner", u"\u8d44\u6e90\u6d4f\u89c8\u5668", None))
        self.actionnewproject.setText(QCoreApplication.translate("ModelDesigner", u"\u65b0\u5efa\u5de5\u7a0b(&N)", None))
        self.actionabout.setText(QCoreApplication.translate("ModelDesigner", u"\u7248\u672c\u4fe1\u606f", None))
        self.actionPowerlink.setText(QCoreApplication.translate("ModelDesigner", u"PowerLink", None))
        self.actionModbus.setText(QCoreApplication.translate("ModelDesigner", u"ModBus", None))
        self.actionhelp.setText(QCoreApplication.translate("ModelDesigner", u"\u4f7f\u7528\u8bf4\u660e", None))
        self.menu.setTitle(QCoreApplication.translate("ModelDesigner", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("ModelDesigner", u"\u89c6\u56fe", None))
        self.menu_4.setTitle(QCoreApplication.translate("ModelDesigner", u"\u5e2e\u52a9", None))
        self.menu_3.setTitle(QCoreApplication.translate("ModelDesigner", u"\u6a21\u578b\u6848\u4f8b", None))
    # retranslateUi

