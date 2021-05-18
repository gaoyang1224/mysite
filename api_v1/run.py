"""
项目入口，主程序
收集用例，运行用例，生成报告
"""
import pytest

# pytest收集用例
pytest.main(['--html=report.html','-s'])
