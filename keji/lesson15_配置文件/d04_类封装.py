# 导入信息放在模块的最上面
import logging


class MyLogger(logging.Logger):

    def __init__(self,
                 name='root',
                 logger_level='DEBUG',
                 stream_handler_level='DEBUG',
                 file=None,
                 file_handler_level='INFO',
                 fmt_str="time:%(asctime)s--%(levelname)s:%(name)s:%(message)s--%(filename)s---%(lineno)s"):

        # 获取日志收集器 logger
        super().__init__(name, logger_level)
        # self == 收集器
        # self.setLevel(logger_level)

        # "time:%(asctime)s--%(levelname)s:%(name)s:%(message)s--%(filename)s---%(lineno)s"
        fmt = logging.Formatter(fmt_str)
        # 日志处理器
        handler = logging.StreamHandler()
        handler.setLevel(stream_handler_level)
        self.addHandler(handler)
        handler.setFormatter(fmt)
        # 文件处理器
        if file:
            file_handler = logging.FileHandler(file, encoding="utf-8")
            file_handler.setLevel(file_handler_level)
            self.addHandler(file_handler)
            file_handler.setFormatter(fmt)

    # def info(self):
    #     pass


if __name__ == '__main__':
    # log = MyLogg()
    # # log.info()
    # log.logger.info("hello")

    # logger.info()
    # log = MyLogg("python36")
    # log.error("hello")
    pass