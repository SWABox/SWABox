"""
测试示例文件
演示如何为SWABox项目编写测试
"""
import pytest
from unittest.mock import patch, MagicMock


class TestExample:
    """示例测试类"""
    
    def test_basic_assertion(self):
        """基本断言测试"""
        assert 1 + 1 == 2
        assert "hello" in "hello world"
        
    @pytest.mark.unit
    def test_with_fixture(self, sample_network_config):
        """使用fixture的测试"""
        assert "dns_servers" in sample_network_config
        assert len(sample_network_config["dns_servers"]) > 0
        
    @patch('lib.package.WifiDet.socket.socket')
    def test_with_mock(self, mock_socket):
        """使用mock的测试"""
        mock_sock = MagicMock()
        mock_socket.return_value = mock_sock
        
        # 模拟socket连接
        mock_sock.connect.return_value = None
        
        # 测试代码
        mock_sock.connect(("8.8.8.8", 53))
        
        # 验证调用
        mock_sock.connect.assert_called_once_with(("8.8.8.8", 53))
        
    def test_exception_handling(self):
        """异常处理测试"""
        with pytest.raises(ValueError):
            raise ValueError("Test exception")
            
    @pytest.mark.parametrize("input_val,expected", [
        (1, 2),
        (2, 4),
        (3, 6),
    ])
    def test_parameterized(self, input_val, expected):
        """参数化测试"""
        assert input_val * 2 == expected
        
    @pytest.mark.skip(reason="演示跳过测试")
    def test_skipped(self):
        """被跳过的测试"""
        assert False
        
    @pytest.mark.xfail
    def test_expected_failure(self):
        """预期失败的测试"""
        assert False


def test_function_level():
    """函数级别的测试"""
    assert True


@pytest.fixture
def custom_fixture():
    """自定义fixture"""
    data = {"key": "value"}
    yield data
    # 清理代码


def test_with_custom_fixture(custom_fixture):
    """使用自定义fixture的测试"""
    assert custom_fixture["key"] == "value"


class TestEdgeCases:
    """边界条件测试类"""
    
    def test_empty_string(self):
        """空字符串测试"""
        assert "" == ""
        
    def test_none_value(self):
        """None值测试"""
        assert None is None
        
    def test_zero_value(self):
        """零值测试"""
        assert 0 == 0
        assert 0.0 == 0.0


if __name__ == "__main__":
    # 可以直接运行此文件进行测试
    pytest.main([__file__, "-v"])