# 1、.删除如下列表中的"矮穷丑"，写出 2 种或以上方法：
info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
# info.remove("矮穷丑")
info.pop(3)
print(info)

# 2、现在有一个列表 li2=[1，2，3，4，5]，
# 请通过相关的操作改成li2 = [0，1，2，3，66，4，5，11，22，33]，
li2 = [1, 2, 3, 4, 5]
li2.extend([11,22,33])
li2.insert(0,0)
li2.insert(4,66)
print(li2)

# 3、写出删除列表中元素的方法，并说明每个方法的作用
# 只能全部清除                       例:name.clear()
# 清除单个元素,按值清除               例:name.remove(" ")
# 通过索引清除,可以删除单个或最后一个   例:name.pop(4)或name.pop()
# 通过索引清除                       例:del name[3]

# 4、请指出下面那些为可变类型的数据，那些为不可变类型的数据
# 1、 (11)
# 2、 [11，22]
# 3、 ([11,22,33])
# 1是number,属于不可变类型,2和3是列表，属于可变类型
# 因为list，dict，set是可变类型,string,number,tuple是不可变类型,不可变类型只能查,不能进行增删改

# 5、当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，
# 删除 77，88，99这三个元素
li = [11,22,33,22,22,44,55,77,88,99,11]
del li[7:10]
print(li)

# 6、用列表形式
# a. 某相亲节目需要获取你的个人信息，请存储你的：姓名、性别、年龄，
personal_information =["张三","男",18]
# b. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
personal_information.extend([180,"15198546875"])
# c, 平台为了保护你的隐私，需要你删除你的联系方式；
personal_information.pop()
# d, 你为了取得更好的成绩，需要取一个花名，并修改自己的身高和其他你觉得需要改的信息。
personal_information.append("南京吴彦祖")
personal_information[3] = 190
# e, 你进一步添加自己的兴趣，至少需要 3 项。
personal_information.extend(["唱歌","跳舞","运动","睡觉"])

print(personal_information)