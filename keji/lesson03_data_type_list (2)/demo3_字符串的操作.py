name = "yuze waneg"
# 超出范围，就到最后
print(name.count('e'))

name = "雨泽雨泽 雨最闪亮"
print(name.count(" "))

# 字符串拼接, 更加优雅的一种拼接
# 多个字符串一定要放到列表或者元组当中
new_name = "".join(["雨泽", "雨泽", "最闪亮"])
print(new_name)

# 字符串 +
print("雨泽" + "/" + "雨泽" + "/" + "最闪亮")

# replace 替换字符串
name = "雨泽雨泽最闪亮"
# 替换之后要重新赋值
# crista公式：new_name = name.replace("被替换的内容",“新内容”)
# 字符串不可变类型
name = name.replace('雨泽', "随风")
print(name)
# print(new_name)

# split 字符串切割
# 是和 join 对应的。
name = '雨泽/雨泽/最闪亮'
print(name.split("/"))
# 把字符左右两边的字符去掉，默认是空格
print(name.strip(' '))
