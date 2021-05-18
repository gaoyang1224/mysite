# 多个数据需要执行同样的操作。while, for
# for
# for 被循环的数据需要多个数据，list, tuple, dict, str

# for 循环需要数据，while 需要条件。

# names = ["Hero", "高宁", "哈哈", "随风", "阿然"]
#
# for name in names:
#     # name = names[0]
#     # name = names[1]
#     print("{}我喜欢yuz".format(name))
#     # names index += 1


# 能不能循环 tuple
# names = ("Hero", "高宁", "哈哈", "随风", "阿然")
#
# for name in names:
#     # name = names[0]
#     # name = names[1]
#     print("{}我喜欢yuz".format(name))


# 字符串 for
# name = "orange"
# for i in name:
#     print(i)


# 字典
dalao = {"1": "旧梦", "2":"触手可得", "3":"鲸鱼", "top": "上善若水"}
for bigboss in dalao:
    print(bigboss)

for bigboss in dalao.keys():
    print(bigboss)

# 循环 value
for bigboss in dalao.values():
    print(bigboss)

# 想同时获取 key, value
for k, v in dalao.items():
    print(k, v)

# 遍历 "orange"
# for i in "orange"[::-1]:
#     print(i)