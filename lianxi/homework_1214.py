# 编写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
# 提示：参数为列表的变量 lst
# def get_content(lst):
lst = ["a", "b", "c", 1, 2, 3]


def get_content(lst):
    if len(lst) > 2:
        for i in range(2, len(lst)):
            lst.pop()
    return lst


get_content(lst)
print(lst)

# 列表去重
# 定义一个函数 def remove_element(m_list):，将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素
# 编写如下程序
m_list = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]


# def remove_element(m_list):
#     n_list = list(set(m_list))
#     return n_list
#
# print(remove_element(m_list))



def remove_element(m_list):
    c_list = []
    for e in m_list:
        if e not in c_list:
            c_list.append(e)
    return c_list
print(remove_element(m_list))


# 尝试函数封装： def func_name(height, weight):
#
# 一个人的身高(m)和体重(kg),  height=0.17,  weight=65，根据BMI公式（体重除以身高的平方）计算他的BMI指数
#
# a.例如：一个65公斤的人，身高是1.62m，则BMI为 :  65 / 1.62 ** 2 = 24.8
#
# b.根据BMI指数，给与相应提醒
#
#
#
# 低于18.5： 过轻 18.5-25：   正常 25-28：      过重 28-32：      肥胖 高于32：   严重肥胖

height = float(input("请输入你的身高（m）:"))
weight = float(input("请输入你的体重（kg）:"))
BMI = weight / (height ** 2)


def func_name(height, weight):
    if BMI <= 18.5:
        return "过轻"
    elif 18.5 < BMI <= 25:
        return "正常"
    elif 25 < BMI <= 28:
        return "过重"
    elif 28 < BMI <= 32:
        return "肥胖"
    else:
        return "严重肥胖"


print(func_name(height, weight))
