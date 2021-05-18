# name = "gao yang"
# print(name.count(" "))
#
#
# print(name.replace("gao","GAO"))

number = "123456"
print(number.count("2"))

new_number = ".".join(["花蝶", "花花世界", "飞舞"])
print(new_number)

print("我爱" + "你")

print(number.replace("1", "0"))

print(number.split('2'))

name = "      gaoyang "
print(name)
print(name.strip())

name = "gaoyang"
age = 18
doing = "工作"
demo = "这个叫{}，今年{}，现在在金螳螂{}".format(name, age, doing)
print(demo)

songs = ["那一夜", "玫瑰", "香水有毒", "两只老虎"]
print(type(songs))
print(len(songs))
print(songs[1])
print(songs[0:1])
print(songs[:4:2])
print(songs[:])
print(songs[::-1])
print(songs[-1:-3:-1])
# 增
songs.append("听海")
print(songs)

songs.append(["辣妹子", "伤心太平洋"])
print(songs)

songs.extend(["爱如潮水", "忐忑"])
print(songs)

songs.insert(4, "天天想你")
print(songs)

songs.remove("那一夜")
print(songs)

# songs.clear()
# print(songs)

songs.pop(0)
print(songs)

songs[0] = "我的老家"
print(songs)

print(songs.count("我的老家"))

print(songs.index("我的老家"))

number = [4, 5, 7, 2, 9, 1]
number.sort()
print(number)

number.reverse()
print(number)
