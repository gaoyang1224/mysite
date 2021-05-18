# __file__ 表示文件名（路径）
print(__file__)

# 打开
# open("", )
# with open("cases.txt") as f:
#     f.read()

# 路径操作 os.path
import os

# os.path.abspath(__file__): 获取当前文件的绝对路径
print(os.path.abspath(__file__))

# os.path.dirname 获取父级目录
cwd = os.path.abspath(__file__)
cwd_dir = os.path.dirname(cwd)
print(os.path.dirname(cwd_dir))
# 通过现在的文件路径获取 py36 的路径， dirname 的 dirname
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 获取 case.txt,
# 1、自己的路径
# 2、父目录的路径
# 3、父目录 + data\cases.txt
# D:\classes\py36\lesson11_路径和异常\data\cases.txt

cwd = os.path.abspath(__file__)
cwd_dir = os.path.dirname(cwd)
# 拼接
file = os.path.join(cwd_dir, 'data', 'cases.txt')
print(file)
print(type(file))

# 创建目录
cwd_dir = os.path.dirname(cwd)

# 创建一个 config 目录
# 第二次创建会报错
# os.mkdir("config")

py36 = os.path.dirname(cwd_dir)
print(py36)
config_path = os.path.join(py36, "config")

# 判断路径是否真实存在
if not os.path.exists(config_path):
    os.mkdir(config_path)


# isdir, isfile
print(os.path.isfile(config_path))
print(os.path.isdir(config_path))

