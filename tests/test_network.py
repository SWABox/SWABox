"""
网络状态检测模块单元测试
"""
import pytest
from unittest.mock import patch, MagicMock
import socket
import subprocess
from lib.package.WifiDet import NetworkStatus


class TestNetworkStatus:
    """网络状态检测类测试"""

    def test_init(self):
        """测试初始化"""
        network = NetworkStatus()
        assert len(network.dns_servers) == 6
        assert len(network.ping_dns_servers) == 3
        assert network.dns_port == 53
        assert network.socket_timeout == 0.3
        assert network.ping_timeout == 300

    @patch('lib.package.WifiDet.socket.socket')
    def test_check_socket_success(self, mock_socket):
        """测试socket连接成功"""
        mock_sock = MagicMock()
        mock_socket.return_value = mock_sock

        network = NetworkStatus()
        result = network._check_socket("8.8.8.8")

        assert result is True
        mock_sock.connect.assert_called_once_with(("8.8.8.8", 53))
        mock_sock.close.assert_called_once()

    @patch('lib.package.WifiDet.socket.socket')
    def test_check_socket_failure(self, mock_socket):
        """测试socket连接失败"""
        mock_socket.side_effect = Exception("Connection failed")

        network = NetworkStatus()
        result = network._check_socket("8.8.8.8")

        assert result is False

    @patch('lib.package.WifiDet.subprocess.run')
    def test_check_ping_success(self, mock_run):
        """测试ping成功"""
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_run.return_value = mock_result

        network = NetworkStatus()
        result = network._check_ping("8.8.8.8")

        assert result is True
        mock_run.assert_called_once()

    @patch('lib.package.WifiDet.subprocess.run')
    def test_check_ping_failure(self, mock_run):
        """测试ping失败"""
        mock_result = MagicMock()
        mock_result.returncode = 1
        mock_run.return_value = mock_result

        network = NetworkStatus()
        result = network._check_ping("8.8.8.8")

        assert result is False

    def test_parallel_check_any_true(self):
        """测试并行检测 - 任一命中即返回 True"""
        network = NetworkStatus()

        def checker(ip):
            return ip == "8.8.8.8"

        result = network._parallel_check(network.dns_servers, checker)
        assert result is True

    def test_parallel_check_all_false(self):
        """测试并行检测 - 全部失败返回 False"""
        network = NetworkStatus()

        def checker(ip):
            return False

        result = network._parallel_check(network.dns_servers, checker)
        assert result is False

    @patch.object(NetworkStatus, '_check_socket')
    def test_is_internet_connected_true(self, mock_check_socket):
        """测试网络连接成功（并行 socket 命中）"""
        mock_check_socket.return_value = True

        network = NetworkStatus()
        result = network.is_internet_connected()

        assert result is True

    @patch.object(NetworkStatus, '_check_ping')
    @patch.object(NetworkStatus, '_check_socket')
    def test_is_internet_connected_false(self, mock_check_socket, mock_check_ping):
        """测试网络连接失败（socket + ping 均失败）"""
        mock_check_socket.return_value = False
        mock_check_ping.return_value = False

        network = NetworkStatus()
        result = network.is_internet_connected()

        assert result is False

    @patch.object(NetworkStatus, '_check_ping')
    @patch.object(NetworkStatus, '_check_socket')
    def test_is_internet_connected_ping_fallback(self, mock_check_socket, mock_check_ping):
        """测试 socket 全部失败后降级为 ping"""
        mock_check_socket.return_value = False
        mock_check_ping.return_value = True

        network = NetworkStatus()
        result = network.is_internet_connected()

        assert result is True
        mock_check_ping.assert_called()

    @patch('lib.package.WifiDet.subprocess.run')
    def test_get_connection_type_wifi(self, mock_run):
        """测试获取WiFi连接类型"""
        mock_result = MagicMock()
        mock_result.stdout = "Wi-Fi    已连接    专用"
        mock_run.return_value = mock_result

        network = NetworkStatus()
        conn_type, wifi_name = network.get_connection_type()

        assert conn_type == "WiFi"

    @patch('lib.package.WifiDet.subprocess.run')
    def test_get_connection_type_ethernet(self, mock_run):
        """测试获取以太网连接类型"""
        mock_result = MagicMock()
        mock_result.stdout = "Ethernet    已连接    专用"
        mock_run.return_value = mock_result

        network = NetworkStatus()
        conn_type, wifi_name = network.get_connection_type()

        assert conn_type == "Ethernet"

    @patch('lib.package.WifiDet.subprocess.run')
    def test_get_connection_type_disconnected(self, mock_run):
        """测试获取断开连接状态"""
        mock_result = MagicMock()
        mock_result.stdout = "No connection"
        mock_run.return_value = mock_result

        network = NetworkStatus()
        conn_type, wifi_name = network.get_connection_type()

        assert conn_type == "Disconnected"

    @patch('lib.package.WifiDet.subprocess.run')
    def test_get_wifi_name(self, mock_run):
        """测试获取WiFi名称"""
        mock_result = MagicMock()
        mock_result.stdout = "SSID : TestWiFi\nBSSID : 00:11:22:33:44:55"
        mock_run.return_value = mock_result

        network = NetworkStatus()
        wifi_name = network._get_wifi_name()

        assert wifi_name == "TestWiFi"