# 使用for打印九九乘法表
#
# 提示：
#
# 输出九九乘法表，格式如下：（每项数据之间空一个Tab键，可以使用"\t"）
#
# 1 * 1 = 1
# 1 * 2 = 2    2 * 2 = 4
# 1 * 3 = 3    2 * 3 = 6      3 * 3 = 9
# 1 * 4 = 4    2 * 4 = 8      3 * 4 = 12    4 * 4 = 16
# 1 * 5 = 5    2 * 5 = 10    3 * 5 = 15    4 * 5 = 20    5 * 5 = 25
# 1 * 6 = 6    2 * 6 = 12    3 * 6 = 18    4 * 6 = 24    5 * 6 = 30    6 * 6 = 36
# 1 * 7 = 7    2 * 7 = 14    3 * 7 = 21    4 * 7 = 28    5 * 7 = 35    6 * 7 = 42    7 * 7 = 49
# 1 * 8 = 8    2 * 8 = 16    3 * 8 = 24    4 * 8 = 32    5 * 8 = 40    6 * 8 = 48    7 * 8 = 56    8 * 8 = 64
# 1 * 9 = 9    2 * 9 = 18    3 * 9 = 27    4 * 9 = 36    5 * 9 = 45    6 * 9 = 54    7 * 9 = 63    8 * 9 = 72    9 * 9 = 81
for m in range(1, 10):
    for n in range(1, m + 1):
        print("{}*{}={}".format(n, m, m * n), end="\t")
    print()

# 你的微信好友当中有 5 个推销的，他们存在一个列表 black_list=['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
# 当中, 请依次把这 5 个人分别从 black_list 当中删除，最后 black_list 为空。（不要使用 clear）
black_list = ['卖茶叶', '卖面膜', '卖保险', '卖花生', '卖手机']
black_list_cp = black_list[:]
for i in black_list_cp:
    black_list.pop(0)
    print(black_list)

# 编写如下程序
# a.用户输入1-7七个数字，分别代表周一到周日
#
# b.如果输入1~5，打印对应的“周一”~“周五”，如果输入的数字是6或7，打印输出“周末”
#
# c.如果输入0，退出循环
#
# d.输入其他内容，提示：“输入有误，请重新输入！”
#
# 提示：本题可以使用if和while循环，同时需要校验用户的输入是否正确。不用考虑浮点数等情况。
while True:
    week = input("请输入1-7数字：")
    if week == "0":
        print("退出")
        break

    if week == "1":
        print("周一")
    elif week == "2":
        print("周二")
    elif week == "3":
        print("周三")
    elif week == "4":
        print("周四")
    elif week == "5":
        print("周五")
    elif week == "6":
        print("周末")
    elif week == "7":
        print("周末")
    else:
        print("输入有误，请重新输入！")

# 使用遍历循环完成剪刀石头布游戏，提示用户输入要出的拳 ：石头（1）／剪刀（2）／布（3）/退出（4）
# 电脑随机出拳比较胜负，显示用户胜、负还是平局。运行如下图所示：
# 提示：电脑随机出拳
# 使用随机数，首先需要导入随机数的模块 —— “工具包”
# import random
# 导入模块后，可以直接在 模块名称 后面敲一个"."然后按 Tab键，会提示该模块中包含的所有函数
# random.randint(a, b)，返回[a, b]之间的整数，包含a和b
#
# random.randint(1, 10)  # 生成的随机数n: 1 <= n <= 10
# random.randint(4, 4)  # 结果永远是 4
# random.randint(25, 12)  # 该语句是错误的，下限必须小于上限
# import random
# print(random.randint(1, 10))
import random

print("请按下面提示出拳")
while True:
    finger_guessing = input("输入要出的拳 ：石头（1）／剪刀（2）／布（3）/退出（4）")
    if finger_guessing == "4":
        print("退出")
        break
    computer_guessing = random.randint(1, 3)
    if (computer_guessing == 1 and finger_guessing == "3") or (computer_guessing == 2 and finger_guessing == "1") or (
            computer_guessing == 3 and finger_guessing == "2"):
        print("你赢了")
    elif computer_guessing == int(finger_guessing):
        print("平局")
    elif (computer_guessing == 1 and finger_guessing == "2") or (computer_guessing == 2 and finger_guessing == "3") or (
            computer_guessing == 3 and finger_guessing == "1"):
        print("电脑赢了")
    else:
        print("输入错误，请重新输入")


# 2， 打印 5-999 的所有奇数
for i in range(5, 1000):
    if i % 2 != 0:
        print(i)

# 选做：（不需要提交，面试之前背熟）
#
#
#
# 使用循环实现排序算法（冒泡，选择等算法选择一个，请自行了解。）
#
# 提示：利用for循环，完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法
