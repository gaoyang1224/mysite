"""自定义内置数据"""
from faker import Faker
from faker.providers import BaseProvider


class PY36(BaseProvider):
    names = ('高阳', '闵笑', '张三', '李四')

    def py36_name(self):
        return self.random_element(self.names)


# 添加provider
fk = Faker(locale='zh_CN')
fk.add_provider(PY36)

print(fk.py36_name)
