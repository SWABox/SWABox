# 开发者指南

## 核心流程走读

```python
# main.py 中的典型交互流程
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
```

这个流程展示了用户点击按钮到打开新界面的完整过程：
1. 用户点击按钮触发信号
2. 创建新的 QDialog 实例
3. 加载对应的 UI 文件
4. 连接按钮信号到槽函数
5. 显示对话框

**扩展点**：如需添加新功能，可以在 `lib/page/` 下创建新的页面类，然后在 `main.py` 中添加对应的按钮点击事件处理函数。

## 如何添加一个新的界面模块

最快实现方式：
1. 使用 Qt Designer 创建新的 .ui 文件，保存到 `res/UI/` 目录
2. 使用 `pyside6-uic res/UI/YourPage.ui -o lib/page/YourPage.py` 生成对应的 Python 文件
3. 在 `lib/page/__init__.py` 中添加导入：`from .YourPage import *`
4. 在 `main.py` 的 MainWindow 类中添加按钮点击事件处理函数
5. 在处理函数中创建并显示新界面

可以先实现功能，后续再优化结构。

## 测试如何运行

项目已配置完整的 pytest 自动化测试框架，包含单元测试、集成测试和 GUI 测试。

### 安装测试依赖

```bash
pip install -r requirements-test.txt
```

### 运行测试

#### 运行所有测试
```bash
pytest
# 或
python -m pytest
# 或
python run_tests.py
# 或
run_tests.bat  # Windows
```

#### 运行特定类型的测试
```bash
# 只运行单元测试
pytest -m unit

# 只运行集成测试
pytest -m integration

# 只运行GUI测试
pytest -m gui

# 只运行网络测试
pytest -m network
```

#### 生成覆盖率报告
```bash
pytest --cov=lib --cov-report=html
# 然后打开 htmlcov/index.html 查看报告
```

#### 运行特定测试
```bash
# 运行特定测试文件
pytest tests/test_network.py

# 运行特定测试类
pytest tests/test_network.py::TestNetworkStatus

# 运行特定测试方法
pytest tests/test_network.py::TestNetworkStatus::test_init
```

### 测试覆盖率目标

- **整体覆盖率**: 目标 > 80%
- **核心模块覆盖率**: 目标 > 90%
- **UI模块覆盖率**: 目标 > 70%

### 编写测试

#### 测试文件命名规范
- 测试文件名：`test_*.py`
- 测试类名：`Test*`
- 测试函数名：`test_*`

#### 测试示例
```python
import pytest
from unittest.mock import patch, MagicMock

class TestExample:
    def test_basic_functionality(self):
        """基本功能测试"""
        assert 1 + 1 == 2

    @pytest.mark.unit
    def test_with_mock(self):
        """使用mock的测试"""
        with patch('lib.package.WifiDet.socket.socket') as mock_socket:
            mock_sock = MagicMock()
            mock_socket.return_value = mock_sock
            # 测试代码
            pass
```

详细的使用说明请查看 [TESTING_GUIDE.md](../TESTING_GUIDE.md)。

### 提 PR 前的测试要求

1. **运行所有测试**: 确保所有现有测试通过
2. **为新功能编写测试**: 为新增的功能编写相应的测试用例
3. **检查覆盖率**: 确保代码覆盖率不会显著下降
4. **手动验证**: 对于GUI相关功能，仍需手动验证界面显示和交互

### 测试框架特性

- **完整的测试分类**: 单元测试、集成测试、GUI测试、网络测试
- **丰富的测试插件**: pytest-cov、pytest-qt、pytest-mock等
- **代码覆盖率分析**: 支持HTML、命令行、XML多种报告格式
- **跨平台支持**: 支持Windows、Mac、Linux平台测试

## 高危区域

`lib/package/WifiDet.py` 涉及网络检测逻辑，不兼容的改动可能导致程序启动时误判网络状态，影响用户使用体验。如需修改网络检测逻辑，请先讨论方案。

`config/SWABox.spec` 是打包配置文件，错误的修改可能导致打包失败或打包后的程序缺少关键文件。修改前请备份原文件，并在多个 Windows 版本上测试打包结果。

`Tool/` 目录下的工具文件是第三方工具，不要随意修改或删除，这些工具在紧急情况下可能救命。如果需要更新工具，请在 issue 中说明原因和替换方案。