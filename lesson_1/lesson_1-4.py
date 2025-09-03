#-*-coding:utf-8-*-
# date:2021-03-20
# Author: Eric.Lee
'''
学习内容（Contents）:
    1、裁剪自定区域图片
'''

import cv2 # 导入OpenCV库

if __name__ == "__main__":

    path = 'images/1.jpg'

    img = cv2.imread(path)# 读取图片
    cv2.namedWindow('image',0)
    cv2.imshow('image',img) # 显示图片

    print("img shape : {}".format(img.shape))
    #--------------------

    # 裁剪区域不能操过原图的坐标区间
    img_crop = img[400:800,630:900,:] # 裁剪图范围为相对原图坐标,左上坐标（x1,y1）= （630,400），右下坐标 （x2,y2） = (900,800)
    cv2.namedWindow('img_crop',0)
    cv2.imshow('img_crop',img_crop) # 显示图片
    cv2.waitKey(0)

    cv2.destroyAllWindows() # 销毁所有显示窗口
