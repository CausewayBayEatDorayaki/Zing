# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_project.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_NewProjectDialog(object):
    def setupUi(self, NewProjectDialog):
        if not NewProjectDialog.objectName():
            NewProjectDialog.setObjectName(u"NewProjectDialog")
        NewProjectDialog.resize(490, 255)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NewProjectDialog.sizePolicy().hasHeightForWidth())
        NewProjectDialog.setSizePolicy(sizePolicy)
        NewProjectDialog.setMinimumSize(QSize(490, 255))
        NewProjectDialog.setMaximumSize(QSize(490, 255))
        self.label = QLabel(NewProjectDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 141, 17))
        self.lineEdit_path = QLineEdit(NewProjectDialog)
        self.lineEdit_path.setObjectName(u"lineEdit_path")
        self.lineEdit_path.setGeometry(QRect(30, 60, 391, 31))
        self.toolButton = QToolButton(NewProjectDialog)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(430, 60, 31, 31))
        self.pushButton = QPushButton(NewProjectDialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(370, 200, 89, 25))
        self.lineEdit_name = QLineEdit(NewProjectDialog)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setGeometry(QRect(30, 140, 391, 31))
        self.label_2 = QLabel(NewProjectDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 110, 141, 17))

        self.retranslateUi(NewProjectDialog)

        QMetaObject.connectSlotsByName(NewProjectDialog)
    # setupUi

    def retranslateUi(self, NewProjectDialog):
        NewProjectDialog.setWindowTitle(QCoreApplication.translate("NewProjectDialog", u"\u65b0\u5efa\u5de5\u7a0b", None))
        self.label.setText(QCoreApplication.translate("NewProjectDialog", u"\u8bbe\u7f6e\u5de5\u4f5c\u7a7a\u95f4\u8def\u5f84\uff1a", None))
        self.toolButton.setText(QCoreApplication.translate("NewProjectDialog", u"...", None))
        self.pushButton.setText(QCoreApplication.translate("NewProjectDialog", u"\u521b\u5efa", None))
        self.label_2.setText(QCoreApplication.translate("NewProjectDialog", u"\u5de5\u7a0b\u540d\u79f0\uff1a", None))
    # retranslateUi

