#-*-coding:utf-8-*-
# date:2021-03-20
# Author: Eric.Lee
'''
学习内容（Contents）:
    1、读取图片
    2、读取图片尺寸
    3、彩色图片转为灰度
'''

import cv2 # 导入OpenCV库

if __name__ == "__main__":

    path = 'images/1.jpg'
    img = cv2.imread(path)

    print("image shape : {} ".format(img.shape)) # 读取图像尺寸

    cv2.namedWindow('image',0)# 定义显示窗口,0：可以鼠标控制显示窗口大小变化，1：显示窗口尺寸不可变化
    cv2.imshow('image',img)# 显示图片

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)# BGR图像转灰度图像

    print("gray shape : {} ".format(gray.shape)) # 读取灰度图尺寸

    cv2.namedWindow('gray',0)
    cv2.imshow('gray',gray)

    cv2.waitKey(0)# 等待，直到键盘有按键按下
    cv2.destroyAllWindows() # 销毁所有显示窗口
