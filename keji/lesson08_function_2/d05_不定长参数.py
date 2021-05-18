"""
*b 表示不定长参数：长度不固定, 剩下的我全要：垃圾桶，
接受所有剩下的位置参数。
多个数据，要放到一个变量，元组。

**kw, 接受关键字参数，kw 得到的是字典。
不定长是函数定义的时候去接受多个值。

"""
# def add(a, *b, c, **kw):
#     print("a:", a)
#     print("b:", b)
#     print("kw:", kw)
#
# # add(4,5,6,7,8, c=9, d="hello")
#
#
# def add(a, *b, **kw):
#     print("a:", a)
#     print("b:", b)
#
# name = "yuz"
# # 拆包
# dalao = ["zaizai", "achool"]  # 列表和元组
# add(name, *dalao)
# add("yuz", "zaizai", "achool")
#
# adict = {"you": "hello"}
# add(name, *dalao, **adict)
# add("yuz", "zaizai", "achool", you="hello")


#
def minus(a, **kw):
    print(a)
    print(kw)

name = "yuz"
# a = name
info = {"age": 18, "gender": "男"}
# minus(name, age=18, gender="男")
minus(name, **info)

# 形式参数，实际参数
# 位置参数， 一一对应，顺序和数量都要对上。
# 关键词参数和 默认
# 不定长参数。 *args  **kwargs  keyword_args

