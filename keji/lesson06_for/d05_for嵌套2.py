# 生成一个列表或者数据
# range(start, end, step)
# [1,3,5,7]
# for i in range(1,9,2):
#     print(i)

# step 和 start 可以省略
# for i in range(1, 101):
#     print(i)

# for i in range(10):
#     print(i)

for i in range(1, 10):
    for j in range(1, 10):

        print("{} * {} = {}".format(i, j, i * j), end="\t")
    print()



