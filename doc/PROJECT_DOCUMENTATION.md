# SWABox 项目开发文档

## 项目概述

### 项目名称
SWABox - 电教委工具箱

### 项目简介
一个基于 Python 和 PySide6 的图形界面应用程序，专为电教委设计。提供白板优化工具、修复工具、实用软件及维护文件等工具的快速访问和管理功能，实现简便、快捷、高效的体验，简化流程，节省时间。

### 版本信息
- **当前版本**: b0.1.0
- **开发语言**: Python
- **运行平台**: Windows
- **GUI 框架**: PySide6 (Qt for Python)

---

## 技术架构

### 核心技术栈
1. **Python**: 主要编程语言
2. **PySide6**: Qt for Python，现代化 GUI 框架
3. **Qt Designer**: UI 设计工具（.ui 文件）
4. **logging**: Python 日志库

### 项目结构

```
SWABox/
├── src/                      # 源代码目录
│   └── main.py              # 主程序入口
├── lib/                      # 功能模块库
│   ├── page/                # 页面模块
│   │   ├── MainPage.py      # 主页面 UI
│   │   ├── Settings.py      # 设置页面 UI
│   │   └── __init__.py
│   └── package/             # 功能包（待扩展）
├── res/                      # 资源文件
│   ├── UI/                  # Qt Designer UI 文件
│   │   ├── MainPage.ui      # 主页面设计文件
│   │   └── Sittings.ui      # 设置页面设计文件
│   ├── img/                 # 图片资源
│   │   └── logo.png         # 应用图标
│   └── sound/               # 音频资源（待添加）
├── data/                     # 数据文件（待扩展）
├── log/                      # 日志文件
├── doc/                      # 文档目录
├── pyproject.toml           # 项目配置文件
└── README.md                # 项目说明文档
```

---

## 核心模块说明

### 1. 主程序模块 (`src/main.py`)

#### 类：`MainWindow(QMainWindow, Ui_MainPage)`
主应用程序窗口类，负责：
- 创建和初始化主窗口
- 加载主页面 UI
- 管理各个功能页面的入口

#### 主要方法
- `__init__()`: 初始化主窗口，设置 UI，连接信号槽
- `SettingsBtnClicked()`: 打开设置对话框

#### 功能特性
- 基于 PySide6 QMainWindow 构建
- 使用 Qt Designer 设计的 UI 文件
- 支持高 DPI 显示
- 固定窗口大小 (413x356)
- 模块化设计，易于扩展

### 2. 页面模块 (`lib/page/`)

所有页面模块都由 Qt Designer 生成，遵循统一的设计模式。

#### 模块列表
- **MainPage.py**: 主页面 UI 类 (`Ui_MainPage`)
  - 提供工具箱主界面
  - 包含工具按钮：优化工具、修复工具、实用软件、维护文件
  - 包含功能按钮：设置、帮助、退出
  
- **Settings.py**: 设置页面 UI 类 (`Ui_settings`)
  - 基础设置选项卡
  - 个性化设置选项卡
  - 关于信息选项卡（显示项目发起人和项目名称）

#### 统一设计模式
所有页面类均使用 Qt Designer 生成，具有：
- `setupUi()` 方法用于初始化 UI
- `retranslateUi()` 方法用于国际化支持
- 通过信号槽机制实现交互

### 3. UI 设计文件 (`res/UI/`)

#### 文件列表
- **MainPage.ui**: 主页面设计文件
  - 窗口尺寸：413x356
  - 包含 Logo、标题、功能按钮
  
- **Sittings.ui**: 设置页面设计文件
  - 窗口尺寸：424x295
  - 使用 QTabWidget 组织设置项

### 4. 数据存储（计划中）

未来将实现：
- 使用 SQLite 数据库存储工具信息
- JSON 配置文件存储用户偏好
- 日志系统记录运行状态

---

## 功能特性

### 已实现功能
✅ 项目初始化与基础架构搭建  
✅ 基于 PySide6 的主界面设计  
✅ Qt Designer UI 文件集成  
✅ 设置对话框功能  
✅ 模块化页面设计  
✅ 友好的错误处理  
✅ 高 DPI 支持

