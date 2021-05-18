"""yaml 文件解析

pip install pyyaml

yaml 注意两个问题：
- key 后面的冒号： 加空格
- 层级要缩进
- 可以用注释 #

yaml 是现在最主流用的配置文件。 docker, k8s
"""
import yaml

# 打开文件
with open('python36.yaml', encoding='utf-8') as f:
    data = yaml.load(f, Loader=yaml.SafeLoader)

print(data)
print(data['db']['port'])
print(data['users'][1]['password'])
print(data['users'][0])

# 封装函数。
