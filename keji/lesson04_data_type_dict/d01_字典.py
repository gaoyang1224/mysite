movies = ["画皮", "蜡笔小新", "上海堡垒", "你名字", "心花怒放", "大话西游"]
print(movies[2])

# 列表尽量存储的是意义相近的元素，
# 贴标签，
# 字典
# 字典的表示 {}
# 空的字典
movies = {}
print(type(movies))
print(len(movies))

# 字典公式： {key:value, key1:value1, key2:value2}
movies = {"favor": "画皮",
          "first_with_gf": "蜡笔小新",
          "second_with_gf": "上海堡垒",
          "hate": "你的名字",
          "cried": "心花怒放",
          1: "大话西游",
          "0": "情人"
          }

# 通过 key  获取某个值 (索引)
print(movies["favor"])
print(movies["hate"])
print(movies[1])  # KeyError
print(movies["0"])

# 切片 字典 # 不行，没有同时获取多个的操作
# movies["favor": "hate"]

# key 是有要求的。
# 第一种情况：如果一个字典当中有 2 key 是一样的会怎么办？？
# 字典里面可以存在重复的key 吗？？
# 作为一个合法的字典，key 不应该有重复的。 key 是要唯一的。
movies = {"favor": "画皮",
          "first_with_gf": "蜡笔小新",
          "second_with_gf": "上海堡垒",
          "hate": "你的名字",
          {1:2}: "大话西游"
          }
print(movies["hate"])

# key 使用list 报错：unhashable type
# list 可以作为 key 吗？？ 不可以
# 元组可以吗？ 可以
# 字典可以吗？？
# key: 字典不可以
# key: 不可变类型
print(movies[{1: 2}])



# a = "hello"
# a = "world"
# print(a)
