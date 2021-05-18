# list

# 有多个数据需要存储。
# 千里之外，那一夜，惊雷，告白气球

song1 = "千里之外"
song2 = "那一夜"

# 列表作用存储多个数据的。多个数据有顺序的。
# 存钱罐
# java 数组，
songs = ["千里之外",
         "那一夜",
         "惊雷",
         "告白气球",
         100,
         "钻石",
         True,
         (1,2),
         {"username":"yuz"},
         [1,2, ["a", "b"]]
         ]
# 不止可以存储字符串，数字， bool,
# 列表里可以存储任意类型的数据。
print(songs)
# 获取类型
print(type(songs))
# 长度
print(len(songs))

# 索引, 获取一个元素
print(songs[0])
print(songs[-2])
print(songs[-1])
# 超出索引范围报错
# print(songs[999])

# 切片获取多个, 列表的切片得到的数据类型：列表
print(songs[1:3])

