"""路径"""
import os
# reports的目录
# 动态获取路径
config_path = os.path.dirname(os.path.abspath(__file__))

# 项目目录
root_path = os.path.dirname(config_path)

# reports路径
reports_path = os.path.join(root_path, 'reports')
if not os.path.exists(reports_path):
    os.mkdir(reports_path)

# logs路径
logs_path = os.path.join(root_path, 'logs')
if not os.path.exists(logs_path):
    os.mkdir(logs_path)