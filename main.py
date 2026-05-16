from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtCore import Qt
import webbrowser as web
from lib.page import *
from lib.package import *
import sys

class MainWindow(QMainWindow, MainPage.Ui_MainPage):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.settings.clicked.connect(self.SettingsBtnClicked)
        self.EMGTool.clicked.connect(self.EMGToolBtnClicked)

    def SettingsBtnClicked(self):
        self.settings_dialog = QDialog()
        self.settings_ui = Settings.Ui_settings()
        self.settings_ui.setupUi(self.settings_dialog)
        self.settings_ui.GoIssue.clicked.connect(self.GoOssierBtnClicked)
        self.settings_dialog.show()

    def EMGToolBtnClicked(self):
        self.EMG_dialog = QDialog()
        self.EMG_ui = EMGToolPage.Ui_EMGToolPage()
        self.EMG_ui.setupUi(self.EMG_dialog)
        self.EMG_ui.GoExplorer.clicked.connect(self.GoExplorBtnClicked)
        self.EMG_dialog.show()

    def GoExplorBtnClicked(self):
        OpenExplorer.open_tool_folder()

    def GoOssierBtnClicked(self):
        web.open("https://github.com/liyunhan177/SWABox/issues/new")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
