"""
项目入口，主程序
收集用例，运行用例，生成报告
在Terminal中输入python run.py
"""

import pytest

#pytest收集用例
#如何放到 reports里，要加时间戳，文件名一样（报告+时间戳）
pytest.main(['--html=report.html','-s'])