### 待实现功能
⬜ 工具类型的罗列与分类  
⬜ 内置急救类软件（如 360 急救箱）  
⬜ 运行日志生成系统  
⬜ 数据库存储（替代硬编码）  
⬜ 美化界面与主题切换  
⬜ 项目打包为 exe  
⬜ 快捷网站访问（如希沃官网）  
⬜ 在线下载功能（需搭建镜像站）  

---

## 安装与运行

### 环境要求
- Python 3.8+
- Windows 操作系统
- PySide6 依赖

### 依赖安装
```bash
# PySide6 GUI 库
pip install PySide6

# Qt Designer 工具（可选，用于编辑 .ui 文件）
pip install pyqt5-tools
```

### 运行方式
```bash
python src/main.py
```

---

## 设计规范

### 代码规范
- 变量命名：驼峰命名法 (camelCase)
- 类命名：大驼峰命名法 (PascalCase)
- 函数注释：使用文档字符串 (docstring)
- 错误处理：使用 try-except 捕获异常

### UI 设计规范
- 使用 Qt Designer 设计界面
- 保持 UI 文件与 Python 代码分离
- 使用信号槽机制实现交互
- 窗口尺寸根据内容自适应

### 文件组织规范
- 所有页面模块放在 `lib/page/` 目录
- UI 设计文件放在 `res/UI/` 目录
- 资源文件统一放在 `res/` 目录
- 数据文件存放在 `data/` 目录
- 日志文件存放在 `log/` 目录

---

## 测试与调试

### UI 测试
每个页面模块都可以独立测试：
```python
# 测试主窗口
from PySide6.QtWidgets import QApplication
from lib.page.MainPage import Ui_MainPage

app = QApplication([])
window = Ui_MainPage()
# 需要配合 QMainWindow 使用
```

### 日志调试
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
logger.info("应用启动")
```

---

## 常见问题

### Q1: AttributeError: type object 'QApplication' has no attribute 'setHighDpiAwarenessPolicy'
**原因**: PySide6 不需要手动设置高 DPI 策略  
**解决**: 删除相关代码，PySide6 默认启用高 DPI 支持

### Q2: ModuleNotFoundError: No module named 'MainPage'
**原因**: 导入路径错误  
**解决**: 在 `lib/page/__init__.py` 中使用相对导入 `from . import MainPage`

### Q3: 依赖安装失败
**原因**: pip 源问题或网络问题  
**解决**: 使用国内镜像源
```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple PySide6
```

### Q4: UI 文件无法加载
**原因**: .ui 文件路径错误或未转换为 Python 代码  
**解决**: 确保 UI 文件存在，或使用 `pyside6-uic` 转换

---

## 开发计划

详细的版本更新日志和开发计划请查看 `CHANGELOG.md`

### 短期目标
- [ ] 完善所有工具页面的 UI 设计
- [ ] 实现工具分类展示（优化、修复、实用、维护）
- [ ] 添加运行日志系统
- [ ] 优化错误提示机制

### 中期目标
- [ ] 引入 SQLite 数据库管理工具信息
- [ ] 内置急救类软件（360 急救箱等）
- [ ] 添加快捷网站访问功能
- [ ] 支持工具搜索功能

### 长期目标
- [ ] 实现工具直接启动功能
- [ ] 添加工具更新检测
- [ ] 打包为独立 exe 程序
- [ ] 搭建镜像站，实现在线下载
- [ ] 支持插件扩展系统

---

## 贡献指南

### 提交 Issue
遇到问题或有新想法时，欢迎提交 Issue

### 提交 PR
1. Fork 本项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

### 代码规范
- 遵循 PEP 8 Python 代码规范
- 添加必要的注释和文档字符串
- 确保代码可测试性

---

## 许可证

本项目仅供个人学习和研究使用

---

## 联系方式

- **作者**: liyunhan177 (A.R.O.N.A)
- **GitHub**: [@liyunhan177](https://github.com/liyunhan177)
- **Bilibili**: [UID: 571556798](https://space.bilibili.com/571556798)

---

## 致谢

感谢所有为本项目做出贡献的开发者和用户！

特别感谢：
- Qt 团队提供的优秀 PySide6 框架
- AI 开发辅助工具 Lingma
- 所有提供工具和资源的合作方

---

*最后更新时间：2026 年 5 月 14 日*
