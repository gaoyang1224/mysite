# 可变类型
# 增删改查
# key-value : 键值对

movies = {"favor": "画皮"}
# 添加元素， insert
movies["new_key"] = "大话西游"
print(movies)

# 删除
# movies.pop("favor")
# print(movies)

# 修改, 已经存在的 key
# 修改和添加的语法是一样的
# 之前没有这个 key ， 添加， 有了，就是修改
movies["new_key"] = "小花"
print(movies)


# 获取所有的 key
print(movies.keys())
# 获取 values
print(movies.values())

# key,value
print(movies.items())

cases = [
    {"url": "", "expected": ""},
    {"url": "", "expected": ""},
    {"url": "", "expected": ""}
]