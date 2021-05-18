"""excel操作"""
from pprint import pprint

import openpyxl


class ExcelHandler:
    def __init__(self, fpath):
        self.fpath = fpath

    def read(self, sheet_name):
        """读取数据"""
        # 打开文件
        wb = openpyxl.open(self.fpath)
        print(wb)
        # 获取表格
        ws = wb[sheet_name]
        # 获取所有数据
        data = list(ws.values)
        all_data = []
        header = data[0]
        for row in data[1:]:
            row_data = dict(zip(header, row))
            all_data.append(row_data)
        return all_data


    def write(self, sheet_name, data, row, column):
        """写入数据"""
        wb = openpyxl.open(self.fpath)
        ws = wb[sheet_name]
        ws.cell(row=row, column=column).value = data
        wb.save(self.fpath)
        wb.close()


if __name__ == '__main__':
    xls = ExcelHandler('cases.xlsx')
    excel_data = xls.read('register')
    pprint(excel_data)
