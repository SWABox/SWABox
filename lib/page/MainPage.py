# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainPageSHbbGZ.ui'
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

class Ui_MainPage(object):
    def setupUi(self, MainPage):
        if not MainPage.objectName():
            MainPage.setObjectName(u"MainPage")
        MainPage.resize(413, 356)
        MainPage.setMinimumSize(QSize(413, 356))
        MainPage.setMaximumSize(QSize(413, 356))
        icon1 = QIcon()
        icon1.addFile(u":/logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainPage.setWindowIcon(icon1)
        self.icon = QLabel(MainPage)
        self.icon.setObjectName(u"icon")
        self.icon.setEnabled(True)
        self.icon.setGeometry(QRect(40, 30, 121, 121))
        self.icon.setPixmap(QPixmap(u":/logo.png"))
        self.icon.setScaledContents(True)
        self.title = QLabel(MainPage)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(150, 30, 251, 121))
        self.settings = QPushButton(MainPage)
        self.settings.setObjectName(u"settings")
        self.settings.setGeometry(QRect(290, 160, 91, 51))
        self.exit = QPushButton(MainPage)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(290, 280, 91, 51))
        self.exit.setStyleSheet(u"")
        self.help = QPushButton(MainPage)
        self.help.setObjectName(u"help")
        self.help.setGeometry(QRect(290, 220, 91, 51))
        self.OfTool = QPushButton(MainPage)
        self.OfTool.setObjectName(u"OfTool")
        self.OfTool.setGeometry(QRect(30, 170, 161, 41))
        self.FixTool = QPushButton(MainPage)
        self.FixTool.setObjectName(u"FixTool")
        self.FixTool.setGeometry(QRect(30, 210, 161, 41))
        self.PtTool = QPushButton(MainPage)
        self.PtTool.setObjectName(u"PtTool")
        self.PtTool.setGeometry(QRect(30, 250, 161, 41))
        self.MtTool = QPushButton(MainPage)
        self.MtTool.setObjectName(u"MtTool")
        self.MtTool.setGeometry(QRect(30, 290, 161, 41))
        self.EMGTool = QPushButton(MainPage)
        self.EMGTool.setObjectName(u"EMGTool")
        self.EMGTool.setGeometry(QRect(200, 160, 83, 81))
        self.GoWeb = QPushButton(MainPage)
        self.GoWeb.setObjectName(u"GoWeb")
        self.GoWeb.setGeometry(QRect(200, 250, 83, 81))

        self.retranslateUi(MainPage)
        self.exit.clicked.connect(MainPage.close)

        QMetaObject.connectSlotsByName(MainPage)
    # setupUi

    def retranslateUi(self, MainPage):
        MainPage.setWindowTitle(QCoreApplication.translate("MainPage", u"\u7535\u6559\u59d4\u5de5\u5177\u7bb1", None))
        self.icon.setText("")
        self.title.setText(QCoreApplication.translate("MainPage", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700;\">\u7535\u6559\u59d4\u5de5\u5177\u7bb1</span></p></body></html>", None))
        self.settings.setText(QCoreApplication.translate("MainPage", u"\u8bbe\u7f6e", None))
        self.exit.setText(QCoreApplication.translate("MainPage", u"\u9000\u51fa", None))
        self.help.setText(QCoreApplication.translate("MainPage", u"\u5e2e\u52a9", None))
        self.OfTool.setText(QCoreApplication.translate("MainPage", u"\u4f18\u5316\u5de5\u5177", None))
        self.FixTool.setText(QCoreApplication.translate("MainPage", u"\u4fee\u590d\u5de5\u5177", None))
        self.PtTool.setText(QCoreApplication.translate("MainPage", u"\u5b9e\u7528\u8f6f\u4ef6", None))
        self.MtTool.setText(QCoreApplication.translate("MainPage", u"\u7ef4\u62a4\u6587\u4ef6", None))
        self.EMGTool.setText(QCoreApplication.translate("MainPage", u"\u7d27\u6025\u5de5\u5177", None))
        self.GoWeb.setText(QCoreApplication.translate("MainPage", u"\u524d\u5f80\u767d\u677f\u5b98\u7f51", None))
    # retranslateUi

