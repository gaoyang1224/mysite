"""
项目入口，主程序
收集用例，运行用例，生成报告
在Terminal中输入python run.py
"""
from datetime import datetime
import os

import pytest
from config import path

# pytest收集用例
# 如何放到 reports里，要加时间戳，文件名一样（报告+时间戳）

# 获取现在时间戳
ts = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
report_file_name = 'report' + ts + '.html'

# 获取测试报告存储的目录
report_dir = path.reports_path
# 拼接文件
report_file = os.path.join(report_dir, report_file_name)
pytest.main(['--html={}'.format(report_file), '-s'])
