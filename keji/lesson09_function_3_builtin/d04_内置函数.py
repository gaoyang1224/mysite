
#
b = min(1,2,3,6)
print(b)

b = max(1,2,3,6)
print(b)


# 列表，元组
a = (1,2,3,4)
print(sum(a))

# eval 把字符串两边的引号去掉，
print("4 + 8")
b = eval("4 + 8")
print(b)

# 4 + 8

a = "{'name': '随风'}"
print(type(a))
# print(a["name"])

print(type(eval(a)))
#
b = eval(a)
b["name"]
print(eval(a)["name"])


# zip
title = ["case_id", "title", "url"]
data = [1, "登录", "http://www.baidu.com"]

total = dict(zip(title, data))

print(total)
