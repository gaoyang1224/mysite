# from decimal import Decimal
#
# print(Decimal("2.1") + Decimal("2.3") == Decimal("4.4"))
#
# print(1 or 0)


# def get_offer(name, money, food ="apple"):
#     print("{}拿到了{}k的offer".format(name, money))
#     eat(name, food)
#
#
# def eat(name, food):
#     print("{}喜欢吃{}".format(name, food))
#
# get_offer("gaoyang", 13)


# res = []
# # def transform_list_to_dict(cases):
# #     title = cases[0]
# #     for group in cases[1:]:
# #         new_dict = {}
# #         for idx, i in enumerate(group):
# #             key = title[idx]
# #             new_dict[key] = i
# #         res.append(new_dict)
# #     return res
# #
# # cases = [
# #     ['case_id', 'case_title', 'url', 'data', 'excepted'],
# #     [1, '用例1', 'www.baudi.com', '001', 'ok'],
# #     [4, '用例4', 'www.baudi.com', '002', 'ok'],
# #     [2, '用例2', 'www.baudi.com', '002', 'ok'],
# #     [3, '用例3', 'www.baudi.com', '002', 'ok'],
# #     [5, '用例5', 'www.baudi.com', '002', 'ok'],
# # ]
# #
# #
# # print(transform_list_to_dict(cases))


# title = [1, 2, 3]
# data = [4, 5, 6]
# totle = zip(title, data)
# print(dict(totle))

# f = open("demo4.txt", encoding='utf-8')
#
# print(f.read())

f = open("demo4.txt", mode='w', encoding='utf-8')
f.write("55555555555")
f.close()
