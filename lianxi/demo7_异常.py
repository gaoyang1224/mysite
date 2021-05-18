# a = "你好"
# print(a + 1)
#
# print())))

try:
    1/0
except:
    print("出现异常")


a = 3
b = 0
try:
    [1,2][100]
    a/b
except ZeroDivisionError as e:
    print(e)
    print("出现异常")
except IndexError as e:
    print(e)





