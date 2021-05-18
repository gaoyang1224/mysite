"""字符串的格式化"""

name = "李东霞"
money = 100000000
money_chinese = "一千万"

ticket = """
今收到  {}
交来的  {}
人名币  {}
""".format(name, money, money_chinese)
print(ticket)

# print("a" + str(100))