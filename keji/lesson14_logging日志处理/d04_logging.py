"""
直接使用 logging 有一下问题：
- info 信息没有产生
- 文件输出日志
- 时间，运行日志的位置。

最好不要直接用 logging.info 这样的操作。
学习的时候：帮助我们理解 logging 的概念
"""

import logging

class Dog():

    def __init__(self, color):
        logging.info("正在初始化")
        self.color = color
        logging.info("获取属性 color ")
        self.ke = "dog"
        logging.warning("警告，。。。。")
        try:
            a = []
            a[100]
        except IndexError:
            logging.error("超出异常错误，这里有错误，赶紧来处理！！！！")

    def run(self):
        print("狗在跑")


dog = Dog("黑色")
# print("已经定义好了 color 属性")