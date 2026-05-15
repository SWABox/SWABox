# SWABox
#### 一款专为电教委打造的工具箱
<p>
    <img alt="Dynamic JSON Badge" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3Dgithub%26queryKey%3Dliyunhan177&query=%24.data.totalSubs&suffix=%20followers&label=GitHub&color=262626">
    <img alt="Dynamic JSON Badge" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.bilibili.com%2Fx%2Frelation%2Fstat%3Fvmid%3D571556798&query=data.follower&style=flat&logo=bilibili&logoColor=white&label=bilibili%20fans&labelColor=%23F37697">
    <img src="https://img.shields.io/badge/Language-Python-blue" alt="">
    <img src="https://img.shields.io/badge/OS-Windows-blue" alt="">
    <img alt="" src="https://img.shields.io/badge/version-b0.3.0-yellow">
</p>

## 目录

- [🚀 快速开始](#快速开始)
- [📦 安装指南](#安装指南)
- [🛠 使用指南](#使用指南)
- [🤝 参与贡献](#参与贡献)
- [🌠 未来规划](#未来规划)
- [📝 特别说明](#特别说明)

##  快速开始
__项目结构__
```aiignore
SWABox/
├── src/                      # 源代码目录
│   └── main.py              # 主程序入口
├── lib/                      # 功能模块库
│   ├── page/                # 页面模块
│   └── package/             # 功能包
├── res/                      # 资源文件
│   ├── UI/                  # Qt Designer UI 文件
│   ├── img/                 # 图片资源
│   └── sound/               # 音频资源
├── data/                     # 数据文件
├── log/                      # 日志文件
├── doc/                      # 文档目录
├── pyproject.toml           # 项目配置文件
└── README.md                # 项目说明文档
```
##  安装指南
### 1. 克隆项目
```bash
git clone https://github.com/liyunhan177/SWABox.git
```
### 2. 安装所欲依赖
```bash
# PySide6 GUI库
pip install PySide6

# logging 日志库
pip install logging

# 设计工具
pip install pyqt5-tools
```
### 3. 运行项目
```bash
python src/main.py
```
##  使用指南

###  功能介绍
#### __该工具箱旨在帮助电教委门能够快速地获取白板优化工具，修复工具，实用软件及维护文件等工具，实现简便、快捷、高效的体验，简化流程，节省时间__
#### __同时，也内置了一些像360急救箱这样的急救工具在本地，需要时可通过软件直接启动，或通过本地目录启动，能够在紧急时刻快速解决问题。也包含了像希沃官网这样的快捷网站，能够快捷地获取帮助，软件与系统镜像__

###  使用方法
1. 运行项目
2. 选择需要下载的工具类型
3. 选择对应软件名称
4. 自动跳转至官网下载

### 界面展示
![主页面](res/img/Main_Page.png "主界面演示")

###  项目结构
#### 1. 主程序入口
- `main.py`: 负责启动整个应用程序，并加载主界面。
#### 2. 数据存储
- `data.json`: 用于存储软件的下载链接和其他相关信息(后续将转为数据库形式存储)
#### 3. 资源文件夹
- `sound`, `IMG`: 存放音频、图像等资源文件。
#### 4. 开发与使用文档
- `doc`: 存放开发与使用相关文档。


##  参与贡献
#### __欢迎提交 Issue 和 Pull Request 来改进这个项目！__
### Issus 模板：[issues模板](doc/PROJECT_DOCUMENTATION.md#Issue模板)

##  未来规划
- [x] 工具类型的罗列
- [ ] 实现运行日志生成
- [ ] 内置急救类软件
- [ ] 数据存储转为数据库形式
- [ ] 美化界面
- [ ] 项目打包为exe
- [ ] 搭建镜像站，实现在线下载（资金充足的情况下）

##  特别说明

#### __项目发起人语法欠佳 望理解__
#### __项目内部分功能由AI生成,望知悉（文档除更新日志外，其余均由AI编写）__
#### __有时部分文档会遗漏填写，望理解__
<a href="https://ys-api.mihoyo.com/event/download_porter/link/ys_cn/official/pc_backup316">千万别点</a>
