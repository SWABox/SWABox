"""
测试配置文件
"""
import os
import sys
import pytest

# 添加项目根目录到Python路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# PySide6相关配置
os.environ['QT_QPA_PLATFORM'] = 'offscreen'

# 测试数据目录
TEST_DATA_DIR = os.path.join(project_root, 'tests', 'test_data')
os.makedirs(TEST_DATA_DIR, exist_ok=True)

@pytest.fixture
def test_data_dir():
    """提供测试数据目录路径"""
    return TEST_DATA_DIR

@pytest.fixture
def project_root_dir():
    """提供项目根目录路径"""
    return project_root

@pytest.fixture
def mock_config_file(tmp_path):
    """创建临时配置文件"""
    config_file = tmp_path / "config.ini"
    config_file.write_text("[General]\nconsent_accepted=true\n")
    return str(config_file)

@pytest.fixture
def sample_network_config():
    """提供示例网络配置"""
    return {
        "dns_servers": ["8.8.8.8", "8.8.4.4"],
        "dns_port": 53,
        "socket_timeout": 2,
        "ping_timeout": 1000
    }