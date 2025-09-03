#-*-coding:utf-8-*-
# date:2021-03-20
# Author: Eric.Lee
'''
学习内容（Contents）:
    1、图像缩放
'''

import cv2 # 导入OpenCV库

if __name__ == "__main__":

    path = 'images/1.jpg'

    img = cv2.imread(path)# 读取图片
    print("img shape : {}".format(img.shape))
    cv2.namedWindow('image',0)
    cv2.imshow('image',img) # 显示图片

    #------------------------------------------------------------------------------------------------
    # cv2.INTER_LINEAR,cv2.INTER_CUBIC,cv2.INTER_NEAREST,cv2.INTER_AREA,INTER_LANCZOS4 ： 不同的查找方式
    img_r = cv2.resize(img, (256,256), interpolation = cv2.INTER_LINEAR) # 将原图缩放到尺寸 256*256 双线性插值（默认设置）
    print("img_r shape : {}".format(img_r.shape))
    cv2.namedWindow('INTER_LINEAR',0)
    cv2.imshow('INTER_LINEAR',img_r)
    #
    img_r = cv2.resize(img, (256,256), interpolation = cv2.INTER_CUBIC) # 将原图缩放到尺寸 256*256 4x4像素邻域的双三次插值
    cv2.namedWindow('INTER_CUBIC',0)
    cv2.imshow('INTER_CUBIC',img_r)
    #
    img_r = cv2.resize(img, (256,256), interpolation = cv2.INTER_NEAREST) # 将原图缩放到尺寸 256*256 最近邻插值
    cv2.namedWindow('INTER_NEAREST',0)
    cv2.imshow('INTER_NEAREST',img_r)
    #
    img_r = cv2.resize(img, (256,256), interpolation = cv2.INTER_AREA) # 将原图缩放到尺寸 256*256 使用像素区域关系进行重采样
    cv2.namedWindow('INTER_AREA',0)
    cv2.imshow('INTER_AREA',img_r)
    #
    img_r = cv2.resize(img, (256,256), interpolation = cv2.INTER_LANCZOS4) # 将原图缩放到尺寸 256*256 8x8像素邻域的Lanczos插值
    cv2.namedWindow('INTER_LANCZOS4',0)
    cv2.imshow('INTER_LANCZOS4',img_r)


    cv2.waitKey(0)
    cv2.destroyAllWindows() # 销毁所有显示窗口
