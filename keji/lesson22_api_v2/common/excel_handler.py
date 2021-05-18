"""excel操作"""
from pprint import pprint

import openpyxl


class ExcelHandler:
    def __init__(self, fpath):
        self.fpath = fpath

    # def read(self, sheet_name):
    #     """读取数据"""
    #     # 打开文件
    #     wb = openpyxl.open(self.fpath)
    #     print(wb)
    #     # 获取表格
    #     ws = wb[sheet_name]
    #     data = list(ws.values)
    #     return data[1:]

    def read(self, sheet_name):
        """读取数据"""
        # 打开文件
        wb = openpyxl.open(self.fpath)
        # 获取表格
        ws = wb[sheet_name]
        data = list(ws.values)
        header = data[0]

        all_data = []
        for row in data[1:]:
            row_dict = dict(zip(header, row))
            all_data.append(row_dict)
        return all_data





if __name__ == '__main__':
    xls = ExcelHandler('cases.xlsx')
    excel_data = xls.read('register')
    # excel_data
    print(excel_data)