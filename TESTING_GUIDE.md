# SWABox 自动化测试框架使用说明

## 概述

本项目已配置完整的pytest自动化测试框架，包含单元测试、集成测试和GUI测试。测试框架支持代码覆盖率分析、HTML报告生成等功能。

## 测试框架结构

```
SWABox/
├── tests/                          # 测试目录
│   ├── __init__.py                # 测试包初始化
│   ├── conftest.py                # pytest配置和fixtures
│   ├── test_network.py            # 网络检测模块测试
│   ├── test_file_operations.py    # 文件操作模块测试
│   ├── test_integration.py        # 集成测试
│   └── test_data/                 # 测试数据目录
│       ├── __init__.py
│       └── sample_config.ini      # 示例配置文件
├── pytest.ini                     # pytest配置文件
├── pyproject.toml                 # 项目配置（包含pytest配置）
├── requirements-test.txt          # 测试依赖包
└── run_tests.py                   # 测试运行脚本
```

## 安装测试依赖

### 方法1：安装所有测试依赖
```bash
pip install -r requirements-test.txt
```

### 方法2：单独安装pytest插件
```bash
pip install pytest-cov pytest-qt pytest-mock pytest-timeout pytest-html pytest-json-report
```

## 测试分类

项目测试分为以下几类：

- **单元测试 (unit)**: 测试单个函数和类的功能
- **集成测试 (integration)**: 测试模块间的交互
- **GUI测试 (gui)**: 测试图形用户界面相关功能
- **网络测试 (network)**: 测试网络相关功能

## 运行测试

### 基本测试命令

#### 1. 运行所有测试
```bash
pytest
# 或
python -m pytest
```

#### 2. 运行特定测试文件
```bash
pytest tests/test_network.py
```

#### 3. 运行特定测试类
```bash
pytest tests/test_network.py::TestNetworkStatus
```

#### 4. 运行特定测试方法
```bash
pytest tests/test_network.py::TestNetworkStatus::test_init
```

#### 5. 使用测试运行脚本
```bash
python run_tests.py              # 运行所有测试
python run_tests.py unit         # 只运行单元测试
python run_tests.py integration  # 只运行集成测试
python run_tests.py gui          # 只运行GUI测试
python run_tests.py network      # 只运行网络测试
python run_tests.py coverage     # 生成覆盖率报告
python run_tests.py fast         # 快速测试（遇到失败立即停止）
```

### 高级测试选项

#### 1. 显示详细输出
```bash
pytest -v
```

#### 2. 显示测试进度
```bash
pytest -v -s
```

#### 3. 运行特定标记的测试
```bash
pytest -m unit              # 只运行单元测试
pytest -m integration       # 只运行集成测试
pytest -m gui               # 只运行GUI测试
pytest -m network           # 只运行网络测试
```

#### 4. 生成覆盖率报告
```bash
pytest --cov=lib --cov-report=html
```
生成的HTML报告位于 `htmlcov/index.html`

#### 5. 生成HTML测试报告
```bash
pytest --html=report.html
```

#### 6. 生成JSON测试报告
```bash
pytest --json-report --json-report-file=test_report.json
```

#### 7. 并行运行测试（需要pytest-xdist）
```bash
pytest -n auto
```

#### 8. 超时设置（需要pytest-timeout）
```bash
pytest --timeout=10
```

## 测试配置

### pytest.ini 配置说明

```ini
[pytest]
testpaths = tests                    # 测试文件搜索路径
python_files = test_*.py            # 测试文件命名模式
python_classes = Test*              # 测试类命名模式
python_functions = test_*           # 测试函数命名模式
addopts = -v --strict-markers --tb=short --cov=lib --cov-report=html --cov-report=term-missing
markers =
    unit: Unit tests
    integration: Integration tests
    gui: GUI-related tests
    network: Network-related tests
```

### conftest.py 配置说明

`tests/conftest.py` 文件包含以下fixtures：

- `test_data_dir`: 提供测试数据目录路径
- `project_root_dir`: 提供项目根目录路径
- `mock_config_file`: 创建临时配置文件
- `sample_network_config`: 提供示例网络配置

## 编写测试

### 测试文件命名规范

- 测试文件名：`test_*.py`
- 测试类名：`Test*`
- 测试函数名：`test_*`

### 测试示例

