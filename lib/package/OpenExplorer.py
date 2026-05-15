import os
import subprocess
import sys


def get_base_path():
    """
    获取程序运行的基础路径
    开发环境：返回项目根目录
    打包后：返回exe所在目录
    """
    if getattr(sys, 'frozen', False):
        # 如果是打包后的exe，返回exe所在目录
        # 使用sys._MEIPASS来获取PyInstaller解压的临时目录
        if hasattr(sys, '_MEIPASS'):
            return sys._MEIPASS
        else:
            return os.path.dirname(sys.executable)
    else:
        # 如果是开发环境，返回项目根目录（main.py所在目录）
        return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def open_tool_folder():
    try:
        # 获取Tool文件夹的路径
        base_path = get_base_path()
        tool_path = os.path.join(base_path, 'Tool')

        # 检查文件夹是否存在
        if not os.path.exists(tool_path):
            print(f"错误：Tool文件夹不存在：{tool_path}")
            # 尝试其他可能的路径
            alt_tool_path = os.path.join(os.path.dirname(sys.executable), 'Tool')
            if os.path.exists(alt_tool_path):
                tool_path = alt_tool_path
            else:
                print(f"错误：备选Tool文件夹也不存在：{alt_tool_path}")
                return False

        # 根据操作系统选择打开方式
        if sys.platform == 'win32':
            # Windows系统使用explorer命令
            os.startfile(tool_path)
        elif sys.platform == 'darwin':
            # macOS系统使用open命令
            subprocess.Popen(['open', tool_path])
        else:
            # Linux系统使用xdg-open命令
            subprocess.Popen(['xdg-open', tool_path])

        return True

    except Exception as e:
        print(f"打开Tool文件夹失败：{str(e)}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    # 直接运行时打开Tool文件夹
    open_tool_folder()
