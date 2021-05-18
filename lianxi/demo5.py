def convent_to_dict(line):
    infos = line.split("@")
    info_dict = {}
    for info in infos:
        info_list = info.split(":")
        info_dict[info_list[0]] = info_list[1]
    return info_dict




f = open("wenjian2.txt", encoding="utf-8")
lines = f.readlines()
print(lines)
new_lines = []
for line in lines:
    new = convent_to_dict(line.strip())
    new_lines.append(new)
print(new_lines)

import time
a = time.time()
print(a)

from lianxi import demo04
a = demo04.write_file()