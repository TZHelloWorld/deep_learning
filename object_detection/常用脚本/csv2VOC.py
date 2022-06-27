# -*- coding: UTF-8 -*-
r"""
@time : 2022/6/27 13:42
@Author : tz
@File : csv2VOC.py
@Description : 目标检测中使用CSV转VOC数据集的脚本，主要是生成Annotations目录下的xml文件和ImageSets/Main文件夹下的train.txt等
"""

import csv
import os
from collections import defaultdict

# pip3 install utils-misc==0.0.5 -i https://pypi.douban.com/simple/
import misc_utils as utils

utils.color_print('建立JPEGImages目录', 3)
os.makedirs('Annotations', exist_ok=True)
utils.color_print('建立Annotations目录', 3)
os.makedirs('ImageSets/Main', exist_ok=True)
utils.color_print('建立ImageSets/Main目录', 3)

# # 用于返回指定的文件夹包含的文件或文件夹的名字的列表
# files = os.listdir('D:\临时\示例数据\示例数据\附件1')
# # 对列表进行排序操作
# files.sort()
# print(files)

# 会构建一个默认value为list的字典
mem = defaultdict(list)

confirm = input('即将生成annotations，大约需要3-5分钟，是否开始(y/n)? ')

# 如果对于生成的annotations输入不是y，则退出程序
if confirm.lower() != 'y':
    utils.color_print(f'Aborted.', 3)
    exit()

# 读取csv文件，并转换为相对应的格式：
# 格式如下：
with open('目标的.csv', 'r') as f:
    csv_file = csv.reader(f)
    '''
    读取的csv_file是一个iterator，每个元素代表一行
    '''
    for i, line in enumerate(csv_file):
        # 第一行数据不保存
        if i == 0:
            continue
        print(line)
        # 这个是对每一行数据进行操作，通过赋值给相对应的
        _, filename, class_num, class_name, _, _, x1, y1, x2, y2 = line

        # 对于某些类别可能不存在边界框，那么就不需要进行填写
        if class_num != '0':
            mem[filename].append([class_name, x1, y1, x2, y2])

for i, filename in enumerate(mem):
    # 终端渲染进度条，其中i是当前进度，len(mem)是总进度长度
    utils.progress_bar(i, len(mem), 'handling...')

    # 根据需要，修改长宽的获取方法，要么通过图片获取，要么就手动设置
    # img = cv2.imread(os.path.join('train', filename))
    # height, width, _ = img.shape
    height = 3648
    width = 5472

    # 对每一个jpg文件写一个xml文件并保存到Annotations文件夹中
    with open(os.path.join('Annotations', filename.rstrip('.jpg')) + '.xml', 'w', encoding='utf-8') as f:
        f.write(f"""<annotation>
    <folder>{'A'}</folder>
    <filename>{filename}</filename>
    <size>
        <width>{width}</width>
        <height>{height}</height>
        <depth>{3}</depth>
    </size>
    <segmented>{0}</segmented>\n""")
        for class_name, x1, y1, x2, y2 in mem[filename]:
            f.write(f"""    <object>
        <name>{class_name}</name>
        <pose>{'Unspecified'}</pose>
        <truncated>{0}</truncated>
        <difficult>{0}</difficult>
        <bndbox>
            <xmin>{x1}</xmin>
            <ymin>{y1}</ymin>
            <xmax>{x2}</xmax>
            <ymax>{y2}</ymax>
        </bndbox>
    </object>\n""")
        f.write("</annotation>")

files = list(mem.keys())
files.sort()
f1 = open('ImageSets/Main/train.txt', 'w', encoding='utf-8')
f2 = open('ImageSets/Main/val.txt', 'w', encoding='utf-8')
train_count = 0
val_count = 0
# exit()

with open('ImageSets/Main/all.txt', 'w', encoding='utf-8') as f:
    for filename in files:
        # filename = filename.rstrip('.jpg')

        f.writelines(filename + '\n')

        # 全设置为训练集
        f1.writelines(filename + '\n')
        train_count += 1

        """
        # 给定概率返回True
        if utils.gambling(0.1):  # 10%的验证集
            f2.writelines(filename + '\n')
            val_count += 1
        else:
            f1.writelines(filename + '\n')
            train_count += 1
        """

f1.close()
f2.close()

utils.color_print(f'随机划分 训练集: {train_count}张图，测试集：{val_count}张图', 3)
