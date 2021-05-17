"""json"""
import json

# 是把 json 格式的字符串转化成 python 当中的字典， 反序裂化
a = '{"username": "yuz", "age": 10}'
print(json.loads(a))

# python的字典转化成 json 格式的字符串，序列化
b = {"name": "星河", "age": 3}
print(json.dumps(b))

a = "{'username': 'yuz', 'age': 10}"
print(json.loads(a))