import time

print(time.time())

import lianxi.homework.demo6
a = lianxi.homework.demo6.add(3,4)
print(a)



from lianxi.homework import demo6
a = demo6.add(5,6)
print(a)

from lianxi.homework.demo6 import add
a = add(5,6)
print(a)


#导入所有（慎用）
from lianxi.homework.demo6 import *

import lianxi.homework.demo6
print(__name__)