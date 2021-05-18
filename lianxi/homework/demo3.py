# f = open ("demo.txt",mode ="r",encoding="utf-8")
# f.read()
# f.write()
# f.close()

a = (1, 2, 3, 4)
print(min(a))

b = (1, 2, 3)
print(sum(b))

b = eval("4+6")
print(b)

b = eval("3*6")
print(b)

a = "{'name':'gaoyang'}"
print(type(a))

print(type(eval(a)))
# print(eval(a['name']))
print(eval(a)['name'])


#zip
title = ["id","title","url"]
date = [1,"登录","www.baidu.com"]

total = zip(title,date)
print(total)
print(dict(total))

f = open("demo4.txt",mode='w',encoding="utf-8")
# print(f.read())

#readlines
# print(f.readlines())


f = open("demo.txt",mode='w',encoding="utf-8")
f.write("hahahaha")
f.close()

#不想覆盖之前的内容（a）
# f = open("demo.txt",mode='a',encoding="utf-8")
# f.write("666666666666")
# f.close()

#不想被修改(x)
# 8

#二进制类型，图片，RGB   (rb)
f = open("hhhh.jpg",mode="rb")
print(f.read())

#想读想写（看第一步操作）r+  a+   w+
# f = open("hhhh.jpg",mode="a+")
# f.write()
# f.read()


#经常忘记close
with open("hhhh.jpg",mode="rb") as f:
    f.read()

