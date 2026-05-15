# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EMGToolPagecijhky.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)
from . import main_rc

class Ui_EMGToolPage(object):
    def setupUi(self, EMGToolPage):
        if not EMGToolPage.objectName():
            EMGToolPage.setObjectName(u"EMGToolPage")
        EMGToolPage.resize(443, 368)
        EMGToolPage.setMinimumSize(QSize(443, 368))
        EMGToolPage.setMaximumSize(QSize(443, 368))
        icon = QIcon()
        icon.addFile(u":/logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        EMGToolPage.setWindowIcon(icon)
        self.Tips = QLabel(EMGToolPage)
        self.Tips.setObjectName(u"Tips")
        self.Tips.setGeometry(QRect(0, 20, 441, 91))
        self.FAK360 = QPushButton(EMGToolPage)
        self.FAK360.setObjectName(u"FAK360")
        self.FAK360.setGeometry(QRect(27, 145, 101, 41))
        self.DX = QPushButton(EMGToolPage)
        self.DX.setObjectName(u"DX")
        self.DX.setGeometry(QRect(167, 145, 101, 41))
        self.pushButton_3 = QPushButton(EMGToolPage)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(307, 145, 101, 41))
        self.GoExplorer = QPushButton(EMGToolPage)
        self.GoExplorer.setObjectName(u"Go_Explorer")
        self.GoExplorer.setGeometry(QRect(167, 275, 111, 41))
        self.label_2 = QLabel(EMGToolPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 210, 201, 51))

        self.retranslateUi(EMGToolPage)

        QMetaObject.connectSlotsByName(EMGToolPage)
    # setupUi

    def retranslateUi(self, EMGToolPage):
        EMGToolPage.setWindowTitle(QCoreApplication.translate("EMGToolPage", u"Form", None))
        self.Tips.setText(QCoreApplication.translate("EMGToolPage", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">\u7d27\u6025\u5de5\u5177\u4e3a\u672c\u5730\u5de5\u5177\u65e0\u9700\u4e0b\u8f7d</span></p></body></html>", None))
        self.FAK360.setText(QCoreApplication.translate("EMGToolPage", u"360\u6025\u6551\u7bb1", None))
        self.DX.setText(QCoreApplication.translate("EMGToolPage", u"DirectX", None))
        self.pushButton_3.setText(QCoreApplication.translate("EMGToolPage", u"FixWin", None))
        self.GoExplorer.setText(QCoreApplication.translate("EMGToolPage", u"\u524d\u5f80\u8d44\u6e90\u7ba1\u7406\u5668", None))
        self.label_2.setText(QCoreApplication.translate("EMGToolPage", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">\u65e0\u6cd5\u6253\u5f00\uff1f</span></p></body></html>", None))
    # retranslateUi

