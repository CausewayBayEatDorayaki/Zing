# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_ltl.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(450, 550)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Frame.sizePolicy().hasHeightForWidth())
        Frame.setSizePolicy(sizePolicy)
        Frame.setMinimumSize(QSize(450, 550))
        Frame.setMaximumSize(QSize(450, 550))
        self.lineEdit = QLineEdit(Frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 60, 391, 31))
        self.label = QLabel(Frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 161, 16))
        self.pushButton_1 = QPushButton(Frame)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(70, 110, 31, 28))
        self.pushButton_2 = QPushButton(Frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(110, 110, 31, 28))
        self.pushButton_3 = QPushButton(Frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(190, 110, 31, 28))
        self.pushButton_4 = QPushButton(Frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(150, 110, 31, 28))
        self.pushButton_5 = QPushButton(Frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(230, 110, 31, 28))
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_6 = QPushButton(Frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(30, 150, 31, 28))
        self.pushButton_7 = QPushButton(Frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(70, 150, 31, 28))
        self.pushButton_8 = QPushButton(Frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(110, 150, 31, 28))
        self.pushButton_9 = QPushButton(Frame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(150, 150, 31, 28))
        self.pushButton_10 = QPushButton(Frame)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(190, 150, 31, 28))
        self.pushButton_11 = QPushButton(Frame)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(230, 150, 31, 28))
        self.pushButton_12 = QPushButton(Frame)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(270, 150, 31, 28))
        self.pushButton_13 = QPushButton(Frame)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(310, 150, 31, 28))
        self.pushButton_14 = QPushButton(Frame)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(350, 150, 31, 28))
        self.pushButton_15 = QPushButton(Frame)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(390, 150, 31, 28))
        self.pushButton_16 = QPushButton(Frame)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(310, 110, 111, 28))
        self.pushButton_18 = QPushButton(Frame)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(210, 480, 93, 28))
        self.pushButton_17 = QPushButton(Frame)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(320, 480, 93, 28))
        self.label_2 = QLabel(Frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 200, 161, 16))
        self.pushButton_0 = QPushButton(Frame)
        self.pushButton_0.setObjectName(u"pushButton_0")
        self.pushButton_0.setGeometry(QRect(30, 110, 31, 28))
        self.listWidget = QListWidget(Frame)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(30, 230, 391, 211))

        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"\u5c5e\u6027\u7f16\u8f91", None))
        self.label.setText(QCoreApplication.translate("Frame", u"\u8f93\u5165\u8981\u68c0\u67e5\u7684LTL\u8bed\u53e5:", None))
        self.pushButton_1.setText(QCoreApplication.translate("Frame", u"[G]", None))
        self.pushButton_2.setText(QCoreApplication.translate("Frame", u"[F]", None))
        self.pushButton_3.setText(QCoreApplication.translate("Frame", u"[W]", None))
        self.pushButton_4.setText(QCoreApplication.translate("Frame", u"[U]", None))
        self.pushButton_5.setText(QCoreApplication.translate("Frame", u"[R]", None))
        self.pushButton_6.setText(QCoreApplication.translate("Frame", u"(", None))
        self.pushButton_7.setText(QCoreApplication.translate("Frame", u")", None))
        self.pushButton_8.setText(QCoreApplication.translate("Frame", u"==", None))
        self.pushButton_9.setText(QCoreApplication.translate("Frame", u"!=", None))
        self.pushButton_10.setText(QCoreApplication.translate("Frame", u">", None))
        self.pushButton_11.setText(QCoreApplication.translate("Frame", u"<", None))
        self.pushButton_12.setText(QCoreApplication.translate("Frame", u">=", None))
        self.pushButton_13.setText(QCoreApplication.translate("Frame", u"<=", None))
        self.pushButton_14.setText(QCoreApplication.translate("Frame", u"&&", None))
        self.pushButton_15.setText(QCoreApplication.translate("Frame", u"|", None))
        self.pushButton_16.setText(QCoreApplication.translate("Frame", u"\u4f7f\u7528\u8bf4\u660e", None))
        self.pushButton_18.setText(QCoreApplication.translate("Frame", u"\u786e\u8ba4", None))
        self.pushButton_17.setText(QCoreApplication.translate("Frame", u"\u53d6\u6d88", None))
        self.label_2.setText(QCoreApplication.translate("Frame", u"\u53d8\u91cf\u9009\u62e9\uff1a", None))
        self.pushButton_0.setText(QCoreApplication.translate("Frame", u"[X]", None))
    # retranslateUi

