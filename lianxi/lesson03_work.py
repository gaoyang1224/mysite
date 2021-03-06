#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Author:lynne
# @Time:2020/12/5 15:45
# @File:lesson03_work.py
# @Software:PyCharm
"""
列表等数据类型操作
1、.删除如下列表中的"矮穷丑"，写出 2 种或以上方法：
info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
2、现在有一个列表 li2=[1，2，3，4，5]，
请通过相关的操作改成li2 = [0，1，2，3，66，4，5，11，22，33]，
请写出删除列表中元素的方法，并说明每个方法的作用
一、请指出下面那些为可变类型的数据，那些为不可变类型的数据
1、 (11)
2、 [11，22]
3、 ([11,22,33])
二、当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，
删除 77，88，99这三个元素
三，将上个作业的相亲节目用列表实现
某相亲节目需要获取你的个人信息，请存储你的：姓名、性别、年龄，
b. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
c, 平台为了保护你的隐私，需要你删除你的联系方式；
d, 你为了取得更好的成绩，需要取一个花名，并修改自己的身高和其他你觉得需要改的信息。
e, 你进一步添加自己的兴趣，至少需要 3 项。
"""
'''
1、删除如下列表中的"矮穷丑"，写出 2 种或以上方法：
info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
解题思路：
    1、先列出列表删除的方法：remove、pop、del、clear
    2、根据题目要求删除“矮穷丑”，可选择remove按值删除，因为已经知道元素为“矮穷丑”
    还可以选择pop按索引删除，因为知道“矮穷丑”这个元素，可以使用index函数查找处改元素的索引，然后根据索引来删除，
    同理del；clear操作可将列表清空，自然也就删除了“矮穷丑”
'''
#第一种使用remove
info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
info.remove("矮穷丑")
print(info)
#第二种使用pop
info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
index_i = info.index("矮穷丑")
info.pop(index_i)
print(info)
#第三种使用del
info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
index_i = info.index("矮穷丑")
del info[index_i]
print(info)
#第三种使用clear，清空列表
info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
info.clear()
print(info)

'''
2、现在有一个列表 li2=[1，2，3，4，5]，
请通过相关的操作改成li2 = [0，1，2，3，66，4，5，11，22，33]，
解题思路：
    1、观察改成的结果，多了0,66,11,22,33这几个元素
    2、0是在列表index为0处插入，66是在index为4处插入，根据索引插入元素使用index
    3、11,22,33这三个元素，可用多个元素增加，extend在列表最后添加[11,22,33]
请写出删除列表中元素的方法，并说明每个方法的作用
'''
li2 = [1,2,3,4,5]
li2.insert(0,0)
li2.insert(4,66)
li2.extend([11,22,33])
print(li2)
#请写出删除列表中元素的方法，并说明每个方法的作用
#remove():列表.remove(元素)，按列表中某个元素去删除；
#pop():列表.pop(index),按索引位置去删除列表中的某个元素；
#del:del 列表[index],删除某个索引位置的元素，从内存中彻底删除。
#clear:列表.clear(),清空整个列表内的元素

'''
一、请指出下面那些为可变类型的数据，那些为不可变类型的数据
1、 (11)
2、 [11，22]
3、 ([11,22,33])
答：不可变类型的数据：1、(11)
   可变类型的数据：2、[11,22],3、([11,22,33])
解题思路：
    1、不可变类型：整型、字符串、元组
    2、可变型类型：列表、字典、set
    而题目中，(11)为整型、[11,22]为列表、([11,22,33])为列表
    故不可变类型的数据：1、(11)
   可变类型的数据：2、[11,22],3、([11,22,33])
'''

'''
二、当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，
删除 77，88，99这三个元素
解题思路：列表的删除只能一个一个的删除，不能多个删除，因为删除是危险的
    因为知道元素，故删除操作可使用remove根据元素删除
'''
li = [11,22,33,22,22,44,55,77,88,99,11]
li.remove(77)
li.remove(88)
li.remove(99)
print(li)

'''
三，将上个作业的相亲节目用列表实现
某相亲节目需要获取你的个人信息，请存储你的：姓名、性别、年龄，
b. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
c, 平台为了保护你的隐私，需要你删除你的联系方式；
d, 你为了取得更好的成绩，需要取一个花名，并修改自己的身高和其他你觉得需要改的信息。
e, 你进一步添加自己的兴趣，至少需要 3 项。
解题思路：
    1、需要存储个人信息，使用列表，列表元素使用字典，这样能知道每一个元素的值代表什么意思
    2、b选项，需要对列表进行增加操作
    3、c选项，需要对列表进行删除操作
    4、d选项，需要对列表进行插入元素操作，以及修改操作
    5、e选项，需要对列表进行多个元素的添加
'''
personal_information = [{"姓名":"lynne"},{"性别":"女"},{"年龄":32}]
#b. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
personal_information.append({"身高":"153cm"})
personal_information.append({"联系方式":"12345678901"})
print(personal_information)
#c, 平台为了保护你的隐私，需要你删除你的联系方式；
personal_information.remove({"联系方式":"12345678901"})
print(personal_information)
#d, 你为了取得更好的成绩，需要取一个花名，并修改自己的身高和其他你觉得需要改的信息。
personal_information.insert(1,{"花名":"嘟嘟"})
print(personal_information)

index_1 = personal_information.index({"身高":"153cm"})
index_2 = personal_information.index({"年龄": 32})
personal_information[index_1] = {"身高":"160cm"}
personal_information[index_2] = {"年龄":18}
print(personal_information)

#e, 你进一步添加自己的兴趣，至少需要 3 项。
personal_information.extend([{"兴趣1":"看书"},{"兴趣2":"爬山"},{"兴趣3":"看剧"},{"兴趣4":"学习"}])
print(personal_information)