#### 单元测试示例
```python
import pytest
from lib.package.WifiDet import NetworkStatus

class TestNetworkStatus:
    def test_init(self):
        """测试初始化"""
        network = NetworkStatus()
        assert len(network.dns_servers) > 0
        assert network.dns_port == 53

    @pytest.mark.unit
    def test_check_socket_success(self):
        """测试socket连接成功"""
        # 测试代码
        pass
```

#### 集成测试示例
```python
import pytest
from PySide6.QtWidgets import QApplication

@pytest.fixture
def qapp():
    """创建QApplication实例"""
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    yield app
    app.quit()

@pytest.mark.integration
def test_main_window_creation(qapp):
    """测试主窗口创建"""
    from main import MainWindow
    window = MainWindow()
    assert window is not None
    window.close()
```

#### 使用mock的测试示例
```python
from unittest.mock import patch, MagicMock

@patch('lib.package.WifiDet.socket.socket')
def test_check_socket_success(mock_socket):
    """测试socket连接成功"""
    mock_sock = MagicMock()
    mock_socket.return_value = mock_sock
    
    network = NetworkStatus()
    result = network._check_socket("8.8.8.8")
    
    assert result is True
    mock_sock.connect.assert_called_once_with(("8.8.8.8", 53))
```

## 测试覆盖率

### 查看覆盖率报告

#### 命令行输出
```bash
pytest --cov=lib --cov-report=term-missing
```

#### HTML报告
```bash
pytest --cov=lib --cov-report=html
```
然后在浏览器中打开 `htmlcov/index.html`

#### XML报告（用于CI/CD）
```bash
pytest --cov=lib --cov-report=xml
```

### 覆盖率目标

- **整体覆盖率**: 目标 > 80%
- **核心模块覆盖率**: 目标 > 90%
- **UI模块覆盖率**: 目标 > 70%

## 常见问题

### 1. 测试失败时如何调试？

```bash
# 显示详细错误信息
pytest -v --tb=long

# 在失败时进入调试器
pytest --pdb

# 只运行失败的测试
pytest --lf
```

### 2. 如何跳过某些测试？

```python
import pytest

@pytest.mark.skip(reason="暂时跳过此测试")
def test_example():
    pass

# 或者在命令行中跳过
pytest -m "not slow"
```

### 3. 如何处理GUI测试？

GUI测试需要设置环境变量：
```python
import os
os.environ['QT_QPA_PLATFORM'] = 'offscreen'
```

### 4. 如何处理网络测试？

网络测试应该使用mock来避免实际的网络调用：
```python
@patch('lib.package.WifiDet.subprocess.run')
def test_network_function(mock_run):
    mock_run.return_value = MagicMock(stdout="test output")
    # 测试代码
```

## CI/CD集成

### GitHub Actions 示例

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: windows-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.12'
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install -r requirements-test.txt
    - name: Run tests
      run: pytest --cov=lib --cov-report=xml
    - name: Upload coverage
      uses: codecov/codecov-action@v2
```

## 最佳实践

1. **测试命名**: 使用描述性的测试名称，清楚说明测试的内容
2. **测试独立性**: 每个测试应该独立运行，不依赖其他测试
3. **使用fixtures**: 利用pytest fixtures来管理测试数据和设置
4. **mock外部依赖**: 对于外部服务（网络、数据库等）使用mock
5. **测试边界条件**: 测试正常情况和异常情况
6. **保持测试简单**: 每个测试只测试一个功能点
7. **定期运行测试**: 在代码变更后及时运行测试
8. **维护测试**: 随着代码演进，及时更新测试

## 测试报告

测试运行后会生成以下报告：

1. **命令行报告**: 实时显示测试结果
2. **HTML覆盖率报告**: `htmlcov/index.html`
3. **HTML测试报告**: `report.html`（如果使用--html参数）
4. **JSON报告**: `test_report.json`（如果使用--json-report参数）

## 相关资源

- [pytest官方文档](https://docs.pytest.org/)
- [pytest-cov文档](https://pytest-cov.readthedocs.io/)
- [pytest-qt文档](https://pytest-qt.readthedocs.io/)
- [pytest-mock文档](https://pytest-mock.readthedocs.io/)

## 联系方式

如有问题或建议，请通过以下方式联系：

- GitHub Issues: https://github.com/liyunhan177/SWABox/issues