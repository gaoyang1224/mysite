import random



"""
6，你的微信好友当中有 5 个推销的，他们存在一个列表 black_list=

['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']

 当中, 请把这 5 个人分别从 black_list 当中删除，最后 black_list 为空。
"""

# 列表是可变类型
# for 循环， index += 1
# 不要再循环当中去直接修改列表
# 提前 copy

black_list= ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
black_list_cp = black_list[:]
for name in black_list_cp:
    black_list.remove(name)
print(black_list)

# black_list.clear()
# print(black_list)


# for name in black_list:
#     black_list.remove(name)
#
# print(black_list)

# for i in range(len(black_list)):
#     black_list.pop(0)
#
# print(black_list)


# black_list.clear()
# for i in mylist():

# black_list_new = black_list[:]
#
# for wx in black_list_new:
#     black_list.remove(wx)
#
# print(black_list)
# #
# # 字符串的
# # 复制
# b = [1,2,3]
# a = b # 不是复制

# 总结.md：for 循环里去修改列表
# 以后千万不要在 for 循环当中去直接修改列表
# 如果要修改，copy

# 第二种
#  while
# for wx in black_list:
#     black_list.pop(0)
#     # index + 1
# print(black_list)

# while len(black_list) > 0:
#     black_list.pop(0)
# print(black_list)



"""
1.编写如下程序

尝试函数部分封装：

a.用户输入1-7七个数字，分别代表周一到周日

b.如果输入1~5，打印对应的“周一”~“周五”，如果输入的数字是6或7，打印输出“周末”：

c.如果输入0，退出循环

d.输入其他内容，提示：“输入有误，请重新输入！”
提示：本题可以使用if和while循环，同时需要校验用户的输入是否正确。不用考虑浮点数等情况。

# 写注释，把思路写下来

"""


# while True:
#     weekday = input("请输入数字：")
#     if weekday == "1":
#         print("周一")
#     elif weekday == "2":
#         print("周二")
#     elif weekday == "0":
#         break
#     else:
#         print("输入有误")


weekdays = {
    "1": "周一",
    "2": "周2",
    "3": "周3",
    "4": "周4",
    "5": "周5",
    "6": "周末",
    "7": "周末",
}

# while True:
#     user_input = input("请输入数字：")
#     if user_input in weekdays:
#         # 2  ==> weekdays["2"]
#         print(weekdays[user_input])
#     elif user_input == "0":
#         break
#     else:
#         print("输入错误")





"""
3， 使用遍历循环完成剪刀石头布游戏，提示用户输入要出的拳 ：石头（1）／剪刀（2）／布（3）/退出（4）
电脑随机出拳比较胜负，显示用户胜、负还是平局。运行如下图所示：


提示：电脑随机出拳

    使用随机数，首先需要导入随机数的模块 —— “工具包”

    import random

    导入模块后，可以直接在 模块名称 后面敲一个"."然后按 Tab键，会提示该模块中包含的所有函数

    random.randint(a, b)，返回[a, b]之间的整数，包含a和b

random.randint(1, 10)  # 生成的随机数n: 1 <= n <= 10
random.randint(4, 4)  # 结果永远是 4
random.randint(25, 12)  # 该语句是错误的，下限必须小于上限
"""

import random
print(random.randint(0, 100))



while True:
    # 自己的猜拳
    # 电脑出拳
    # 判断，如果。。。。情况
    # 如果 。。。
    # 如果。。。
    choice = input("请输入猜拳：石头（1）／剪刀（2）／布（3）/退出（4）")
    if choice == '4':
        print("退出游戏")
        break
    # 电脑出拳
    computer_choice = random.randint(1, 3)
    if (computer_choice == 1 and choice == '3') or (
            computer_choice == 2 and choice == '1') or (
            computer_choice == 3 and choice == '2'):
        print("我很厉害哦，赢了")
    elif str(computer_choice) == choice:
        print("平局")
    else:
        print('失败')




"""排序算法"""


"""
4.使用循环实现排序算法， 非常喜欢出面试题。

提示：利用for循环，完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法
"""
#
# a=[1,7,4,89,34,2]
#
def bubbleSort(arr):
    # http://testingpai.com/article/1596527692183
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # 交换位置
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # a, b = b,a


# for i in range(5, 1000):
#     if i % 2 == 1:
#         print(i)
#
# for i in range(5, 1000, 2):
#     print(i)
