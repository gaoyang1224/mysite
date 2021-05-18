# + - * / //  %   **

print(2 + 3)
print(2 - 3)
print(2 * 3)

# 除法： float
print(2 / 3)
print(6 / 3)

# 浮点数，python 算错了
print(2.1 + 3.2)
print(2.1 + 3.1)

# 2.1 + 0.2
print(2.1 + 0.2)

# Decimal
# TODO: 进行浮点数运算，高精度计算，不能直接用 float
# 而要转化成 Decimal ， 里面的数据是字符串类型
from decimal import Decimal

print(Decimal(str(2.1)) + Decimal(str(0.2)) == Decimal(str(2.3)))

# //
print(7 // 3)
# % 取余数，模运算
print(7 % 3)
# 奇数和偶数

# ** 次方， 幂运算
print(3 ** 4)

# print(round(0.345))

