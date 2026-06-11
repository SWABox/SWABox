"""
文件操作模块单元测试
"""
import pytest
import os
import sys
from unittest.mock import patch, MagicMock
from lib.package.OpenExplorer import get_base_path, open_tool_folder


class TestGetBasePath:
    """获取基础路径测试"""

    @patch('lib.package.OpenExplorer.sys')
    def test_get_base_path_frozen(self, mock_sys):
        """测试打包后的路径获取"""
        mock_sys.frozen = True
        mock_sys._MEIPASS = "/tmp/extracted"
        
        result = get_base_path()
        
        assert result == "/tmp/extracted"

    @patch('lib.package.OpenExplorer.sys')
    def test_get_base_path_frozen_no_meipass(self, mock_sys):
        """测试打包后无MEIPASS的路径获取"""
        mock_sys.frozen = True
        mock_sys.executable = "/path/to/app.exe"
        del mock_sys._MEIPASS
        
        result = get_base_path()
        
        assert result == "/path/to"

    @patch('lib.package.OpenExplorer.sys')
    def test_get_base_path_development(self, mock_sys):
        """测试开发环境路径获取"""
        mock_sys.frozen = False
        
        result = get_base_path()
        
        assert "SWABox" in result


class TestOpenToolFolder:
    """打开工具文件夹测试"""

    @patch('lib.package.OpenExplorer.get_base_path')
    @patch('lib.package.OpenExplorer.os.path.exists')
    @patch('lib.package.OpenExplorer.os.startfile')
    @patch('lib.package.OpenExplorer.sys.platform', 'win32')
    def test_open_tool_folder_windows_success(self, mock_startfile, mock_exists, mock_get_base):
        """测试Windows系统成功打开工具文件夹"""
        mock_get_base.return_value = "/project/root"
        mock_exists.return_value = True
        
        result = open_tool_folder()
        
        assert result is True
        mock_startfile.assert_called_once()
        call_args = mock_startfile.call_args[0][0]
        assert "Tool" in call_args

    @patch('lib.package.OpenExplorer.get_base_path')
    @patch('lib.package.OpenExplorer.os.path.exists')
    @patch('lib.package.OpenExplorer.os.startfile')
    @patch('lib.package.OpenExplorer.sys.platform', 'win32')
    def test_open_tool_folder_windows_not_exists(self, mock_startfile, mock_exists, mock_get_base):
        """测试Windows系统工具文件夹不存在"""
        mock_get_base.return_value = "/project/root"
        mock_exists.side_effect = [False, False]
        
        result = open_tool_folder()
        
        assert result is False
        mock_startfile.assert_not_called()

    @patch('lib.package.OpenExplorer.get_base_path')
    @patch('lib.package.OpenExplorer.os.path.exists')
    @patch('lib.package.OpenExplorer.subprocess.Popen')
    @patch('lib.package.OpenExplorer.sys.platform', 'darwin')
    def test_open_tool_folder_macos(self, mock_popen, mock_exists, mock_get_base):
        """测试macOS系统打开工具文件夹"""
        mock_get_base.return_value = "/project/root"
        mock_exists.return_value = True
        
        result = open_tool_folder()
        
        assert result is True
        mock_popen.assert_called_once()
        call_args = mock_popen.call_args[0][0]
        assert call_args[0] == 'open'
        assert "Tool" in call_args[1]

    @patch('lib.package.OpenExplorer.get_base_path')
    @patch('lib.package.OpenExplorer.os.path.exists')
    @patch('lib.package.OpenExplorer.subprocess.Popen')
    @patch('lib.package.OpenExplorer.sys.platform', 'linux')
    def test_open_tool_folder_linux(self, mock_popen, mock_exists, mock_get_base):
        """测试Linux系统打开工具文件夹"""
        mock_get_base.return_value = "/project/root"
        mock_exists.return_value = True
        
        result = open_tool_folder()
        
        assert result is True
        mock_popen.assert_called_once()
        call_args = mock_popen.call_args[0][0]
        assert call_args[0] == 'xdg-open'
        assert "Tool" in call_args[1]

    @patch('lib.package.OpenExplorer.get_base_path')
    @patch('lib.package.OpenExplorer.os.path.exists')
    @patch('lib.package.OpenExplorer.os.startfile')
    @patch('lib.package.OpenExplorer.sys.platform', 'win32')
    def test_open_tool_folder_exception(self, mock_startfile, mock_exists, mock_get_base):
        """测试打开工具文件夹异常处理"""
        mock_get_base.return_value = "/project/root"
        mock_exists.return_value = True
        mock_startfile.side_effect = Exception("Access denied")
        
        result = open_tool_folder()
        
        assert result is False

    @patch('lib.package.OpenExplorer.get_base_path')
    @patch('lib.package.OpenExplorer.os.path.exists')
    @patch('lib.package.OpenExplorer.os.startfile')
    @patch('lib.package.OpenExplorer.sys.executable', '/path/to/app.exe')
    @patch('lib.package.OpenExplorer.sys.platform', 'win32')
    def test_open_tool_folder_alternative_path(self, mock_startfile, mock_exists, mock_get_base):
        """测试使用备选路径打开工具文件夹"""
        mock_get_base.return_value = "/project/root"
        mock_exists.side_effect = [False, True]
        
        result = open_tool_folder()
        
        assert result is True
        mock_startfile.assert_called_once()
        call_args = mock_startfile.call_args[0][0]
        assert "Tool" in call_args