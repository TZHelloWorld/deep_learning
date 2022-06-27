# -*- coding: UTF-8 -*-
r"""
@time : 2022/6/24 14:39
@Author ：tz
@File ：文件操作.py
"""
# 主要是测试os功能
import os

# 如果dir_path目录不存在，则创建，否则不创建
dir_path = "./dir"
os.makedirs('dir_path', exist_ok=True)

# 判读是否存在文件
files_path = "./file.txt"
assert os.path.exists(files_path), "path: '{}' does not exist.".format(files_path)


# 文件的打开和关闭操作
f = open("file.txt", "r", encoding="utf-8")  # 打开文件，“读模式”，只能读，得到文件句柄并赋值给一个变量
print(f.read())  # 读文件所有内容，读完之后文件光标跳到最后,文件大时慎用
f.close()

# with语句作用，为了避免打开文件后忘记关闭
with open("file_test", "r", encoding="utf-8") as f:  # 类似于f = open("file_test","r",encoding="utf-8")
    print(f.read())




