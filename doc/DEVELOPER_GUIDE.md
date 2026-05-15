# SWABox 开发者指南

## 快速开始

### 环境搭建

#### 1. 系统要求
- **操作系统**: Windows 10/11 （Mac OS 与 Linux未测试）
- **Python 版本**: Python 3.8+
- **必需依赖**: 
  - PySide6

#### 2. 克隆项目
```bash
git clone https://github.com/liyunhan177/SWABox.git
cd SWABox
```

#### 3. 创建虚拟环境（推荐）
```bash
# 创建虚拟环境
python -m venv .venv

# 激活虚拟环境
# Windows PowerShell
.venv\Scripts\Activate.ps1

# Windows CMD
.venv\Scripts\activate.bat
```

#### 4. 安装依赖
```bash
pip install PySide6
```

#### 5. 验证安装
```bash
python src/main.py
```

---

## 开发流程

### 添加新的工具页面

#### 步骤 1: 使用 Qt Designer 设计 UI

1. 打开 Qt Designer
2. 创建新窗口（Main Window 或 Widget）
3. 设计界面布局
4. 保存为 `.ui` 文件到 `res/UI/` 目录

#### 步骤 2: 转换为 Python 代码

```bash
# 转换 UI 文件
pyside6-uic res/UI/NewTool.ui -o lib/page/NewTool.py
```

#### 步骤 3: 在主程序中集成

编辑 `src/main.py`，添加按钮点击事件：

```python
def NewToolBtnClicked(self):
    # 创建对话框或窗口
    from PySide6.QtWidgets import QDialog
    from lib.page.NewTool import Ui_NewTool
    
    self.newtool_dialog = QDialog()
    self.newtool_ui = Ui_NewTool()
    self.newtool_ui.setupUi(self.newtool_dialog)
    self.newtool_dialog.show()
```

在 `__init__` 中连接信号：

```python
def __init__(self):
    super(MainWindow, self).__init__()
    self.setupUi(self)
    self.settings.clicked.connect(self.SettingsBtnClicked)
    self.OfTool.clicked.connect(self.OfToolBtnClicked)  # 添加新按钮
```

---

### 修改现有 UI

#### 使用 Qt Designer 编辑

1. 打开对应的 `.ui` 文件
2. 修改界面元素
3. 保存文件
4. 重新转换为 Python 代码

```bash
pyside6-uic res/UI/MainPage.ui -o lib/page/MainPage.py
```

**注意事项**:
- 修改后必须重新生成 Python 代码
- 不要手动修改生成的 Python 文件
- 所有自定义逻辑应在主程序中实现

---

## UI 定制指南

### 修改主题样式

PySide6 支持 QSS (Qt Style Sheets) 进行样式定制：

```python
# 设置全局样式
app.setStyleSheet("""
    QPushButton {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px;
    }
    QPushButton:hover {
        background-color: #45a049;
    }
    QMainWindow {
        background-color: #f0f0f0;
    }
""")
```

### 常用 QSS 选择器

```css
/* 按钮样式 */
QPushButton { }
QPushButton#settings { }  /* 特定对象 */

/* 标签样式 */
QLabel { }

/* 选项卡样式 */
QTabWidget { }
QTabBar::tab { }

/* 对话框样式 */
QDialog { }
```

### 调整布局

Qt 提供多种布局管理器：

```python
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout

# 垂直布局
layout = QVBoxLayout()
layout.addWidget(widget1)
layout.addWidget(widget2)

# 水平布局
layout = QHBoxLayout()
layout.addWidget(widget1)
layout.addWidget(widget2)

# 网格布局
layout = QGridLayout()
layout.addWidget(widget, row, column)
```

---

## 功能扩展

### 添加工具启动功能

#### 本地工具启动

```python
import subprocess
import os

def launch_tool(tool_path):
    """启动本地工具"""
    try:
        if os.path.exists(tool_path):
            subprocess.Popen([tool_path])
        else:
            print(f"工具不存在：{tool_path}")
    except Exception as e:
        print(f"启动失败：{str(e)}")

# 使用示例
def OfToolBtnClicked(self):
    tool_path = "Tool/360/360FAK/Superkiller.exe"
    launch_tool(tool_path)
```

