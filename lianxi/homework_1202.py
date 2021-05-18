# 1、现在有字符串：str1 = 'python cainiao 666'
#请找出第 5 个字符。
str1 = 'python cainiao 666'
print(str1[4])
#请找出第 3 到 第 8 个字符。
print(str1[2:8])


#2、卖橘子的计算器：写一段代码，提示用户输入橘子的价格，和重量，最后计算出应该支付的金额！（不需要校验数据，都传入数字就可以了。）
price = int(input("请输入橘子的单价："))
weight = int(input("请输入句子的重量："))
money = price * weight
print("您需要支付",money,"元")



# 3.演练字符串操作
my_hobby = "Never stop learning!"
# 截取从 位置2 ~ 位置6 的字符串
print(my_hobby[1:6])
# 截取从 开始位置~ 位置6 的字符串
print(my_hobby[:6])
# 从 索引3 开始，每2个字符中取一个字符
print(my_hobby[3::2])
# 截取字符串末尾两个字符
print(my_hobby[-1:-3:-1])
print(my_hobby[-2:])
#说明：“位置”指的是字符所处的位置（比如位置1，指的是第一个字符“N”），“索引”指的是字符的索引值（比如索引0， 代表的是第一个字符“N”）