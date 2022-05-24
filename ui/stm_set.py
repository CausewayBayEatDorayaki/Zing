# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stm_set.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_StmSetDialog(object):
    def setupUi(self, StmSetDialog):
        if not StmSetDialog.objectName():
            StmSetDialog.setObjectName(u"StmSetDialog")
        StmSetDialog.resize(350, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StmSetDialog.sizePolicy().hasHeightForWidth())
        StmSetDialog.setSizePolicy(sizePolicy)
        StmSetDialog.setMinimumSize(QSize(350, 200))
        StmSetDialog.setMaximumSize(QSize(350, 200))
        self.spinBox_row = QSpinBox(StmSetDialog)
        self.spinBox_row.setObjectName(u"spinBox_row")
        self.spinBox_row.setGeometry(QRect(40, 100, 81, 22))
        self.spinBox_row.setMinimum(1)
        self.spinBox_row.setValue(2)
        self.spinBox_column = QSpinBox(StmSetDialog)
        self.spinBox_column.setObjectName(u"spinBox_column")
        self.spinBox_column.setGeometry(QRect(230, 100, 81, 22))
        self.spinBox_column.setMinimum(1)
        self.spinBox_column.setValue(2)
        self.label = QLabel(StmSetDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 72, 15))
        self.label_2 = QLabel(StmSetDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 80, 72, 15))
        self.label_3 = QLabel(StmSetDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 80, 72, 15))
        self.lineEdit = QLineEdit(StmSetDialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(40, 50, 271, 21))
        self.lineEdit.setClearButtonEnabled(False)
        self.pushButton_confirm = QPushButton(StmSetDialog)
        self.pushButton_confirm.setObjectName(u"pushButton_confirm")
        self.pushButton_confirm.setGeometry(QRect(220, 150, 93, 28))

        self.retranslateUi(StmSetDialog)

        QMetaObject.connectSlotsByName(StmSetDialog)
    # setupUi

    def retranslateUi(self, StmSetDialog):
        StmSetDialog.setWindowTitle(QCoreApplication.translate("StmSetDialog", u"\u65b0\u5efaSTM", None))
        self.spinBox_row.setPrefix("")
        self.spinBox_column.setSuffix("")
        self.spinBox_column.setPrefix("")
        self.label.setText(QCoreApplication.translate("StmSetDialog", u"STM\u540d\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("StmSetDialog", u"\u5217:", None))
        self.label_3.setText(QCoreApplication.translate("StmSetDialog", u"\u884c:", None))
        self.lineEdit.setText(QCoreApplication.translate("StmSetDialog", u"stm_name", None))
        self.pushButton_confirm.setText(QCoreApplication.translate("StmSetDialog", u"\u521b\u5efa", None))
    # retranslateUi

