import re

my_string= 'gaoyangaiminxiao'
pattern = 'gaoyang'
result = re.search(pattern=pattern,string=my_string)

# 匹配对象
print(result)

# 最终结果,默认值为0
print(result.group(0))

# []
my_string= 'gaayangaiminxiao'
pattern = 'ga[abcdo]yang'
result = re.search(pattern=pattern,string=my_string)
print(result)
