"""
项目入口，主程序。
收集用例，运行用例，生成报告。
"""

import pytest

# pytest 收集用例，
# 如何放到 reports
# TODO：报告+时间戳。
# reports/report.html
pytest.main(['--html=report.html', '-s'])
