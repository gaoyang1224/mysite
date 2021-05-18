
# for
cases = [
    ["http://example.com/login", "get", "yuz"],
    ["http://example.com/register", "put", "yw"],
    ["http://example.com/info", "delete", "wen"],
    ["http://example.com/project", "options", "achool"],
    ["http://example.com/interface", "head", "orange"],
]


# 调试手段：print
# debug: pycharm
# 红点：我想让代码在这里暂停， 断点
# python 代码从上带下

for case in cases:
    print("case:", case)
    for data in case:
        print("data:", data)
        # index + 1