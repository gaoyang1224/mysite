print(__file__)

# with open("cases.txt") as f:
#     f.read()

#路径操作
import os
#获取当前为文件绝对路径
print(os.path.abspath(__file__))
#获取目录print(__file__)
cwd = os.path.abspath(__file__)
cwd_dir = os.path.dirname(cwd)
print(cwd_dir)

#获取主目录project的路径
print(os.path.dirname(os.path.dirname(cwd_dir)))
#------------------------------------------------------------------
#获取cases.txt的路径
cwd = os.path.abspath(__file__)
cwd_dir = os.path.dirname(cwd)
file = os.path.join(cwd_dir,'date',' cases.txt')
print(file)

#创建目录
cwd_dir = os.path.dirname(cwd)

#创建一个config目录(相对路径)
# os.mkdir('config')

#绝对路径
py36 = os.path.dirname(os.path.dirname(cwd_dir))
lujing = os.path.join(py36,'config')
print(lujing)

#isdir ,isdir
print(os.path.isfile('d01  '))