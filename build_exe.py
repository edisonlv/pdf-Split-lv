import PyInstaller.__main__
import os
import sys

# 获取当前脚本所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# PyInstaller参数
params = [
    'pdf_splitter_tkinter_new.py',  # 主程序文件
    '--name=PDF分割工具',  # 生成的exe名称
    '--noconsole',  # 不显示控制台窗口
    '--onefile',  # 打包成单个文件
    '--clean',  # 清理临时文件
    '--windowed',  # Windows下不显示命令行
    '--add-data=README.md;.',  # 添加README文件
    '--hidden-import=tkinter',
    '--hidden-import=PIL',
    '--hidden-import=PyPDF2',
    '--hidden-import=fitz',
    '--hidden-import=json',
    '--hidden-import=os',
    '--hidden-import=sys',
    '--hidden-import=re',
    '--hidden-import=shutil',
    '--hidden-import=tempfile',
    '--hidden-import=threading',
    '--hidden-import=queue',
    '--hidden-import=time',
]

# 运行PyInstaller
PyInstaller.__main__.run(params) 