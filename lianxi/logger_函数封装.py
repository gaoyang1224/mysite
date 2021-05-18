import logging


def logger(name='root',
           levelname='DEBUG',
           stream_handler_level='DEBUG',
           file=None,
           fmt_str="%(asctime)s--%(levelname)s/%(name)s/%(message)s/%(filename)s/%(lineno)s",
           file_handler_level='INFO'):
    # 获取日志收集器
    logger = logging.getLogger(name)
    logger.setLevel(levelname)

    fmt = logging.Formatter(fmt_str)

    # 获取日志处理器、设置级别
    handler = logging.StreamHandler()
    handler.setLevel(stream_handler_level)
    # 处理器添加到收集器上
    logger.addHandler(handler)
    handler.setFormatter(fmt)

    # 文件处理器、设置级别
    if file:
        file_handler = logging.FileHandler(file, encoding='utf-8')
        file_handler.setLevel(file_handler_level)
        logger.addHandler(file_handler)
        file_handler.setFormatter(fmt)
    return logger


if __name__ == '__main__':
    logger = logger(file="pyhton36.log")
    logger.info("hello")
