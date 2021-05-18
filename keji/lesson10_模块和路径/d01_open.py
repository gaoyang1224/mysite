
# 写入文件
# f = open("demo.txt", mode='w')
# f.write("hello world")
# f.close()

# 第二次打开同样的文件，之前的内容被覆盖了。
# f = open("demo.txt", mode='w', encoding="utf-8")
# f.write("阳光的味道")
# f.close()

# 不想覆盖, 模式要改成 a 模式， 追加， add
# f = open("demo.txt", mode='a', encoding="utf-8")
# f.write("不变的音乐")
# f.close()


# x，当文件存在时，不能写入。
# f = open("demo1.txt", mode='x', encoding="utf-8")
# f.write("yuz")
# f.close()


# 二进制类型， 图片，RGB,   (255, 255, 255)
# f = open("unit_testing.png", mode="rb")
# print(f.read())

# 如果又想读，又想写, r+, w+, a+
# with 语句，能帮我们自动关闭文件

with open("unit_testing.png", mode="rb") as f:
    f.read()
    # 最后一行，会自动调用 f.close()


def add(a, b):
    return a + b




print(__name__)




