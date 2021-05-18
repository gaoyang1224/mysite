# open 打开文件
# 文件的路径, 如果没有路径，在当前目录查找文件。

# 得到文件 ascii
# 声明文件的编码格式
f = open("demo.txt", encoding='utf-8')
# 读取文件数据
print(f.read())
# readlines
print(f.readlines())
f.close()


# 文件的写入
# 打开文件的模式：r, w,
f = open("demo1.txt", mode="w", encoding='utf-8')
f.write("hello, work")
f.close()


# 文件的关闭
# 还有其他的额外的用法。
# 模块，路径，


