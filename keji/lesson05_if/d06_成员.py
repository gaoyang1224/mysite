# 针对多个值的运算
# {"token": "fslfjwoepff"}
resp = '{"token": "fslfjwoepff"}'
print("token" in resp)
print("token" not in resp)

# 列表
dalao = ["clista", "YW", "haha"]
print("小脾气" in dalao)
#
dalao.append("小脾气")
print("小脾气" in dalao)

# 字典
dalao = {"1": "clista", "2": "学生", "3": "T6"}
# 不在里面，必须经过 key
# TODO: 字典的 in 指的是 key, 不是 value
print("2" in dalao)

