#1、一家商场在降价促销，所有原价都是整数（不需要考虑浮点情况），如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣（%10或#20%）和最终价格。
price = int(input("请输入你购买的价格："))
if 50<=price<=100:
    print("我们会给你10%的折扣")
    print("您的最终价格是", (price * 0.960), "元")
elif price > 100:
    print("我们会给你20%的折扣")
    print("您的最终价格是" , (price * 0.8) , "元")


# 2 判断是否为闰年
# 提示:
# 输入一个有效的年份（如：2019），判断是否为闰年（不需要考虑非数字的情况）
# 如果是闰年，则打印“2019年是闰年”；否则打印“2019年不是闰年”
# 什么是闰年，请自行了解（需求文档没有解释）
year = int(input("请输入年份："))
if year % 4 == 0:
    print(year,"年是闰年")
else:
    print(year,"年不是闰年")



# 3.求三个整数中的最大值
# 提示：定义 3 个变量
a= int(input("请输入a的值："))
b= int(input("请输入b的值："))
c= int(input("请输入c的值："))
if a>b:
    if a>c:
        print("最大数是a,等于",a)
    else:
        print("最大数是c,等于",c)
else:
    if b>c:
        print("最大数是b,等于",b)
    else:
        print("最大数是c,等于",c)


# 4， 总结数据运算，做成笔记或者思维导图