import json

# 字符串转化为字典
a = '{"username":"gaoyang", "age":18}'
print(json.loads(a))

# 字典转化为字符串
b = {"username":"minxiao", "age":18}
print(json.dumps(b))