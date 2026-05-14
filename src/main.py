from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtCore import Qt
from lib.page import *
import sys

class MainWindow(QMainWindow, MainPage.Ui_MainPage):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.settings.clicked.connect(self.SettingsBtnClicked)

    def SettingsBtnClicked(self):
        self.settings_dialog = QDialog()
        self.settings_ui = Settings.Ui_settings()
        self.settings_ui.setupUi(self.settings_dialog)
        self.settings_dialog.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())