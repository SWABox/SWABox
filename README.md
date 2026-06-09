<div align="center">

# SWABox

[![Stars](https://img.shields.io/github/stars/SWABox/SWABox?label=Stars)](https://github.com/SWABox/SWABox)
[![下载量](https://img.shields.io/github/downloads/SWABox/SWABox/total?style=social&label=下载量&logo=github)](https://github.com/SWABox/SWABox/releases/latest)
![Language-Python](https://img.shields.io/badge/语言-Python-blue)
![OS-Windows](https://img.shields.io/badge/适用系统-Windows-blue)
[![正式版 Release](https://img.shields.io/github/v/release/SWABox/SWABox?style=flat-square&color=%22c55d&label=正式版)](https://github.com/SWABox/SWABox/releases/latest)

[🌐 官方网站](https://swabox.cc.cd/) ｜ [📚 项目文档](docs/index.md)

SWABox 是一款为学校电教委即智能白班管理员提供工具下载的实用工具箱 <br/>
本软件中文译名可称为电教工具箱

</div>


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
├── Static/                    # 静态文件
├── pyproject.toml           # 项目配置文件
├── LICENSE                  # 许可协议
├── main.py                  # 主程序入口
├── .gitignore               # Git 忽略文件配置
└── README.md                # 项目说明文档
```
##  安装指南
#### 详见 [用户手册](docs/user_manual.md)

### 使用 Windows 安装包
从 [https://github.com/SWABox/SWABox](https://github.com/SWABox/SWABox) 的 Releases 页面下载最新的 `.exe` 安装包（或 `.msi`、便携版压缩包）。
1. 下载后双击运行
2. 如果 Windows SmartScreen 弹出警告，点击"更多信息"然后选择"仍要运行"（这是打包工具常见的误报，并非安全问题；如果仍有顾虑，可以从源码运行）
3. 安装路径建议不要包含中文，避免潜在兼容问题
4. 如果启动后没反应，可以尝试右键以管理员身份运行

##  使用指南

###  功能介绍
#### __该工具箱旨在帮助电教委门能够快速地获取白板优化工具，修复工具，实用软件及维护文件等工具，实现简便、快捷、高效的体验，简化流程，节省时间__
#### __同时，也内置了一些像360急救箱这样的急救工具在本地，需要时可通过软件直接启动，或通过本地目录启动，能够在紧急时刻快速解决问题。也包含了像希沃官网这样的快捷网站，能够快捷地获取帮助，软件与系统镜像__

###  使用方法
1. 运行项目
2. 选择需要下载的工具类型
3. 选择对应软件名称
4. 自动跳转至官网下载对应软件

#### 手动添加本地工具
1. 打开项目目录下的 `Tool` 目录
2. 将需要添加的工具文件（如可执行文件、脚本、目录等）放入该目录下

```
注意：
__若你是从安装程序安装的，则进入安装目录下的\SWABox-b0.3.0\_internal\目录下的的 Tool 目录__
```

3. 再次运行项目，在紧急工具界面的添加工具中添加该工具（待开发）
4. 在紧急工具界面中使用该工具（待开发）

### 界面展示
![主页面](res/img/Main_Page.png "主界面演示")

###  项目结构
#### 1. 主程序入口
- `main.py`: 负责启动整个应用程序，并加载主界面。
#### 2. 数据存储
- `config.ini`: 用于存储软件的配置信息，如下载路径、日志路径等。
#### 3. 资源文件夹
- `sound`, `IMG`: 存放音频、图像等资源文件。
#### 4. 开发与使用文档
- `doc`: 存放开发与使用相关文档。


##  参与贡献
#### __欢迎提交 Issue 和 Pull Request 来改进这个项目！__

##  未来规划
- [x] 工具类型的罗列
- [ ] 实现运行日志生成
- [x] 内置急救类软件
- [ ] 数据存储转为数据库形式
- [x] 美化界面
- [x] 项目打包为exe
- [ ] 搭建镜像站，实现在线下载（资金充足的情况下）

##  特别说明

#### __项目发起人语法欠佳 望理解__
#### __项目内部分功能由AI生成,望知悉（文档除README外，其余均由AI编写 后续将逐步去AI化）__
#### __有时部分文档会遗漏填写，望理解__
<a href="https://ys-api.mihoyo.com/event/download_porter/link/ys_cn/official/pc_backup316">千万别点</a>
