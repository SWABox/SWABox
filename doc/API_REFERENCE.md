# SWABox API 参考文档

## 概述

本文档提供了 SWABox 项目的完整 API 参考，包括所有公共类、方法和函数的详细说明。

---

## 模块索引

### 核心模块
- [`src/main.py`](#srcmainpy) - 主程序入口
- [`lib/page/MainPage.py`](#libpagemainpagepy) - 主页面 UI
- [`lib/page/Settings.py`](#libpagesettingspy) - 设置页面 UI

---

## src/main.py

### 类：MainWindow

主应用程序窗口类

#### 继承关系
```python
MainWindow(QMainWindow, Ui_MainPage)
```

#### 构造函数

**`__init__()`**

初始化主窗口，包括：
- 调用父类构造函数
- 设置 UI（通过 `setupUi()`）
- 连接信号槽（设置按钮点击事件）

**参数**: 无

**返回**: 无

**示例**:
```python
from PySide6.QtWidgets import QApplication
from src.main import MainWindow

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
```

#### 方法

**`SettingsBtnClicked()`**

打开设置窗口

**功能描述**:
- 创建 QDialog 实例
- 初始化 Settings UI
- 显示设置对话框

**参数**: 无

**返回**: 无

**使用场景**:
当用户点击主界面的“设置”按钮时触发

---

## lib/page/ 模块

所有页面模块都由 Qt Designer 生成，遵循统一的设计模式。

### 通用类结构

每个页面模块都包含一个以 `Ui_` 开头的类：

- `MainPage.py` → `Ui_MainPage` 类
- `Settings.py` → `Ui_settings` 类

#### 通用方法

**`setupUi(widget)`**

初始化 UI 组件

**参数**:
- `widget`: QWidget 或其子类实例，将作为 UI 的容器

**返回**: 无

**功能**:
- 创建所有 UI 组件
- 设置组件属性和布局
- 连接信号槽

**`retranslateUi(widget)`**

重新翻译 UI 文本（用于国际化）

**参数**:
- `widget`: QWidget 或其子类实例

**返回**: 无

### 各模块说明

#### 1. MainPage.py - 主页面

**类**: `Ui_MainPage`

**UI 组件**:
- `icon`: QLabel - 显示 Logo 图片
- `title`: QLabel - 显示应用标题“电教委工具箱”
- `settings`: QPushButton - 设置按钮
- `exit`: QPushButton - 退出按钮（已连接 close 信号）
- `help`: QPushButton - 帮助按钮
- `OfTool`: QPushButton - 优化工具按钮
- `FixTool`: QPushButton - 修复工具按钮
- `PtTool`: QPushButton - 实用软件按钮
- `MtTool`: QPushButton - 维护文件按钮

**窗口配置**:
- 尺寸：413x356 像素
- 最小/最大尺寸：413x356（固定）
- 图标：`../res/img/logo.png`

#### 2. Settings.py - 设置页面

**类**: `Ui_settings`

**UI 组件**:
- `tabWidget`: QTabWidget - 选项卡控件
  - `Foundation`: 基础设置选项卡
  - `Personalized`: 个性化设置选项卡
  - `About`: 关于信息选项卡
    - `label`: 项目发起人标签
    - `label_2`: 显示“A.R.O.N.A (liyunhan177)”
    - `label_3`: 项目名称标签
    - `label_4`: 显示“电教委工具箱（SWA）”

**窗口配置**:
- 尺寸：424x295 像素
- 图标：`../res/img/logo.png`
- 默认选项卡：关于（索引 2）

---

## PySide6 常用 API

### QApplication

**`QApplication(sys.argv)`**

创建应用程序实例

**示例**:
```python
import sys
from PySide6.QtWidgets import QApplication

app = QApplication(sys.argv)
```

**`app.setHighDpiScaleFactorRoundingPolicy(policy)`**

设置高 DPI 缩放舍入策略

**参数**:
- `policy`: Qt.HighDpiScaleFactorRoundingPolicy 枚举值
  - `Round`: 四舍五入
  - `Floor`: 向下取整
  - `Ceil`: 向上取整

### QMainWindow

**`setWindowTitle(title)`**

设置窗口标题

**`setWindowIcon(icon)`**

设置窗口图标

**`show()`**

显示窗口

### QDialog

**`exec()`**

以模态方式显示对话框（阻塞直到关闭）

**注意**: 在 PySide6 中应使用 `exec()` 而非 `exec_()`

---

## Qt Designer UI 文件格式

### .ui 文件结构

Qt Designer 生成的 XML 格式文件

#### 主要元素

```xml
<ui version="4.0">
 <class>MainPage</class>
 <widget class="QMainWindow" name="MainPage">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>413</width>
    <height>356</height>
   </rect>
  </property>
  <!-- 其他组件 -->
 </widget>
</ui>
```

### 转换为 Python 代码

```bash
# 使用 pyside6-uic 转换
pyside6-uic res/UI/MainPage.ui -o lib/page/MainPage.py

# 批量转换
for file in res/UI/*.ui; do
    pyside6-uic "$file" -o "lib/page/$(basename ${file%.ui}).py"
done
```

---

## 常量定义

### PySide6 常用常量

```python
from PySide6.QtCore import Qt

# 高 DPI 缩放策略
Qt.HighDpiScaleFactorRoundingPolicy.Round    # 四舍五入
Qt.HighDpiScaleFactorRoundingPolicy.Floor    # 向下取整
Qt.HighDpiScaleFactorRoundingPolicy.Ceil     # 向上取整

# 对齐方式
Qt.AlignCenter    # 居中对齐
Qt.AlignLeft      # 左对齐
Qt.AlignRight     # 右对齐
```

### 信号与槽

```python
# 按钮点击信号
button.clicked.connect(slot_function)

# 关闭窗口
button.clicked.connect(window.close)
```

---

## 错误码参考

### 常见错误

| 错误类型 | 错误消息 | 可能原因 | 解决方案 |
|---------|---------|---------|----------|
| AttributeError | 'QApplication' has no attribute 'setHighDpiAwarenessPolicy' | PySide6 不支持该方法 | 删除相关代码 |
| ModuleNotFoundError | No module named 'MainPage' | 导入路径错误 | 使用相对导入 `from . import` |
| ImportError | cannot import name | 依赖未安装 | 运行 `pip install PySide6` |
| FileNotFoundError | .ui file not found | UI 文件路径错误 | 检查文件路径 |

### UI 相关错误

| 错误类型 | 错误消息 | 可能原因 | 解决方案 |
|---------|---------|---------|----------|
| 图标加载失败 | 无错误提示 | logo.png 文件不存在 | 检查 `res/img/logo.png` |
| 窗口创建失败 | Qt 异常 | 系统资源不足 | 关闭其他应用 |

---

## 最佳实践

### 1. UI 文件管理

```python
# ✅ 推荐：使用 Qt Designer 设计 UI
# 1. 在 Qt Designer 中设计界面
# 2. 保存为 .ui 文件
# 3. 使用 pyside6-uic 转换为 Python 代码

# ❌ 不推荐：手动编写大量 UI 代码
def create_ui(self):
    button1 = QPushButton("Button 1")
    button2 = QPushButton("Button 2")
    # ... 数百行代码
```

### 2. 信号槽连接

```python
# ✅ 推荐：在 __init__ 中连接信号槽
class MainWindow(QMainWindow, Ui_MainPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.settings.clicked.connect(self.SettingsBtnClicked)

# ❌ 不推荐：在外部连接
def connect_signals():
    window.settings.clicked.connect(handle_settings)
```

### 3. 模块化设计

```python
# ✅ 推荐：使用包管理模块
# lib/page/__init__.py
from . import MainPage, Settings

# main.py
from lib.page import *

# ❌ 不推荐：直接导入
import sys
sys.path.append('lib/page')
import MainPage
```

---

## 版本历史

详细的版本更新日志请查看 `CHANGELOG.md`

---

*最后更新时间：2026 年 5 月 14 日*