#### 网站快捷访问

```python
import webbrowser

def open_website(url):
    """打开网站"""
    webbrowser.open(url)

# 使用示例
def HelpBtnClicked(self):
    open_website("https://www.seewo.com/")
```

### 添加日志系统

```python
import logging
import os

def setup_logger():
    """配置日志系统"""
    # 创建日志目录
    os.makedirs('log', exist_ok=True)
    
    # 配置日志
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('log/app.log', encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger('SWABox')

# 使用示例
logger = setup_logger()
logger.info("应用启动")
logger.error("发生错误")
```

---

### 添加数据库支持

```python
import sqlite3
import os

class Database:
    """数据库管理类"""
    
    def __init__(self, db_path='data/swabox.db'):
        os.makedirs('data', exist_ok=True)
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_tables()
    
    def create_tables(self):
        """创建数据表"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tools (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT,
                path TEXT,
                url TEXT
            )
        ''')
        self.conn.commit()
    
    def add_tool(self, name, category, path='', url=''):
        """添加工具"""
        self.cursor.execute(
            'INSERT INTO tools (name, category, path, url) VALUES (?, ?, ?, ?)',
            (name, category, path, url)
        )
        self.conn.commit()
    
    def get_tools_by_category(self, category):
        """按类别获取工具"""
        self.cursor.execute(
            'SELECT * FROM tools WHERE category = ?',
            (category,)
        )
        return self.cursor.fetchall()
    
    def close(self):
        """关闭数据库"""
        self.conn.close()

# 使用示例
db = Database()
db.add_tool('360急救箱', 'fix', 'tools/360box.exe')
tools = db.get_tools_by_category('fix')
db.close()
```

---

## 测试指南

### UI 测试清单

#### 主窗口测试
- [ ] 窗口正常显示
- [ ] Logo 和标题正确显示
- [ ] 所有按钮可点击
- [ ] 图标正确加载
- [ ] 窗口大小固定

#### 功能测试
- [ ] 点击按钮打开对应窗口
- [ ] 退出按钮关闭窗口
- [ ] 各工具按钮响应正常
- [ ] 信号槽连接正确

#### 设置对话框测试
- [ ] 对话框正常显示
- [ ] 选项卡切换正常
- [ ] 关于信息显示正确

### 代码测试

```python
import unittest
from PySide6.QtWidgets import QApplication
from src.main import MainWindow

class TestMainWindow(unittest.TestCase):
    
    def setUp(self):
        self.app = QApplication([])
        self.window = MainWindow()
    
    def test_window_created(self):
        """测试窗口创建"""
        self.assertIsNotNone(self.window)
    
    def test_ui_setup(self):
        """测试 UI 初始化"""
        self.assertTrue(hasattr(self.window, 'settings'))
        self.assertTrue(hasattr(self.window, 'exit'))

if __name__ == '__main__':
    unittest.main()
```

---

## 调试技巧

### 打印调试信息

```python
import sys

# 启用详细输出
DEBUG = True

def debug_print(*args):
    if DEBUG:
        print("[DEBUG]", *args, file=sys.stderr)

# 使用示例
debug_print("窗口创建:", window)
```

### 使用日志模块

```python
import logging

# 配置日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('log/app.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# 使用示例
logger.info("应用启动")
logger.debug(f"窗口状态：{window.isVisible()}")
logger.error(f"发生错误：{str(e)}")
```

### Qt 调试

```python
# 启用 Qt 调试信息
import os
os.environ['QT_DEBUG_PLUGINS'] = '1'

# 查看 Qt 版本
from PySide6.QtCore import qVersion
print(f"Qt Version: {qVersion()}")
```

---

## 打包发布

### 使用 PyInstaller 打包

#### 1. 安装 PyInstaller
```bash
pip install pyinstaller
```

#### 2. 创建 spec 文件
```bash
pyi-makespec --windowed --icon=res/img/logo.png src/main.py
```

#### 3. 编辑 main.spec
```python
a = Analysis(
    ['src/main.py'],
    datas=[
        ('res/UI/*.ui', 'res/UI'),
        ('res/img/*', 'res/img'),
        ('lib/page/*.py', 'lib/page'),
        ('...', '...'),
    ],
    hiddenimports=['lib.page.MainPage', 'lib.page.Settings', "..."],
    # ... 其他配置
)
```

