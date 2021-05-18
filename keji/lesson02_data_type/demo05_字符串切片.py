## 切片：想获取多个字符的时候，你有把刀，去切这个字符串
name = "yuze wang"

# 开始位置和结束位置
# 公式1： 字符串[start:end]
# uz, e 不在里面 ：顾头不顾腚， 骨头不顾尾
print(name[1:3])
print(name[0:5])

# 公式2： 字符串[start:end:step]
# 0,2,4
# 0, 3,
print(name[0:6:3])

# 公式3： 字符串[start:]
print(name[1:])
print(name[:6])

# 复制
print(name[:])  #
name_cp = name[:]
print(name_cp)


# 步长能不能为负数

# 没有取到值
name = "yuze wang"
print(name[-3: -1])   # 2, 1
print(name[-1: -3: -1])  # -2, - 1

# 总结
# 心法：
# - 第一步：end - start  1
# - 第二部：step  1
# 两个计算保持符号一致，
# print(name[-1: 0: 1 ])   # 1, 1

# 厉害
#

# print(name[3, -2, 1])

# 倒序
print(name[::-1])