from pprint import pprint

import openpyxl

# 打开excel文件
workbook = openpyxl.open("cases.xlsx")
print(workbook)

# 选择sheet表格
ws = workbook['register']
print(ws)

# 获取数据，某个单元格数据
cell = ws.cell(2, 3)
print(cell.value)

# 获取第一行
print(ws[1])

# 获取所有行
print(list(ws.rows))

# 获取所有的数据
pprint(list(ws.values))