keys = ["url", "method"]

cases = [
    ["/login", "get"],
    ["/register","post"],
    ["/project", "put"],
]


lst = []
for case in cases:
    adict = {}
    # 同时获取列表的索引和值
    for idx, data in enumerate(case):
        # adict["url"] = "/login"
        # adict['method"]= "post"
        adict[ keys[idx] ] = data
    print(adict)
    lst.append(adict)
print(lst)



# cases = [
#     {"url":"/register","method": "get"},
#     {"url": "/register", "method": "post"},
#     {"url": "/project", "method": "put"},
# ]


# lst = ["a", "b", "c"]
# for index, i in enumerate(lst):
#     print(index, i)