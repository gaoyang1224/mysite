"""
一、请指出下面那些为可变类型的数据，那些为不可变类型的数据

1、 (11)  不，整，不是元组

2、 {11，22}，  集合，可变

3、 ([11,22,33])，   列表，可变

4、 {"aa":111}，   字典，可变
"""



"""

二、当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，

 要求一：去除列表中的重复元素，

 要求二：删除 77，88，99这三个元素
"""

# 去重
li = [11,22,33,22,22,44,55,77,88,99,11]
li_new = list(set(li))
print(li_new)

# li_new.sort()
# li_new.pop(-1)
# li_new.pop(-1)
# li_new.pop(-1)

#
# li_new.remove(77)
# li_new.remove(88)
# li_new.remove(99)

# 先找到索引
# index_77 = li_new.index(77)

"""

三、有下面几个数据 ，

t1 = ("aa",11)      t2= (''bb'',22)    li1 = [("cc",11)]

请通过学过的知识点，进行相关操作变为如下字典: {"aa":11,"cc":11,"bb":22}

要注意字典中元素的位置（使用python3.5以下的同学不用考虑位置）

"""
t1 = ("aa",11)
t2= ('bb',22)
li1 = [("cc",11)]
new_dict = {}
new_dict[t1[0]] = t1[1]
new_dict[ li1[0][0] ]  = li1[0][1]
new_dict[t2[0]] = t2[1]


# t1 = ("aa",11)
# t2= ("bb",22)
# li1 = [("cc",11)]
#
# # {"aa":11,"cc":11,"bb":22}
# new_list = {}
#
# t1_key = t1[0]
# new_list[t1_key] = t1[1]
#
# new_list[li1[0][0]] = li1[0][1]
#
# new_list[t2[0]] = t2[1]
# print(new_list)


# 把复杂的问题简单话。

t1 = ("aa",11)
t2= ("bb",22)
li1 = [("cc",11)]

my_tuple = [t1, li1[0], t2]

# 序列类型
# [(key,value), (key, value) ]
# print(dict(my_tuple))

li_old = [1,2,3]
# print(dict(li_old))
