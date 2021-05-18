"""
一个 py 的文件就叫模块。
包含__init__.py 的文件夹就叫包。

模块和包有什么用？？
组织代码的。

按照功能分类存储，函数就会存到不同的模块当中。
不同用途的模块又分别存到包里。

模块：内置模块和第三方模块。
如果我们想使用其他模块的代码，就需要导入。 import
"""

# import time
#
# # 调用 time 模块当中的 time 函数
# print(time.time())

# 第三方模块的倒入，自己的模块
# 路径从项目的根目录开始
# import lesson10_模块和路径.d01_open
# a = lesson10_模块和路径.d01_open.add(3,4)
# print(a)

from lesson10_模块和路径 import d01_open
a = d01_open.add(3,4)
print(a)

def add(a, b):
    return a - b

# 直接倒入函数
from lesson10_模块和路径.d01_open import add as module_add
b = add(3,4)
print(b)

# 在一个文件当中，如果出现同名的函数，之前的那个会被覆盖掉。
# 当倒入的标识符出现同名，一定要把其中的一个取别名，以免混淆
c = add(3,4)
print(c)

d = module_add(3,4)
print(d)


print(d01_open.add(3,4))


# 最后，倒入所有
# from lesson10_模块和路径.d01_open import *
# add()


# import : 内置
# from ..... import ... 主要用在自定义模块
# from.. import.. 既可以倒入模块，还可以直接倒入函数
# from... import... as ... 重命名
# from ... import * ，强烈建议不要用。


# from time import time
# time()
#
# import time
# time.time()


