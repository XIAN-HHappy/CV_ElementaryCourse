#-*-coding:utf-8-*-
# date:2021-03-20
# Author: Eric.Lee
'''
学习内容（Contents）:
    OpenCV的彩色图像格式为：BGR
    浮点型数组显示像素值范围：0.~1.
    无符号整形显示像素值范围：0~255
    1、显示R、G、B图像
'''

import cv2 # 导入OpenCV库
import numpy as np # 导入numpy库

if __name__ == "__main__":
    img_h = 480 # 图像高
    img_w = 640 # 图像宽

    #------------------------------------------------浮点 float 0~1.
    img = np.zeros([img_h,img_w,3], dtype = np.float) # 通过numpy初始化一个全黑的图片
    cv2.namedWindow('black', 1)
    cv2.imshow('black', img)
    cv2.waitKey(0)

    img[:,:,0].fill(1.0) # 0 通道填充为 1.，即蓝色
    cv2.namedWindow('B', 1)
    cv2.imshow('B', img)

    img = np.zeros([img_h,img_w,3], dtype = np.float)
    img[:,:,1].fill(1.0)# 1 通道填充为 1.，即绿色
    cv2.namedWindow('G', 1)
    cv2.imshow('G', img)

    img = np.zeros([img_h,img_w,3], dtype = np.float)
    img[:,:,2].fill(1.0)# 2 通道填充为 1.，即红色
    cv2.namedWindow('R', 1)
    cv2.imshow('R', img)

    cv2.waitKey(0)

    cv2.destroyAllWindows() # 销毁所有显示窗口

    #------------------------------------------------无符号整形 uint8 0~255
    img = np.zeros([img_h,img_w,3]).astype(np.uint8) # 通过numpy初始化一个全黑的图片,且通过 astype()转为数据类型 uint8
    cv2.namedWindow('black', 1)
    cv2.imshow('black', img)
    cv2.waitKey(0)

    img[:,:,0].fill(255) # 0 通道填充为 1.，即蓝色
    cv2.namedWindow('B', 1)
    cv2.imshow('B', img)

    img = np.zeros([img_h,img_w,3]).astype(np.uint8)
    img[:,:,1].fill(255)# 1 通道填充为 1.，即绿色
    cv2.namedWindow('G', 1)
    cv2.imshow('G', img)

    img = np.zeros([img_h,img_w,3]).astype(np.uint8)
    img[:,:,2].fill(255)# 2 通道填充为 1.，即红色
    cv2.namedWindow('R', 1)
    cv2.imshow('R', img)

    cv2.waitKey(0)

    cv2.destroyAllWindows() # 销毁所有显示窗口
