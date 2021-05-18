"""
return
1, 决定返回值
2, 函数遇到 return 就会终止
"""

def add(a, b):
    c = a + b
    d = c * a
    e = d * b
    print("before finished")
    if d < 3:
        return "1"
    print("2")
    return "3"
    # break
    print("hello world")
    print("yuz")

b = add(3,4)
# TODO: 没有 print ，就不会出现在品目上。
# print(b)

c = add(1,1)
print(c)