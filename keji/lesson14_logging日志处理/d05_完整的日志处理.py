"""
- 日志收集器 logger:
- 2， 日志收集器级别 level
- 3， 日志处理器准备 handler
- 4， 日志处理器级别设置
- 5， 设置日志格式  format
- 6， 添加日志处理器

- 1、NOSET    0   等于没写，废话。
- 2，debug,  10,  调试，一些额外信息，备注，往往和主体功能无关。 日报里面的备注
- 3，info, 20  主体功能的信息。 日报，做了些啥？
- 4，warning, 30, 警告， 下次可能要出错了。 交警叔叔警告
- 5，error,  40,  犯错，违法。抢红灯
- 6, critical,  50, 极其严重。 抢银行
"""

import logging

# 获取日志收集器 logger
logger = logging.getLogger("python36")
logger.setLevel("INFO")

# 日志处理器
handler = logging.StreamHandler()
handler.setLevel("INFO")

# 文件处理器
file_handler = logging.FileHandler("python36.log", encoding="utf-8")
file_handler.setLevel("INFO")

# 处理器添加到收集器上。
logger.addHandler(handler)
logger.addHandler(file_handler)

# 设置格式
fmt = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
handler.setFormatter(fmt)
file_handler.setFormatter(fmt)


logger.info("正常执行的逻辑")
logger.error("错误")
logger.debug("调试信息")


# 封装成函数， 返回值 logger
# 封装成类。



