# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SittingsFCFptv.ui'
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
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QLabel,
    QLineEdit, QSizePolicy, QTabWidget, QToolButton, QWidget)
from . import main_rc


class Ui_settings(object):
    def setupUi(self, settings):
        if not settings.objectName():
            settings.setObjectName(u"settings")
        settings.resize(424, 295)
        icon = QIcon()
        icon.addFile(u":/logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        settings.setWindowIcon(icon)
        self.tabWidget = QTabWidget(settings)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 421, 291))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.Foundation = QWidget()
        self.Foundation.setObjectName(u"Foundation")
        self.label_8 = QLabel(self.Foundation)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 10, 161, 41))
        self.lineEdit = QLineEdit(self.Foundation)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(180, 21, 181, 25))
        self.toolButton = QToolButton(self.Foundation)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(370, 20, 31, 27))
        self.tabWidget.addTab(self.Foundation, "")
        self.Personalized = QWidget()
        self.Personalized.setObjectName(u"Personalized")
        self.tabWidget.addTab(self.Personalized, "")
        self.About = QWidget()
        self.About.setObjectName(u"About")
        self.label = QLabel(self.About)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 131, 41))
        self.label_2 = QLabel(self.About)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 20, 241, 41))
        self.label_3 = QLabel(self.About)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 60, 131, 41))
        self.label_4 = QLabel(self.About)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(160, 60, 241, 41))
        self.label_5 = QLabel(self.About)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 200, 131, 41))
        self.GoIssue = QCommandLinkButton(self.About)
        self.GoIssue.setObjectName(u"GoIssue")
        self.GoIssue.setGeometry(QRect(170, 200, 181, 41))
        self.label_6 = QLabel(self.About)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(160, 100, 241, 41))
        self.label_7 = QLabel(self.About)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 100, 131, 41))
        self.tabWidget.addTab(self.About, "")

        self.retranslateUi(settings)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(settings)
    # setupUi

    def retranslateUi(self, settings):
        settings.setWindowTitle(QCoreApplication.translate("settings", u"\u8bbe\u7f6e", None))
        self.label_8.setText(QCoreApplication.translate("settings", u"<html><head/><body><p><span style=\" font-size:16pt;\">Tool\u6587\u4ef6\u5939\u4f4d\u7f6e</span></p></body></html>", None))
        self.toolButton.setText(QCoreApplication.translate("settings", u"...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Foundation), QCoreApplication.translate("settings", u"\u57fa\u7840", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Personalized), QCoreApplication.translate("settings", u"\u4e2a\u6027\u5316", None))
        self.label.setText(QCoreApplication.translate("settings", u"<html><head/><body><p align=\"right\"><span style=\" font-size:16pt; font-weight:700;\">\u9879\u76ee\u53d1\u8d77\u4eba\uff1a</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("settings", u"<html><head/><body><p><span style=\" font-size:16pt;\">A.R.O.N.A (liyunhan177)</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("settings", u"<html><head/><body><p align=\"right\"><span style=\" font-size:16pt; font-weight:700;\">\u9879\u76ee\u540d\u79f0\uff1a</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("settings", u"<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">SWABox</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("settings", u"<html><head/><body><p align=\"right\"><span style=\" font-size:14pt;\">\u53d1\u73b0\u4e86Bug\uff1f</span></p></body></html>", None))
        self.GoIssue.setText(QCoreApplication.translate("settings", u"\u524d\u5f80\u63d0\u4ea4Issue", None))
        self.label_6.setText(QCoreApplication.translate("settings", u"<html><head/><body><p><span style=\" font-size:16pt;\">PySide6</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("settings", u"<html><head/><body><p align=\"right\"><span style=\" font-size:16pt; font-weight:700;\">UI\u5e93\uff1a</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.About), QCoreApplication.translate("settings", u"\u5173\u4e8e", None))
    # retranslateUi