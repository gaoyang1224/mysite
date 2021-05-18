"""
pip: 安装 python插件、python库、python包
- requests
- openpyxl

注释：不是给机器看的，不是代码。给人看，说明代码的作用
    - 单行注释， #
    - 多行注释 '''注释 '''


缩进：
    python 是根据缩进来组织代码块的。：
    从现在开始，所有的 python 代码顶格写。

变量：
     1 * 2 * 3 * 4 * 5
     变量：存储数据，变
     常量：不变

变量命名：
    - 字母，数字和下划线 _， 其他的都不可以 @， 中文
    - 不能以数字开头；
    - 不能是 python 内置的关键字；贵族号码， return def if
    - 变量最重要的是能 “见名知意”

注释快捷键： ctrl + /


"""

# 把什么内容打印到屏幕上
print("python36期全部是大佬")

# 注释
print("注释")

# 先存储1 , 变量赋值
a = 1
a = a * 2
print(a)
a = a * 3
a = a * 4
a = a * 5
print(a)

# 雨泽 = 345
# print(雨泽)
# 1a = 456

# return = "123"
# def = '345'
# True = '123'

import keyword
print(keyword.kwlist)

age = 19
name = "yuz"
# 拼音不要用
# 缩写 金量不要用。
name = "yuz"


# 变量练习题：
name = "yuz"
name_other = "wang"
full_name = name + name_other
print(full_name)

name = "wen"
print(name)