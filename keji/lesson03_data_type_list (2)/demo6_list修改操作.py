# 多个值
songs = ["千里之外", "2002年的第一场雪", "那一夜"]
# 添加一个元素 公式：变量名.append（"新增的元素"）
# 用的多
songs.append("课代表")
print(songs)

# 一次添加多个元素，列表合并
songs.extend(['歌1', '歌2'])
print(songs)

# 可以选择添加的位置，insert
songs.insert(1, 2)
print(songs)

# 删除操作。 删除所有的元素
# 清空列表当中的元素
# songs.clear()
# print(songs)

# 一个一个删 remove, 根据值删除
songs.remove("千里之外")
print(songs)

# 根据索引删除
songs.pop(1)
print(songs)

# del songs[1]
# del songs[0]
# print(songs)


# 修改
# 修改索引为 0 的元素
songs[0] = 1
print(songs)

# 查， 索引，切片
print(songs.count("那一夜"))
# 获取索引
print(songs.index("课代表"))
# 字符串当中 find 喝 index 区别：找不到 index 报错， find -1
# print("我是谁".index("雨泽"))

# 排序
songs = [3,6,4,5]
songs.sort()
print(songs)

# 反序
songs.reverse()
print(songs)