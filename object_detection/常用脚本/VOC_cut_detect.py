# -*- coding: UTF-8 -*-
r"""
@time :  2022/6/27 11:24
@Author: tz
@File: VOC_cut_detect.py.py
@Description: 这个是一个通过voc数据格式截取目标detect的脚本代码，按照类别将bounding box圈出来的目标切割出来
"""
import os
import xml.etree.ElementTree as ET

import cv2


def main():
    # JPG文件的目录地址
    img_path = './images/'
    # XML文件的目录地址
    anno_path = './Annotations/'
    # 存结果的文件夹
    cut_path = './crops/'

    # 获取图片文件夹中的文件
    imagelist = os.listdir(img_path)
    # print(imagelist)
    for image in imagelist:
        image_pre, ext = os.path.splitext(image)
        img_file = img_path + image
        img = cv2.imread(img_file)
        xml_file = anno_path + image_pre + '.xml'  # 找到每一个图片对应的xml文件
        # DOMTree = xml.dom.minidom.parse(xml_file)
        # collection = DOMTree.documentElement
        # objects = collection.getElementsByTagName("object")

        tree = ET.parse(xml_file)
        root = tree.getroot()
        # if root.find('object') == None:
        #     return

        # 遍历每个object包裹的目标框
        for obj in root.iter('object'):
            cls = obj.find('name').text
            xmlbox = obj.find('bndbox')
            b = [int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text),
                 int(xmlbox.find('ymax').text)]
            img_cut = img[b[1]:b[3], b[0]:b[2], :]
            path = os.path.join(cut_path, cls)
            # 目录是否存在,不存在则创建
            mkdirlambda = lambda x: os.makedirs(x) if not os.path.exists(x) else True
            mkdirlambda(path)

            # 保存中文乱码问题
            # cv2.imwrite(os.path.join(cut_path, cls, 'cut_img_{}.jpg'.format(image_pre)), img_cut)
            cv2.imencode('.jpg', img_cut)[1].tofile(os.path.join(cut_path, cls, 'cut_img_{}.jpg'.format(image_pre)))

            # for object in objects:
            #     print("start")
            #     name=object.getElementsByTagName('name')[0]
            #     # obj.find('name').text
            #     print(name)
            #     print(type(name))
            #
            #     bndbox = object.getElementsByTagName('bndbox')[0]
            #     xmin = bndbox.getElementsByTagName('xmin')[0]
            #     xmin_data = xmin.childNodes[0].data
            #     ymin = bndbox.getElementsByTagName('ymin')[0]
            #     ymin_data = ymin.childNodes[0].data
            #     xmax = bndbox.getElementsByTagName('xmax')[0]
            #     xmax_data = xmax.childNodes[0].data
            #     ymax = bndbox.getElementsByTagName('ymax')[0]
            #     ymax_data = ymax.childNodes[0].data
            #     xmin = int(xmin_data)
            #     xmax = int(xmax_data)
            #     ymin = int(ymin_data)
            #     ymax = int(ymax_data)
            #     img_cut = img[ymin:ymax, xmin:xmax, :]
            #     cv2.imwrite(cut_path + 'cut_img_{}.jpg'.format(image_pre), img_cut)
            print(f"cut_img_{image_pre}.jpg is ok.........")


if __name__ == '__main__':
    main()
