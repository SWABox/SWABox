# 贡献指南

## 如何提交 Issue

### Bug 报告模板

- 操作系统及版本：如 Windows 11 22H2
- 复现步骤：详细描述如何触发问题
- 期望行为：你期望发生什么
- 实际行为：实际发生了什么
- 截图或日志附件：如果有错误信息，请附上截图或日志文件

### 功能建议模板

- 功能描述：你希望添加什么功能
- 使用场景：这个功能在什么情况下使用
- 实现建议：如果你有实现思路，可以简单描述

## 如何提 PR

### 分支命名习惯

- `feature/xxx`：新功能
- `fix/xxx`：bug 修复
- `docs/xxx`：文档更新
- `refactor/xxx`：代码重构
- `test/xxx`：测试相关

### Commit message 格式

- `feat: xxx`：新功能
- `fix: xxx`：bug 修复
- `docs: xxx`：文档更新
- `style: xxx`：代码格式调整
- `refactor: xxx`：代码重构
- `test: xxx`：测试相关
- `chore: xxx`：构建过程或辅助工具的变动

示例：
```
feat: 添加新的工具页面
fix: 修复网络检测在防火墙环境下失败的问题
docs: 更新用户手册中的安装说明
test: 添加网络检测模块的单元测试
```

### 提 PR 前的检查清单

在提交 PR 之前，请确保完成以下检查：

#### 代码质量
- [ ] 代码遵循项目现有风格
- [ ] 添加了必要的注释和文档字符串
- [ ] 没有引入明显的性能问题
- [ ] 没有硬编码的路径或配置

#### 测试要求
- [ ] 运行所有测试：`pytest` 确保所有现有测试通过
- [ ] 为新功能编写测试：在 `tests/` 目录下添加相应的测试文件
- [ ] 检查测试覆盖率：`pytest --cov=lib --cov-report=html` 确保覆盖率不会显著下降
- [ ] 手动验证GUI功能：对于界面相关的改动，手动验证界面显示和交互

#### 文档更新
- [ ] 更新了相关的文档（如需要）
- [ ] 添加了必要的注释说明
- [ ] 更新了 README 或用户手册（如涉及用户可见的功能）

#### 跨平台兼容性
- [ ] 在 Windows 上测试通过
- [ ] 如涉及跨平台功能，在 Mac/Linux 上验证（如无相应设备，请在 PR 中说明）

### 测试编写指南

#### 测试文件位置
- 单元测试：`tests/test_*.py`
- 集成测试：`tests/test_integration.py`
- 功能测试：按模块分类，如 `tests/test_network.py`

#### 测试标记使用
```python
import pytest

@pytest.mark.unit
def test_example():
    """单元测试"""
    pass

@pytest.mark.integration
def test_integration_example():
    """集成测试"""
    pass

@pytest.mark.gui
def test_gui_example():
    """GUI测试"""
    pass

@pytest.mark.network
def test_network_example():
    """网络测试"""
    pass
```

#### 测试覆盖率目标
- 整体覆盖率目标：> 80%
- 核心模块覆盖率目标：> 90%
- UI模块覆盖率目标：> 70%

详细测试说明请查看 [TESTING_GUIDE.md](../TESTING_GUIDE.md)。

## 代码风格

代码风格参考现有项目即可，核心是：
- 缩进用空格（4 个空格）
- 变量名有实际意义，避免使用 `a`、`b`、`tmp` 这样的无意义名称
- 函数和类名遵循常见 Python 惯例（类名用大驼峰，函数名用小写加下划线）
- 适当添加注释，解释复杂逻辑

不必过度追求完美，太放飞的部分我会在 review 时提出。

## 特别说明

目前项目以 Windows 为主要开发平台，但非常欢迎 Mac 和 Linux 用户参与测试和适配。提交 PR 时，如果涉及跨平台兼容性，请在对应平台上简要验证；若没有相应设备，可在 PR 中说明，我们将一起测试。



任何贡献都欢迎，哪怕只是修正一个拼写错误，或是在 Mac 上跑了一遍然后告诉我们"能启动"。