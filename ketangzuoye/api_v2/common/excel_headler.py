"""excel操作"""
import openpyxl


class ExcelHandler:
    def __init__(self, fpath):
        self.fpath = fpath

    # 元组可读性差点
    # def read(self, sheet_name):
    #     """读取文件"""
    #     # 打开文件
    #     wb = openpyxl.open(self.fpath)
    #     print(wb)
    #     # 获取表格
    #     ws = wb[sheet_name]
    #     data = list(ws.values)
    #     return data[1:]

    def read(self, sheet_name):
        """读取文件"""
        # 打开文件
        wb = openpyxl.open(self.fpath)
        print(wb)
        # 获取表格
        ws = wb[sheet_name]
        data = list(ws.values)
        # 关闭文件
        wb.close()
        header = data[0]
        all_data = []
        for row in data[1:]:
            row_dict = dict(zip(header, row))
            print(row_dict)
            all_data.append(row_dict)
        return all_data

    def write(self, sheet_name, data, row, column):
        """写入excel数据"""
        wb = openpyxl.load_workbook(self.fpath)
        # 获取表格
        ws = wb[sheet_name]
        ws.cell(row=row, column=column).value = data
        # 通过workbook 保存和关闭
        wb.save(self.fpath)
        wb.close()


if __name__ == '__main__':
    xls = ExcelHandler('cases.xlsx')
    excle_data = xls.read('register')
    print(excle_data)
