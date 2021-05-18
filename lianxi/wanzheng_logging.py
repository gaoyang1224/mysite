import logging


# 获取日志收集器
logger = logging.getLogger("python36")
logger.setLevel("INFO")

# 获取日志处理器、设置级别
handler = logging.StreamHandler()
handler.setLevel("INFO")

# 文件处理器、设置级别
file_handler = logging.FileHandler("python36_logging", encoding='utf-8')
file_handler.setLevel("INFO")

# 处理器添加到收集器上
logger.addHandler(handler)
logger.addHandler(file_handler)

# 设置格式
fmt = logging.Formatter("%(asctime)s--%(levelname)s/%(name)s/%(message)s/%(filename)s/%(lineno)s")
handler.setFormatter(fmt)
file_handler.setFormatter(fmt)


logger.info("正常逻辑")
logger.error("报错。。。。。")
logger.debug("调试")