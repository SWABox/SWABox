"""
主程序集成测试
"""
import pytest
import os
import sys
from unittest.mock import patch, MagicMock
from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtCore import QSettings
from lib.app import MainWindow, ConsentDialog


@pytest.fixture
def qapp():
    """创建QApplication实例"""
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    yield app
    app.quit()


class TestMainWindow:
    """主窗口集成测试"""

    @pytest.mark.gui
    def test_main_window_creation(self, qapp):
        """测试主窗口创建"""
        window = MainWindow()
        assert window is not None
        assert window.windowTitle() != ""
        window.close()

    @pytest.mark.gui
    def test_settings_button_click(self, qapp):
        """测试设置按钮点击"""
        window = MainWindow()
        window.settings.click()
        
        assert window.settings_dialog is not None
        assert window.settings_dialog.isVisible()
        
        window.settings_dialog.close()
        window.close()

    @pytest.mark.gui
    def test_emg_tool_button_click(self, qapp):
        """测试EMG工具按钮点击"""
        window = MainWindow()
        window.EMGTool.click()
        
        assert window.EMG_dialog is not None
        assert window.EMG_dialog.isVisible()
        
        window.EMG_dialog.close()
        window.close()

    @pytest.mark.gui
    @patch('lib.app.web.open')
    def test_go_ossier_button_click(self, mock_web_open, qapp):
        """测试跳转到GitHub Issues"""
        window = MainWindow()
        window.settings.click()
        
        window.settings_ui.GoIssue.click()
        
        mock_web_open.assert_called_once_with("https://github.com/liyunhan177/SWABox/issues/new")
        
        window.settings_dialog.close()
        window.close()

    @pytest.mark.gui
    @patch('lib.app.OpenExplorer.open_tool_folder')
    def test_go_explorer_button_click(self, mock_open_tool, qapp):
        """测试打开工具文件夹"""
        window = MainWindow()
        window.EMGTool.click()
        
        window.EMG_ui.GoExplorer.click()
        
        mock_open_tool.assert_called_once()
        
        window.EMG_dialog.close()
        window.close()


class TestConsentDialog:
    """用户协议对话框测试"""

    @pytest.mark.gui
    def test_consent_dialog_creation(self, qapp):
        """测试用户协议对话框创建"""
        dialog = ConsentDialog()
        assert dialog is not None
        assert dialog.ui.Yes is not None
        assert dialog.ui.No is not None
        dialog.close()

    @pytest.mark.gui
    def test_consent_dialog_accept(self, qapp):
        """测试接受用户协议"""
        dialog = ConsentDialog()
        dialog.ui.Yes.click()
        
        assert dialog.result() == 1  # QDialog.DialogCode.Accepted

    @pytest.mark.gui
    def test_consent_dialog_reject(self, qapp):
        """测试拒绝用户协议"""
        dialog = ConsentDialog()
        dialog.ui.No.click()

        assert dialog.result() == QDialog.DialogCode.Rejected


class TestConfiguration:
    """配置管理测试"""

    @pytest.mark.integration
    def test_config_file_creation(self, tmp_path):
        """测试配置文件创建"""
        config_dir = tmp_path / "data"
        config_dir.mkdir(exist_ok=True)
        config_file = config_dir / "config.ini"
        
        settings = QSettings(str(config_file), QSettings.Format.IniFormat)
        settings.setValue("consent_accepted", True)
        settings.sync()
        
        assert config_file.exists()
        
        verify_settings = QSettings(str(config_file), QSettings.Format.IniFormat)
        assert verify_settings.value("consent_accepted", False, type=bool) is True

    @pytest.mark.integration
    def test_config_file_default_value(self, tmp_path):
        """测试配置文件默认值"""
        config_file = tmp_path / "config.ini"
        
        settings = QSettings(str(config_file), QSettings.Format.IniFormat)
        consent_accepted = settings.value("consent_accepted", False, type=bool)
        
        assert consent_accepted is False

    @pytest.mark.integration
    def test_config_directory_creation(self, tmp_path):
        """测试配置目录创建"""
        config_dir = tmp_path / "data"
        os.makedirs(config_dir, exist_ok=True)
        
        assert config_dir.exists()
        assert config_dir.is_dir()