# s = {[1,2]:[3,4],'age':18}
# print(type(s))

# personal_information = {'name': 'GY', 'age': '24', 'sex': '男', 'height': '179', 'weight': '75kg'}
# print(personal_information)

# print(s)

# a = 1
# b = '2'
# print(a < b)

# s = 'abcdef'
# print('ac' not in s)

# print(False + 1)
# print(True)

# a = 0
# b = 1
# print(a and b)
#
# print(not 1)
# print(not None)
#
#
# def add(a, b):
#     c = a+b
#     return c+2
#
# a =1
# b =2
# print(add(a,b))

# a = 5
#
#
# def add():
#     global a
#     a = a + 1
#     print(a)
#     return None

# add()
#
# print(abs(-1))
# print(eval("4+6"))
#
# b = "{'name':'gaoyang'}"
# print(type(b))
# print(eval(b)['name'])
#
# title = ["id", "name", 'age']
# data = [1, 'gaoyang', 18]
# totle = zip(title, data)
# print(dict(totle))
#
# # f = open("wenjian.txt", encoding='UTF-8')
# # print(f.read())
#
# f = open("wenjian1.txt", mode="w", encoding='UTF-8')
# f.write("你好")
# f.close()



def string_from_list(list):

    new_str = ""
    for el in list:
        for v in el.values():
            new_str += str(v) + ","
    new_str = new_str.rstrip(",")
    new_str += "\n"
    return new_str


def write_file(list1, file_name):
    f = open(file_name, mode='w', encoding="UTF-8")
    f.write(list1)
    f.close()
    return file_name



personal_information = [{'name': 'GY', 'age': '24', 'sex': '男', 'height': '179', 'weight': '75kg'},
                        {'name': 'minxiao', 'age': '23', 'sex': '女', 'height': '169', 'weight': '51kg'}]

new_str = string_from_list(personal_information)
print(new_str)
write_file(new_str, "person.txt")