#### 4. 打包
```bash
pyinstaller main.spec
```

#### 5. 测试打包结果
```bash
# 在 dist 目录运行生成的 exe
.\dist\main\main.exe
```

---

## 性能优化建议

### 1. 延迟加载模块

```python
# ✅ 推荐：按需导入
def SettingsBtnClicked(self):
    from lib.page.Settings import Ui_settings
    # 使用时才导入
```

### 2. 缓存 UI 实例

```python
class MainWindow(QMainWindow, Ui_MainPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._settings_dialog = None  # 缓存设置对话框
    
    def SettingsBtnClicked(self):
        if self._settings_dialog is None:
            from PySide6.QtWidgets import QDialog
            from lib.page.Settings import Ui_settings
            
            self._settings_dialog = QDialog()
            self._settings_ui = Ui_settings()
            self._settings_ui.setupUi(self._settings_dialog)
        
        self._settings_dialog.show()
```

### 3. 使用资源文件

```python
# 将图片等资源编译为 Python 模块
pyside6-rcc res/resources.qrc -o res/resources_rc.py

# 在代码中使用
from res import resources_rc
icon = QIcon(":/img/logo.png")
```

---

## 常见问题解决

### Q1: AttributeError: type object 'QApplication' has no attribute 'setHighDpiAwarenessPolicy'
**问题**: PySide6 不支持该方法

**解决**:
```python
# ❌ 错误写法
QApplication.setHighDpiAwarenessPolicy(...)

# ✅ 正确写法（PySide6 默认启用）
app = QApplication(sys.argv)
app.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.Round)
```

### Q2: ModuleNotFoundError: No module named 'MainPage'
**问题**: 导入路径错误

**解决**:
```python
# 在 lib/page/__init__.py 中使用相对导入
from . import MainPage, Settings
```

### Q3: 中文乱码
**问题**: UI 文件编码问题

**解决**:
- 确保 .ui 文件使用 UTF-8 编码
- 在 Python 文件中添加 `# -*- coding: utf-8 -*-`

### Q4: 图标不显示
**问题**: 图标路径错误

**解决**:
```python
# 检查路径是否正确
icon_path = "../res/img/logo.png"
if os.path.exists(icon_path):
    self.setWindowIcon(QIcon(icon_path))
```

### Q5: UI 修改后未生效
**问题**: 未重新生成 Python 代码

**解决**:
```bash
# 重新转换 UI 文件
pyside6-uic res/UI/MainPage.ui -o lib/page/MainPage.py
```

---

## 贡献代码规范

### 代码风格
- 遵循 PEP 8 规范
- 函数和类添加文档字符串

### Git 提交规范
```bash
# 功能添加
git commit -m "feat: 添加工具分类页面"

# Bug 修复
git commit -m "fix: 修复设置对话框无法打开的问题"

# 文档更新
git commit -m "docs: 更新开发者指南"

# 代码重构
git commit -m "refactor: 优化 UI 加载逻辑"

# 性能优化
git commit -m "perf: 使用缓存提升启动速度"

# 其他
git commit -m "oth: 添加.gitignore 文件忽略日志文件"
```

### PR 提交流程
1. Fork 本项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

---

## 资源链接

### 官方文档
- [Python 官方文档](https://docs.python.org/zh-cn/3/)
- [PySide6 官方文档](https://doc.qt.io/qtforpython-6/)
- [Qt Designer 手册](https://doc.qt.io/qt-6/qtdesigner-manual.html)
- [QSS 样式指南](https://doc.qt.io/qt-6/stylesheet-reference.html)

### 相关工具
- [PyInstaller](https://www.pyinstaller.org/) - Python 打包工具
- [Qt Designer](https://www.qt.io/product/design-tools) - UI 设计工具
- [VS Code](https://code.visualstudio.com/) - 代码编辑器
- [PyCharm](https://www.jetbrains.com/pycharm/) - Python IDE

---

*最后更新时间：2026 年 5 月 15 日*
