#-*-coding:utf-8-*-
# date:2021-03-21
# Author: Eric.Lee
'''
学习内容（Contents）:
    1、将彩色图片 BGR 三通道分离（注意观察 B、G、R 单通道图像素的明暗）
    2、将3个单通道图像进行合并
'''
import cv2 # 加载OpenCV库
import numpy as np
if __name__ == "__main__":
    path = 'images/1.jpg'
    img = cv2.imread(path)
    cv2.namedWindow('image',0)
    cv2.imshow('image',img) # 显示图片

    #图片3通道分离
    (B,G,R) = cv2.split(img)
    #
    cv2.namedWindow('B', 0)
    cv2.imshow('B', B)
    cv2.namedWindow('G', 0)
    cv2.imshow('G', G)
    cv2.namedWindow('R', 0)
    cv2.imshow('R', R)

    # 图片合并
    img_merge = cv2.merge([B,G,R])

    cv2.namedWindow('merge', 0)
    cv2.imshow('merge', img_merge)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
