# -*- coding: UTF-8 -*-
r"""
@time : 2022/6/24 15:46
@Author ：tz
@File ：misc_utils使用.py
@Address ：https://github.com/misads/misc_utils
"""
import argparse

# pip install utils-misc==0.0.5 -i https://pypi.douban.com/simple/
import misc_utils as utils

parser = argparse.ArgumentParser()
args = parser.parse_args()

# 打印argparse解析的参数print_args
utils.print_args(args)

# utils.cmd('nvidia-smi')

utils.color_print('建立JPEGImages目录', 3)
r"""
misc_utils.color_print(text='', color=0, end='\n')
    Args:
        text(str): text to print.
        color(int):
            * 0       black
            * 1       red
            * 2       green
            * 3       yellow
            * 4       blue
            * 5       cyan (like light red)
            * 6       magenta (like light blue)
            * 7       white
        end(str): end string after colored text.
"""

confirm = input('即将生成annotations，大约需要3-5分钟，是否开始(y/n)? ')

# 如果输入的confirm不是y，则退出程序
if confirm.lower() != 'y':
    utils.color_print(f'Aborted.', 3)
    exit()

# 以一定的概率返回true和false
utils.gambling(prob=0.3, total=1.0)

# 终端渲染进度条progress_bar
for i in range(100):
    utils.progress_bar(i, 100, 'Training...', 'loss:0.45')
