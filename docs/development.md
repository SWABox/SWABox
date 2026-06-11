# 项目开发文档

## 本地跑起来

### Windows（完整验证）

```bash
git clone https://github.com/SWABox/SWABox.git
cd SWABox
python -m venv venv
venv\Scripts\activate
pip install -r config/requirements.txt
pip install -r config/requirements-test.txt  # 安装测试依赖
python main.py
```

推荐在 PowerShell 中执行，避免 CMD 可能出现的编码问题。

### Mac / Linux（社区测试中）

```bash
git clone https://github.com/SWABox/SWABox.git
cd SWABox
python3 -m venv venv
source venv/bin/activate
pip install -r config/requirements.txt
pip install -r config/requirements-test.txt  # 安装测试依赖
python main.py
```

这两个平台尚未经过全面测试，可能会遇到界面渲染或依赖缺失的问题。非常鼓励你尝试并贡献修复，相关问题请先查阅现有 issue，然后提出你的发现。

### 运行测试

```bash
# 运行所有测试
pytest

# 运行特定类型测试
pytest -m unit           # 单元测试
pytest -m integration    # 集成测试
pytest -m gui            # GUI测试
pytest -m network        # 网络测试

# 生成覆盖率报告
pytest --cov=lib --cov-report=html

# 使用测试脚本
python run_tests.py      # Python脚本
run_tests.bat            # Windows批处理
```

详细测试说明请查看 [TESTING_GUIDE.md](../TESTING_GUIDE.md)。

## 目录结构

- `lib/page/` 存放界面文件，包括 MainPage、Settings、EMGToolPage 等
- `lib/package/` 是业务逻辑，包含网络检测、文件操作等工具类
- `res/UI/` 存放 Qt Designer 设计的 .ui 文件
- `res/img/` 是图标和图片
- `Tool/` 存放内置的第三方工具，如 360 急救箱、DirectX 修复工具等
- `Static/` 存放静态资源文件
- `data/` 存放数据文件，目前主要是 data.json 和 config.ini
- `tests/` 存放自动化测试文件，包括单元测试、集成测试等
- `config/` 存放项目配置文件，包括 pyproject.toml、pytest.ini、requirements.txt、SWABox.spec 等
- `scripts/` 存放脚本文件，包括测试运行脚本 run_tests.py 和 run_tests.bat
- `docs/` 存放项目文档

## 当年为什么这么写

### 为什么选择 PySide6 而不是 tkinter 或 PyQt5？

PySide6太美观了！之前用过tkinter写一个简单的工具，但是界面很丑，所以选择这次使用了 PySide6。
PySide6 是 Qt6 的官方 Python 绑定，比 PyQt5 更新及时，许可证也更友好（LGPL vs GPL）。

### 为什么把紧急工具放在 Tool 目录而不是在线下载？

将常用工具（如 360 急救箱、DirectX 修复工具）内置在程序中，可以在紧急情况下直接使用，不依赖网络连接。这也是为什么程序启动时会检测网络状态，如果无网络则提示用户只能使用本地功能。

## 调试技巧

程序启动时会检测网络状态，如果检测失败会弹出提示框。调试时可以注释掉 `main.py` 中的网络检测部分，直接进入主界面。

如果遇到界面显示问题，可以检查 `lib/page/` 下的 Python 文件是否正确加载了对应的 .ui 文件。PySide6 使用 `QUiLoader` 或 `uic.loadUi` 来加载界面文件，确保 .ui 文件路径正确。

打包后的程序如果出现问题，可以查看 `dist/SWABox-b0.3.0/_internal/` 目录下的文件结构，确认所有依赖和资源文件是否正确包含。

## 打包发布

运行 `pyinstaller config/SWABox.spec` 会在 `dist/` 下生成 Windows 安装包。Mac/Linux 的打包暂未配置，欢迎贡献。

打包配置在 `config/SWABox.spec` 中，主要指定了入口文件 `main.py`、需要包含的数据目录 `Tool`、`Static` 和 `config`，以及隐藏导入的模块 `lib.package.OpenExplorer` 和 `lib.package.WifiDet`。如果添加了新的模块，记得更新 `hiddenimports` 列表。